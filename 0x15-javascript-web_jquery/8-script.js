$.get('https://swapi.co/api/films/?format=json', function (data, stat) {
  for (const i of data.results) $('UL#list_movies').append('<li>' + i.title + '</li>');
});
