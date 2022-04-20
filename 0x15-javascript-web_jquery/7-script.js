$(document).ready(function () {
 $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (n) {
   $('DIV#character').text(n['name'])
 })
})
