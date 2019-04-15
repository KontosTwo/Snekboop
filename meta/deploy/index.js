exports.handler = async (event) => {
    // Dependencies
    var redisURL = process.env.REDIS_URL;
    const redis = require("redis");
    const client = redis.createClient({"url" : redisURL});
    const asyncRedis = require("async-redis");
    const asyncClient = asyncRedis.decorate(client)
    // Parsing request
    var sockets = event.sockets;
    var shardLevel = event.shardLevel;

    if(shardLevel > sockets.length){
        const response = {
            statusCode: 400,
            body: JSON.stringify({ message: "shardLevel cannot be more than the number of shards"})
        };
        
        return response;
    }
    // initializing metadata
    var shardLevelPromise = asyncClient.set("shardLevel",shardLevel);
    var numShardsPromise = asyncClient.set("numShards", sockets.length);
    var socketsPromises = [];
    for(var i = 0; i < sockets.length; i ++){
        socketsPromises.push(asyncClient.hmset("shard",i,JSON.stringify(sockets[i])));
    }
    for(var i = 0; i < sockets.length; i ++){
        await socketsPromises[i];
    }
    await shardLevelPromise;
    await numShardsPromise;

    const response = {
        statusCode: 200,
        body: JSON.stringify({ message: sockets})
    };
    
    return response;
}