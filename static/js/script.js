// show/hide accordion menu
let accordion = document.getElementsByClassName("accordion");
for (let i = 0; i < accordion.length; i++) {
  accordion[i].addEventListener("click", function () {
    this.classList.toggle("active");
    let subMenu = this.nextElementSibling;
    if (subMenu.style.maxHeight) {
      subMenu.style.maxHeight = null;
    } else {
      subMenu.style.maxHeight = subMenu.scrollHeight + "px";
    }
  });
}

//for displaying all other 21 applicants
// let allApplicants = document.getElementsByClassName("hidden-layout")[0];
// let showMore = document.getElementById("show-more-card");
// let cardOverlay = document.getElementsByClassName("card-overlay")[0];

// showMore.addEventListener("click", function () {
//   $("#show-more-card .replace-img").css("display", "block");
//   allApplicants.className = "flex";
//   cardOverlay.style.display = "none";
// });

// for displaying popup
// let popupOpener = document.getElementsByClassName("popup-opener")[0];
// let secondPopupOpener = document.getElementsByClassName("popup-opener")[1];
// let popupOpenerPage = document.getElementById("popup-opener-page");
// let smallPopupOpener = document.getElementById("small-popup-opener");
// let popupCloser = document.getElementById("popup-closer");
// let popup = document.getElementsByClassName("contact-overlay")[0];

// popupOpener.addEventListener("click", function () {
//   popup.setAttribute("style", "display: block;");
// });
// secondPopupOpener.addEventListener("click", function () {
//   popup.setAttribute("style", "display: block;");
// });
// popupOpenerPage.addEventListener("click", function () {
//   popup.setAttribute("style", "display: block;");
// });
// smallPopupOpener.addEventListener("click", function () {
//   popup.setAttribute("style", "display: block;");
// });
// popupCloser.addEventListener("click", function () {
//   popup.setAttribute("style", "display: none");
// });


$(document).ready(function (){
  $("#watch-video").click(function(){
    $(".video-overlay").css("display", "block");
  });
  $(".video-overlay-header i").click(function(){
    $(".video-overlay").css("display", "none");
  });

  $(document).scroll(function () {
    //for cards' image ratio
    let cardImageWidth = $(".img-container").width();
    $(".img-container").css("height", cardImageWidth);

    var $nav = $("nav");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
  });

  //highlight each nav item when clicked
  $('nav a').on('click', function() {
    $('nav a').removeClass('active-nav');
    $(this).addClass('active-nav');
  });

  //show navbar for small nav
  $(".show-menu").click(function () {
    $(".small-nav-menu").css("left", "0");
  });

  $("#close-menu").click(function () {
    $(".small-nav-menu").css("left", "-100%");
  });

  $(".small-nav-menu a").click(function(){
    $(".small-nav-menu").css("left", "-100%");
  });

  $(".small-nav-menu .apply-button").click(function(){
    $(".small-nav-menu").css("left", "-100%");
  });

  //display each term on popup
  $(".register-term-button").click(function () {
    $(".register-term-overlay").css("display", "block");
  });
  $(".apply-term-button").click(function () {
    $(".apply-term-overlay").css("display", "block");
  });
  $(".result-term-button").click(function () {
    $(".result-term-overlay").css("display", "block");
  });
  $(".term-popup-closer").click(function () {
    $(".register-term-overlay").css("display", "none");
    $(".apply-term-overlay").css("display", "none");
    $(".result-term-overlay").css("display", "none");
  });
});