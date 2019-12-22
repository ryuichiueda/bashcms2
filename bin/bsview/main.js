window.onload = function () {
    if(document.cookie.indexOf("cookieconfirm=") < 0){
        window['ga-disable-UA-39565206-5'] = true;
        document.getElementById("cookiemention").style.visibility = "visible";
    }else if(document.cookie.indexOf("cookieconfirm=ng") > 0){
        window['ga-disable-UA-39565206-5'] = true;
    }

    var toc = document.getElementById("toc");
    if(toc.getElementsByTagName("li").length < 2)
	toc.innerHTML = "";
    else
        toc.getElementsByTagName("li")[0].getElementsByTagName("a")[0].innerHTML = "目次";

    tagcloud();
    lastArticles(10); 
    lastRead(10); 
    rankArticles(10); 
    linkKeywords();
//    fullSearch("");
}                     
                      
function lastArticles(num){
    var httpReq = new XMLHttpRequest();
    httpReq.onreadystatechange = function(){
        if(httpReq.readyState != 4 || httpReq.status != 200)
            return;                 

        document.getElementById("last-articles").innerHTML = httpReq.responseText;
    }                               
    var url = "/last_articles.cgi?num=" + num;
    httpReq.open("GET",url,true);   
    httpReq.send(null);             
}

function lastRead(num){
    var httpReq = new XMLHttpRequest();
    httpReq.onreadystatechange = function(){
        if(httpReq.readyState != 4 || httpReq.status != 200)
            return;                 

        document.getElementById("last-read").innerHTML = httpReq.responseText;
    }                               
    var url = "/last_read.cgi?num=" + num;
    httpReq.open("GET",url,true);   
    httpReq.send(null);             
}

function linkKeywords(){
    var httpReq = new XMLHttpRequest();
    httpReq.onreadystatechange = function(){
        if(httpReq.readyState != 4 || httpReq.status != 200)
            return;                 

        document.getElementById("keywords").innerHTML = httpReq.responseText;
    }                               
    var word = document.getElementById("keywords").innerHTML;
    var url = "/link_keywords.cgi?keywords=" + encodeURIComponent(word);
    httpReq.open("GET",url,true);   
    httpReq.send(null);             
}

/*
function fullSearch(word){
    var httpReq = new XMLHttpRequest();
    httpReq.onreadystatechange = function(){
        if(httpReq.readyState != 4 || httpReq.status != 200)
            return;

        document.getElementById("full-search").innerHTML = httpReq.responseText;
        document.body.style.cursor = "default";
    }
    var url = "/full_search.cgi?word=" + encodeURIComponent(word);
    httpReq.open("GET",url,true);
    httpReq.send(null);
    document.body.style.cursor = "wait";
}
*/

function fullSearch(){
    var word = document.getElementById("full-search-box").value;
    if(word == "")
        return;
    var httpReq = new XMLHttpRequest();
    httpReq.onreadystatechange = function(){
        if(httpReq.readyState != 4 || httpReq.status != 200)
            return;

        document.getElementById("article-body").innerHTML = httpReq.responseText;
        document.body.style.cursor = "default";
    }
    var url = "/bsview/full_search.cgi?word=" + encodeURIComponent(word);
    httpReq.open("GET",url,true);
    httpReq.send(null);
    document.body.style.cursor = "wait";
}

function rankArticles(num){
    var httpReq = new XMLHttpRequest();
    httpReq.onreadystatechange = function(){
        if(httpReq.readyState != 4 || httpReq.status != 200)
            return;                 

        document.getElementById("rank-articles").innerHTML = httpReq.responseText;
    }                               
    var url = "/rank_articles.cgi?num=" + num;
    httpReq.open("GET",url,true);   
    httpReq.send(null);             
}

function tagcloud(){
    var httpReq = new XMLHttpRequest();
    httpReq.onreadystatechange = function(){
        if(httpReq.readyState != 4 || httpReq.status != 200)
            return;

        document.getElementById("tag-cloud").innerHTML = httpReq.responseText;
    }
    var url = "/tagcloud.cgi"
    httpReq.open("GET",url,true);
    httpReq.send(null);
}

document.getElementById("cookieok").onclick = function() {
    document.getElementById("cookiemention").hidden = true;
    var expire = new Date();
    expire.setMonth(expire.getMonth() + 3); 
    document.cookie = "cookieconfirm=ok; expires=" + expire.toUTCString();

    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments)};
    gtag('js', new Date());
  
    gtag('config', 'UA-39565206-5');
}

document.getElementById("cookieng").onclick = function() {
    document.getElementById("cookiemention").hidden = true;
    var expire = new Date();
    expire.setMonth(expire.getMonth() + 3); 
    document.cookie = "cookieconfirm=ng; expires=" + expire.toUTCString();
}


setInterval(lastRead, 3000, 10);

