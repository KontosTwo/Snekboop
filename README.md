# Snekboop

A horrific misuse of AWS services. Meant to utilize CPU and RAM over the cloud, but we ended up utilizing latency over the cloud instead.


## Problem
Our project aims to solve the problem of servers not having enough immediate CPU and RAM to solve computationally intensive problems. Rather than scaling vertically, which is costly, a developer could utilize snekboop to delegate CPU and RAM capacity and usage to the cloud. 
## Solution Architecture
The public-facing api is query, write. Query maps a function against JSON data under a category in a parallel manner while write writes JSON data to categories. The CLI commands are deploy and add_function. Deploy programmatically sets up the entire snekboop cloud infrastructure and add_function deploys a lambda function and registers its api url to a function_name. 
 
 ![Architecture](https://imgur.com/ADYU8MK.png)
 
The overall design philosophy was to simulate microservices through Lambda and Elasticache. Lambda provides the scalability of compute whereas Elasticache provides the scalability of storage. Both can be independently fine-tuned. 
	Parallelization is achieved by sharding JSON data under a category across several Elasticache instances, and an instance of a mapper Lambda acts upon each Elasticache instance. 
	The lifecycle of a write(category, data) request is: 
1.	API API Gateway receives the request and routes to the Write Lambda. 
2.	Write Lambda requests the shards in which the category resides from the Meta API Gateway 
3.	Meta API Gateway receives the request and routes to the Find Lambda. 
4.	Find Lambda queries from the Meta Elasticache. If a category record was found, the shards URLs are fetched. Otherwise, one is created by using the next n to n + k shards URLs (wraparound accounted for) where n is a global round robin counter and k is the shard level. In either case the shard URLs are returned
5.	Write Lambda asynchronously writes to each shard
The lifecycle of a query(category, function) request is: 
1.	API API Gateway receives the request and routes to the Query Lambda. 
2.	Write Lambda requests the shards in which the category resides from the Meta API Gateway 
3.	Meta API Gateway receives the request and routes to the Find Lambda. 
4.	Find Lambda queries from the Meta Elasticache. If a category record was found, the shards URLs are fetched. Otherwise, one is created by using the next n to n + k shards URLs (wraparound accounted for) where n is a global round robin counter and k is the shard level. In either case the shard URLs are returned
5.	Query Lambda asynchronously reads data in the category from each shard, and sends each piece of the full data to the function’s API specified
6.	The function’s API processes the piece of data
7.	Query Lambda asynchronously receives the result of each function Lambda’s result, and combines them into one list
8.	Query Lambda returns the computed result


## Cloud and/or Services used
•	Lambda – for scalable compute
•	Elasticache Redis – for scalable storage
•	Cloudwatch – for debugging
•	EC2 – for ssh’ing into Elasticache Redis instances
•	VPC – for securing snekboop and controlling network access

## Lessons learnt
Snekboop was a failure but also a good learning experience. 
•	Network access is the root of 90% of timed out errors
•	We should've tried doing something to group services close by
•	Network latency is gargantuan – this is why snekboop is so slow
•	Cloudwatch access is essential for debugging
•	In most cases hiding AWS backend services (Lambda, EC2, etc) behind AWS Gateway is good for abstraction and decoupling purposes.
•	Some algorithmic analysis to determine what type of algorithms and snekboop specs illustrate the effectiveness of snekboop
•	Constant team communication is important

## Individual contributions (if worked in team)
Vincent Li – backend
•	Designed and wrote the service code
Chris Cale – devops 
•	Wrote the deployment scripts and designed the client library

