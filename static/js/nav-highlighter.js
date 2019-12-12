$(document).ready(function(){
    $(document).on("scroll", function(){
        let scroll = $(window).scrollTop();
        let navHeight = $("nav").outerHeight() + 5;
        let headerOffsetTop = $("#about-section").offset().top;
        let aboutOffsetTop = $("#terms-section").offset().top;
        let termsOffsetTop = $("#attendants-section").offset().top;
        let attendantsOffsetTop = $("#most-asked-section").offset().top;
        let mostAskedOffsetTop = $("#contact-section").offset().top;
        let activeNav = $('a[data-scroll="header"]');

        if(scroll > headerOffsetTop - navHeight){
            activeNav = $('a[data-scroll="about"]');
        }

        if(scroll > aboutOffsetTop - navHeight){
            activeNav = $('a[data-scroll="terms"]');
        }

        if(scroll > termsOffsetTop - navHeight){
            activeNav = $('a[data-scroll="attendants"]');
        }

        if(scroll > attendantsOffsetTop - navHeight){
            activeNav = $('a[data-scroll="most-asked"]');
        }

        if(scroll > mostAskedOffsetTop - navHeight){
            activeNav = $('a[data-scroll="contact"]');
        }
        activeNav.addClass("active-nav");
        $("nav a").not(activeNav).removeClass("active-nav");
    });
});