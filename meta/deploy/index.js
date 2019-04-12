exports.handler = async (event) => {
    // Dependencies
    var redis_url = process.env.REDIS_URL;
    const redis = require("redis");
    const client = redis.createClient({"url" : redis_url});
    const asyncRedis = require("async-redis");
    const async_client = asyncRedis.decorate(client)
    // Parsing request
    var sockets = event.sockets;

    // initializing metadata
    var sockets_promises = [];
    for(var i = 0; i < sockets.length; i ++){
        sockets_promises.push(async_client.hmset(i,"shard",sockets[i]));
    }
    for(var i = 0; i < sockets.length; i ++){
        await sockets_promises[i];
    }

    const response = {
        statusCode: 200,
        body: JSON.stringify({ message: sockets})
    };
    
    return response;
}