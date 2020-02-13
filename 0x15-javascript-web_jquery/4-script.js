$('DIV#toggle_header')[0].addEventListener('click', function () {
  if ($('header')[0].className === 'green') $('header')[0].className = 'red';
  else $('header')[0].className = 'green';
});
