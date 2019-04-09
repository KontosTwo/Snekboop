exports.handler = async (event, context) => {
    // Dependencies
    meta_redis_host = process.env.SNEKBOOP_META_REDIS_HOST;
    meta_redis_port = process.env.SNEKBOOP_META_REDIS_PORT;
    var redis = require('redis');
    var redis_client = redis.createClient(meta_redis_port, meta_redis_host);

    // Parsing request
    var name = event.name
    var data = event.data
    

    const response = {
        statusCode: 200,
        body: JSON.stringify({ message: 'hello world' })
    };
    
    return response;
}