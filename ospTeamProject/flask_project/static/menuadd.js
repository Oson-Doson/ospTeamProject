var i=1

document.getElementById("btnadd").onclick = function(){
    var wrap=document.getElementById("form-wrap");
    var form=document.getElementsByClassName('mform');
    wrap.appendChild(form);
}