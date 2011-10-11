var app = require('express').createServer();

var fibonacci = function(n) {
  if (n < 2) {
    return 1;    
  }
  return fibonacci(n-1) + fibonacci(n-2);
}

app.get('/fibo/:n', function(req, res) {
    res.send('' + fibonacci(req.params.n));
});

app.listen(3000);
