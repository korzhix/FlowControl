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
	$(".header-link").removeClass('header-link-active');
	$( this ).addClass( "header-link-active", 1000, "ease-in" );

	if (this.parentNode.style.backgroundColor == "black"){
		$(this.parentNode).css("background-color", "unset");
	}else{
		$(this.parentNode).css("background-color", "black");
	};

});

const nextPage = (event) => {
	if (event.target.classList[0] == "far" || event.target.classList[0] == "header-link"){
		if (event.target.classList[0] == "far") {
			localStorage['menuId'] = event.target.parentNode.id;
		}else {
			localStorage['menuId'] = event.target.id;
		};
		
	};
};
console.log(localStorage['menuId']);
const active = document.getElementById(localStorage['menuId']);
$(".header-link").removeClass('header-link-active');
$( '#' + localStorage['menuId'] ).addClass( "header-link-active", 1000, "ease-in" );

localStorage['menuId'] = '2';
console.log(active);
document.addEventListener('click', nextPage);

