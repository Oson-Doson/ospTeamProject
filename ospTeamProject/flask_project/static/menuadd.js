var i=1

document.getElementById("btnadd").onclick = create();

function create(){
    var div=document.createElement('div');

    div.innerHTML=document.getElementById('section').innerHTML;
    var wrap=document.getElementById("form_add");
    wrap.appendChild(div);
}