$(document).ready(function () {
  var trigger = $('.hamburger'),
      overlay = $('.overlay'),
      isClosed = false;

  $('[data-toggle="offcanvas"]').click(function () {
    console.log("in data-toggle function");
        $('#wrapper').toggleClass('toggled');
        if (isClosed == true) {
          overlay.hide();
          trigger.removeClass('is-open');
          trigger.addClass('is-closed');
          isClosed = false;
        } else {
          overlay.show();
          trigger.removeClass('is-closed');
          trigger.addClass('is-open');
          isClosed = true;
        }
  });
  // Instantiate the Bootstrap carousel
  $('.multi-item-carousel').carousel({
  interval: false
  //    wrap: false
  });

  $('.multi-item-carousel').carousel({
    interval: false
  });

  $('.multi-item-carousel .item').each(function(){
    var next = $(this).next();
    if (!next.length) {
      next = $(this).siblings(':first');
    }
    next.children(':first-child').clone().appendTo($(this));

    if (next.next().length>0) {
      next.next().children(':first-child').clone().appendTo($(this));
    } else {
      $(this).siblings(':first').children(':first-child').clone().appendTo($(this));
    }
  });
  function validate() {
    var n1 = document.getElementById("num1");
    var n2 = document.getElementById("num2");
    if(n1.value != "" && n2.value != "") {
      if(n1.value == n2.value) {
        return true;
      }
    }
    alert("The values should be equal and not blank");
    return false;
  }



});
