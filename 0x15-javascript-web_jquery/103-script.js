document.addEventListener('DOMContentLoaded', function () {
  function greet () {
    const lang = $('INPUT#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/?lang=' + lang, function (data, stat) {
      $('DIV#hello').text(data.hello);
    });
  }
  $('INPUT#btn_translate')[0].addEventListener('click', greet);
  $('INPUT#language_code')[0].addEventListener('keypress', function (e) {
    if (e.key === 'Enter') greet();
  });
});
