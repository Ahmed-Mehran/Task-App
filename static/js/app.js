

message_timeout = document.getElementById("message-timer");

setTimeout(function(){

    message_timeout.style.display = 'none'
}, 5000)

// message_timeout.style.display = 'none' is effectively hiding the element with the id "message-timer" after a delay of 5000 milliseconds (5 seconds) 
// as specified by the setTimeout function.