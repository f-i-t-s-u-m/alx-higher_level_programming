$(document).ready(function () {
 $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (n) {
   $('DIV#hello').text(n.hello)
 })
})
