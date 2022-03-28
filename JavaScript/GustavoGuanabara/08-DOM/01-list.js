// ============ using getElement ============
window.document.getElementsByTagName('p')[0]; //catch the content of the first paragraph

document.getElementById('msg'); //cath the content from the element identified by msg

window.document.getElementById('msg').style.background = 'green'; //Change to green the background from the element identified by msg

var aa = document.getElementById('msg');
aa.innerText = 'New content'; //replace content from element identified by msg

//============ using query ============ 
var aa = document.querySelector('div#msg')//select the div that has id = msg
aa.style.color = 'blue'

var aa = document.querySelector('div.msg')//select the div that has class = msg


