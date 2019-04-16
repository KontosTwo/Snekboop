exports.handler = async (event) => {
    // Dependencies
    var redisURL = process.env.REDIS_URL;
    const redis = require("redis");
    const client = redis.createClient({"url" : redisURL});
    const asyncRedis = require("async-redis");
    const asyncClient = asyncRedis.decorate(client)

    // Parsing request
    var name = event.name;
    // Get data from Redis
    var shardLevelPromise = asyncClient.get("shardLevel")
    var numShardsPromise = asyncClient.get("numShards")
    var nameExists = await asyncClient.hexists("name", name);
    var shardLevel = await shardLevelPromise;
    if(!nameExists){
        // Initialize metadata for the name
        var incrShard = await asyncClient.incr("globalShardCounter");
        if(incrShard >= shardLevel){
            incrShard = 0;
            await asyncClient.set("globalShardCounter", 0);
        }
        var setNamePromise = asyncClient.hset("name", name,0);
        var setCounterPromise = asyncClient.hmset("shardCounter",name, incrShard);
        await setNamePromise;
        await setCounterPromise; 
    }
    // Find the shards to write to
    var shardCounter = await asyncClient.hmget("shardCounter", name);
    var writeShardsPromise = [];
    var writeShards = [];
    var numShards = await numShardsPromise;
    for(var i = shardCounter; i < shardCounter + shardLevel; i ++){
        var shardNumber = i % numShards;
        writeShardsPromise.push(asyncClient.hmget("shard",shardNumber));
    }
    for(var i = 0; i < shardLevel; i ++){
        writeShards.push(JSON.parse(await writeShardsPromise[i]));
    }
    const response = {
        statusCode: 200,
        body: JSON.stringify({ message: writeShards})
    };
    
    return response;
}