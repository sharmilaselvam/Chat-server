var a;
function inter(){
    a=setInterval(autore,1500)
}
function msgupdate(){
    var mesto=document.getElementById("chatbd");
    var mesfrm=document.getElementById("messIn").value;
    mesto.focus();
    document.getElementById("messIn").focus()
    if (!mesfrm=="")
    {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if(this.status!=200 && this.status!=0)
        {
        clearInterval(a)
        }

        if (this.readyState == 4 && this.status == 200) {
            var temp= xhttp.responseText;
            document.getElementById("messIn").value="";
           
            var p=document.createElement("p")
            p.setAttribute("class","bmsg")
            var span1=document.createElement("span")
            var span2=document.createElement("span")
            span1.setAttribute("class","a")
            span2.setAttribute("class","msg")
            var div=document.createElement("div")
            div.appendChild(p)
            div.setAttribute("class","chat")
            p.appendChild(span1)
            p.appendChild(span2)
            span1.innerText="Me"
            span2.innerText=temp
            mesto.appendChild(div)
            document.getElementById("tnu").value=xhttp.getResponseHeader('count');
            document.getElementById("messIn").value="";
        }
    };
    xhttp.open("POST", "./chat", true );
    xhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
    document.getElementById("tnu").value=xhttp.getResponseHeader('count');
    xhttp.send("subm="+"s"+"&mes="+mesfrm+"&count="+document.getElementById("tnu").value);
    }
}

function autore()
{
    
    var mesto=document.getElementById("chatbd");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if(this.status!=200 && this.status!=0)
        {
            clearInterval(a)
        }
        
        if (this.readyState == 4 && this.status == 200) {
            var p= xhttp.responseText;
            if(p!="")
            {    
            mesto.innerHTML=mesto.innerHTML+p
            document.getElementById("tnu").value=xhttp.getResponseHeader('count');
            console.log(xhttp.getResponseHeader('count'));
            }
        }
        
    };
    xhttp.open("POST", "./chat", true );
    xhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
    xhttp.send("subm="+"n"+"&mes="+"u"+"&count="+document.getElementById("tnu").value);
}




