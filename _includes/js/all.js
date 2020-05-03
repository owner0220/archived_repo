

window.onscroll = function() {scrollFunction()};


var lastScrollTop = 0;
var delta = 5;
var navbarHeight = $(".cnavbar").outerHeight();
function scrollFunction() {
  var st = $(this).scrollTop();
  if (Math.abs(lastScrollTop - st) <= delta){
    return;
  }
  // If current position > last position AND scrolled past navbar...
  if (st > lastScrollTop && st > navbarHeight){
    // Scroll Down
    // 스크롤 내릴때 사라져야 한다.
    $(".cnavbar").removeClass("blue");
    $(".cnavbar").removeClass("fixed-top");
    
  } else {
    // Scroll Up
    // If did not scroll past the document (possible on mac)...
    if(st + $(window).height() < $(document).height()) { 
      //스크롤 올릴때 나와야 한다.
      $(".cnavbar").addClass("blue"); 
      $(".cnavbar").addClass("fixed-top"); 
    }
  }
  lastScrollTop = st;  
  // 스크롤 내릴때 blue가 삭제된다. blue는 기본적으로 가지고 있는데 blue기능에는 sticky와 함께 shadow가 있으면된다.
  

}



