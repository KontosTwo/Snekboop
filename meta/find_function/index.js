exports.handler = async (event) => {
    // Dependencies
    var redisURL = process.env.REDIS_URL;
    const redis = require("redis");
    const client = redis.createClient({"url" : redisURL});
    const asyncRedis = require("async-redis");
    const asyncClient = asyncRedis.decorate(client)

    // Parsing request
    var funcName = event.funcName;

    // Error check
    var nameExists = await asyncClient.hexists("functions",funcName);
    if(!nameExists){
        const response = {
            statusCode: 404,
            body: JSON.stringify({ message: "The name for the function does not exist"})
        };
        
        return response;
    }

    // adding metadata
    var arn = await asyncClient.hmget("functions",funcName);


    const response = {
        statusCode: 200,
        body: JSON.stringify({ message: arn})
    };
    
    return response;
}