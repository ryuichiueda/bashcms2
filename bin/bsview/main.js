window.onload = function () {

    $('body').bsgdprcookies({
      id: 'bs-gdpr-cookies-modal',
      class: '',
      title: 'Cookies & Privacy Policy',
      backdrop: 'static',
      message: 'このサイトでは広告の設定やアクセス解析（Google AdSense, Google Analytics）のために（という理由もありますがbashで書かれた本ページの限界を追求するために）Cookieを使用しています。もし同意いただけない場合はブラウザでクッキーを無効にして閲覧するか、ブラウザのxボタンでページを閉じてください。<br />This site uses cookies for advertising, access analysis, and experiments for this bash based web site. If you cannot accept our use of cookies, please disable cookies on your browser, or please close this page with x button on the tab or window.',
    
      // shows scrollbar
      //message<a href="https://www.jqueryscript.net/tags.php?/Scroll/">Scroll</a>Bar: false,
    
      // max height
      messageMaxHeightPercent: 25,
    
      // auto displays the modal after 1.5 seconds
      delay: 1500,
    
      // 30 days
      expireDays: 10,
    
      // options for read more link
      moreLinkActive: false,
      //moreLinkLabel: 'More informations..',
      //moreLinkNewTab: true,
      //moreLink: 'privacy-policy.php',
    
      // text for accept button
      acceptButtonLabel: 'Accept'
    
    });

    tagcloud();
    lastArticles(10); 
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
