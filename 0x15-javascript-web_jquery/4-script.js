const $header_val = $('header');
const $div_rea_header = $('DIV#toggle_header');

$div_rea_header.on('click', () => {
  const currentClass = $header_val.attr('class');

  if (currentClass === 'green') {
    $header_val.toggleClass(`${currentClass} red`);
  }

  if (currentClass === 'red') {
    $headerElem.toggleClass(`${currentClass} green`);
  }
});
