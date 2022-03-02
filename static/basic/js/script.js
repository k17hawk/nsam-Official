$(document).ready(function(){
  $(".menu-icon").on("click", function(){
    $(".showhas").toggleClass("showing");
  });
});

window.onscroll = function() {
  myFunction()
};



function myFunction() {
    var scroll=document.getElementById("ws-scroll");
    var imge= document.getElementById("imagg")
  if (document.body.scrollTop > 90 ||
            document.documentElement.scrollTop > 90)
        {

             imge.style.height = "95px";
                  imge.style.width= "95px";
        }
        else {

            imge.style.height = "117px";
                  imge.style.width= "120px";

     }
}
