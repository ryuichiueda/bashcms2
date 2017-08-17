window.onload = function () {
    lastArticles(10); 
    linkKeywords();
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

function linkKeywords(){
    var httpReq = new XMLHttpRequest();
    httpReq.onreadystatechange = function(){
        if(httpReq.readyState != 4 || httpReq.status != 200)
            return;                 

        document.getElementById("keywords").innerHTML = httpReq.responseText;
    }                               
    var url = "/link_keywords.cgi?keywords=" 
	    + document.getElementById("keywords").innerHTML;
    httpReq.open("GET",url,true);   
    httpReq.send(null);             
}
