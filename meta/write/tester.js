const lambdaLocal = require('lambda-local');
 
var jsonPayload = {
    'key': 1,
    'another_key': "Some text"
}
 
lambdaLocal.execute({
    event: jsonPayload,
    lambdaPath: path.join(__dirname, './handler.js'),
    profilePath: '~/.aws/credentials',
    profileName: 'default',
    timeoutMs: 3000,
    callback: function(err, data) {
        if (err) {
            console.log(err);
        } else {
            console.log(data);
        }
    },
    clientContext: JSON.stringify({clientId: 'xxxx'})
});