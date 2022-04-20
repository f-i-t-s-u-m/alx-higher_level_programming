$(document).ready(function () {
  let get_trans =  function () {
     const code = $('INPUT#language_code').val()
     $.get('https://fourtonfish.com/hellosalut/?lang='+code, function (n) {
 	$('DIV#hello').text(n.hello)
     })
  }

  $('INPUT#btn_translate').on('click', get_trans ) 
  $('INPUT#language_code').on('keydown', function (e) {
    if (e.which == 13) {
      get_trans()
    }
  }) 

})
