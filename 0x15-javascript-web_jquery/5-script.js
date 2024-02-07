const $list_val= $('ul.my_list');
const $val_add = $('div#add_item');

$val_add.on('click', () => {
	  $list_val.append('<li>Item</li>');
});
