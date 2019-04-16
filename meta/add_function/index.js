exports.handler = async (event) => {
    // Dependencies
    var redisURL = process.env.REDIS_URL;
    const redis = require("redis");
    const client = redis.createClient({"url" : redisURL});
    const asyncRedis = require("async-redis");
    const asyncClient = asyncRedis.decorate(client)


    // Parsing request
    var funcName = event.funcName;
    var arn = event.arn;

    // Error check
    var nameExists = await asyncClient.hexists("functions",funcName);
    if(nameExists){
        const response = {
            statusCode: 400,
            body: JSON.stringify({ message: "The name for the function already exists"})
        };
        
        return response;
    }

    // adding metadata
    await asyncClient.hmset("functions",funcName,arn);


    const response = {
        statusCode: 201,
        body: JSON.stringify({ message: "Function with name " + funcName + " created with ARN " + arn})
    };
    
    return response;
}