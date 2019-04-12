exports.handler = async (event) => {
    // Dependencies
    var meta_redis_host = process.env.SNEKBOOP_META_REDIS_HOST;
    var meta_redis_port = process.env.SNEKBOOP_META_REDIS_PORT;
    var shard_level = process.env.SHARD_LEVEL;
    var num_shards = process.env.NUM_SHARDS;
    var redis = require('async-redis');
    var client = redis.createClient(meta_redis_port, meta_redis_host);

    // Parsing request
    var name = event.name;

    // Get data from Redis
    var name_exists = await client.hexists("name", name);
    if(!name_exists){
        // Initialize metadata for the name
        var setNamePromise = client.hset("name", name);
        var setCounterPromise = client.hmset("shard_counter", name, 0);
        await setNamePromise;
        await setCounterPromise;
    }
    // Find the shards to write to
    var shard_counter = await client.hmget("shard_counter", name);
    var incr_shard_counter_promise = client.hincrby(name, "shard_counter", 1)
    var write_shards_promises = [];
    var write_shards = [];
    for(var i = 0; i < shard_level; i ++){
        shard_number = (shard_counter + i) % num_shards;
        write_shards_promises.push(client.hmget("shard",shard_number));
    }
    for(var i = 0; i < shard_level; i ++){
        write_shards.push(await write_shards_promises[i]);
    }
    await incr_shard_counter_promise;
    
    const response = {
        statusCode: 200,
        body: JSON.stringify({ message: write_shards})
    };
    
    return response;
}