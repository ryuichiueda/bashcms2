window.onload = function () {
    lastArticles(10); 
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
