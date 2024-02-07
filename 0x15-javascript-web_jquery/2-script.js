const $header_val = $('header');
const $divRedHeader = $('div#red_header');

$divRedHeader.on('click', function () {
	  $header_val.css('color', '#FF0000');
});
