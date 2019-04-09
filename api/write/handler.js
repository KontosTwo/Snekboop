exports.handler = async (event, context) => {

    meta_host = process.env.SNEKBOOP_META_HOST




    const response = {
        statusCode: 200,
        body: JSON.stringify({ message: 'hello world' })
    }
    
    return response
}