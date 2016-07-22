$(document).ready(function() {
    $(window).scroll(function() {
        if($(window).scrollTop() >= 40) {
            $('.navbar').addClass('navbar-default-fixed');
        }
        else {
            $('.navbar').removeClass('navbar-default-fixed');
        }
    });
});