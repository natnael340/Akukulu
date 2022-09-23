searchInput = $("#search");
searchList = document.getElementsByClassName("search-list")[0];

prodDetail = $("#prod-detail");

$("#earned")[0].innerText = (parseFloat($("#sold")[0].innerText) * parseFloat($("#price")[0].innerText)).toPrecision(3) + "$"

searchInput.keyup(function () {
  $(".search-result").css("display", "block");
  $(".my-loading-dots").css("display", "block");
  if (searchInput.val().length > 2) {
    $.ajax({
      type: "POST",
      url: "/products/",
      data: {
        text: searchInput.val(),
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      },
      dataType: "json",
      success: function (data) {
        console.log(data);
        $(".my-loading-dots").css("display", "none");
        for (i in data.data) {
          console.log(data.data[i]);
          searchList.innerHTML = addLitem(
            data.data[i].id,
            data.data[i].itemName,
            data.data[i].img.replace(/\.media\./g, "\\media\\"),
            data.data[i].price
          );
        }
      },
    });
  } else {
    searchList.innerHTML = "";
  }
});
searchInput.focusout(function () {
  $(".search-result").css("display", "none");
  $(".my-loadin g-dots").css("display", "none");
});
function addLitem(id, name, image, price) {
  var out =
    "<li> <div class='thumbnail col-md-3 col-sm-1 col-xs-1' style='background-color: #ECECEC; border: none;'><img src=" +
    image +
    "></div><a href='/product/" +
    id +
    "'>" +
    name +
    "</a><span>" +
    price +
    "</span></li>";
  return out;
}
function toggleProdDetail(){
  if(prodDetail[0].style.display == "flex")
  prodDetail.css("display", "none")
  else
  prodDetail.css("display", "flex")
}
