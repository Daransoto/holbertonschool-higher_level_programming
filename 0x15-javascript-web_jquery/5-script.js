$('DIV#add_item')[0].addEventListener('click', function () {
  const elem = document.createElement('li');
  elem.innerText = 'Item';
  $('UL.my_list')[0].appendChild(elem);
});
