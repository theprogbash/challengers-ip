$(document).ready(function(){
    $(window).on('load', function(){
        $(".modal-overlay").css("display", "block");
        $(".modal-overlay").click(function(){
            $(this).css("display", "none");
        });
    });
});