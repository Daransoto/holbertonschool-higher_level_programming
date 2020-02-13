$.get('https://swapi.co/api/people/5/?format=json', function (data, stat) {
  $('DIV#character').text(data.name);
});
