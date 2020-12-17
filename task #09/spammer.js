var message = "Hi"; //the message that i wanna spam
var interval = 1  ; //after how many seconds it should send the messages
var count = 10 ; //the number of times i wanna send the messages
var notifyInterval = 5 ; //notify 
var i = 0 ;
var timer = setInterval(function(){
	document.getElementsByClassName('composer_rich_textarea')[0].innerHTML = message;
	$('.im_submit').trigger('mousedown');	
	i++;
	if(i==count)
	clearInterval(timer);
	if( i % notifyInterval == 0)
	console.log(i + ' MESSAGES SENT');
} , interval * 1000 ) ;
    
