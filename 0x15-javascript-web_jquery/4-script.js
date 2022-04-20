$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
     $('header').toggleClass(function (index, current) {
	  $('header').removeClass(current)
	  if (current == 'green') {
	     return 'red'
	  }
	  return 'green'
     })
  })
})
