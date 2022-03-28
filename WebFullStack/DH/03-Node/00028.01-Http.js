/*
methods Hyper text transfer protocol:

get -> request data (request go by url)
post -> send data (request go by body, more security)
put -> send data, replace all informations from some resource
path -> send data, modify information (partially) of a resource
delete - > delete a resource


codes beginning with:
1__ -> informe 
2__ -> Success
3__ -> redirecting
4__ -> client error
5__ -> Server error

200 -> ok
307 -> temporary redirect
403 -> forbiden
404 -> not found
500 -> internal server error

*/
/*
//create this just to access http://localhost and see terminal
const http = require('http'); //load http module in a const

http.createServer((req, res)=>{
    console.log("Server up")
}).listen(3000, "localhost");
*/

/*
//create to see an answer in paget (Just one route)
const http = require('http');
http.createServer((req, res)=>{
    res.writeHead(200, {"Content-Type":"text/plain"})
    res.end("My first server!")
}).listen(3000, "localhost")


*/

//more than one route
const http = require('http');
http.createServer((req, res)=>{
    res.writeHead(200, {"Content-Type":"text/plain"});

    switch(req.url){
        case "/":
            res.end("You are in home page!");
            break;
        case "/contact":
            res.end("You are in contact page");
            break;
        default:
            res.end("Page not found");
    }
}).listen(3000, "localhost")