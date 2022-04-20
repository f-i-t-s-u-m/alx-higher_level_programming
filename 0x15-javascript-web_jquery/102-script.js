$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
     const code = $('INPUT#language_code').val()
     $.get('https://fourtonfish.com/hellosalut/?lang='+code, function (n) {
 	$('DIV#hello').text(n.hello)
     })
  })
})
