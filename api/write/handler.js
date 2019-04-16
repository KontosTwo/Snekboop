exports.handler = async (event) => {
    // Dependencies
    var metaFindURL = process.env.META_FIND_URL;
    const redis = require("redis");
    const asyncRedis = require("async-redis");
    const fetch = require("node-fetch");

    // parsing request
    var name = event.name;
    var data = event.data;
    var dataLength = data.length

    var response = await fetch(metaFindURL,{
        method: 'post',
        body:    JSON.stringify({
            event: {
                name: name
            }
        }),
        headers: { 'Content-Type': 'application/json' }
    })

    var sockets = response.message;
    var socketsLength = sockets.length;
    var writePromises = [];
    var chunkLength = Math.round(dataLength / socketsLength);
    for(var i = 0; i < socketsLength; i  +=chunkLength){
        var chunk = data.slice(i,i + chunk);
        var socket = sockets[i];
        var shardClient = createShardClient(redis, asyncRedis,socket)
        var writePromise = shardClient.lpush(name,chunk);
        writePromises.push(writePromise);
    }
    for(var i = 0; i < socketsLength; i ++){
        await writePromises[i];
    }


    const response = {
        statusCode: 201,
        body: JSON.stringify({ message: "Successful write"})
    };
    
    return response;
}

function createShardClient(redis, asyncRedis, url){
    const client = redis.createClient({"url" : url});
    const asyncClient = asyncRedis.decorate(client)
    return asyncClient;
}