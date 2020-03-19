$( ".sidebar-item-link" ).click(function() {
	$( this.nextElementSibling ).toggleClass( "submenu-active", 1000, "ease-in");
	$( this ).toggleClass( "sidebar-item-link-active", 1000, "ease-in" );

	if (this.parentNode.style.backgroundColor == "black"){
		$(this.parentNode).css("background-color", "unset");
	}else{
		$(this.parentNode).css("background-color", "black");
	};

});
$('li.sidebar-item').click(function(){
	$('this').css("border-left", "1px solid red");
});

$( ".header-link" ).click(function() {
	$( this.nextElementSibling ).toggleClass( "submenu-active", 1000, "ease-in");
	$( this ).toggleClass( "sidebar-item-link-active", 1000, "ease-in" );

	if (this.parentNode.style.backgroundColor == "black"){
		$(this.parentNode).css("background-color", "unset");
	}else{
		$(this.parentNode).css("background-color", "black");
	};
};