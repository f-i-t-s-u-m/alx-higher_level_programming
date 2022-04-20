$(document).ready(function () {
 $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (n) {
   for (x in n.results) {
   	$('UL#list_movies').prepend("<li>" + n.results[x].title  + "</li>")
   }
 })
})
