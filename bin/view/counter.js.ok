function send_href(){
	ws.send(location.href);
}

var ws = new WebSocket('ws://bashcms2.ueda.tech:8080/');
ws.onopen = function() {
	setInterval('send_href()',1000);
};
ws.onclose = function() {
};
ws.onmessage = function(event) {
	document.getElementById("views").innerHTML = event.data;
};

