$('.sign-link').click(function() {  
    $('.sign-link').not(this).removeClass('sign-link-active');
    $(this).toggleClass('sign-link-active');
});

