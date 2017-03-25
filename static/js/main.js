$(function() {
  $("#docs").hover(function() {
    $(this).addClass("w--open"),
    $("#docs-nav").addClass("w--open");
  }, function() {
    $(this).removeClass("w--open"),
    $("#docs-nav").removeClass("w--open");
  });
});
$(function() {
  $("#docs-nav").hover(function() {
    $(this).addClass("w--open"),
    $("#docs").addClass("w--open");
  }, function() {
    $(this).removeClass("w--open"),
    $("#docs").removeClass("w--open");
  });
});
$(function() {
  $("#community").hover(function() {
    $(this).addClass("w--open"),
    $("#community-nav").addClass("w--open");
  }, function() {
    $(this).removeClass("w--open"),
    $("#community-nav").removeClass("w--open");
  });
});
$(function() {
  $("#community-nav").hover(function() {
    $(this).addClass("w--open"),
    $("#community").addClass("w--open");
  }, function() {
    $(this).removeClass("w--open"),
    $("#community").removeClass("w--open");
  });
});

function FriendsListToggle() {
  document.getElementById("friends-list").classList.toggle("w-hidden");
}

function AddFriendOpen() {
  document.getElementById("add-friend-popup").classList.toggle("w-hidden");
}

function FriendsListFilter() {
  var input, filter, ul, li, p, i;
  input = document.getElementById("filter");
  filter = input.value.toUpperCase();
  ul = document.getElementById("active-friend-list");
  li = ul.getElementsByTagName('li');

  for (i = 0; i < li.length; i++) {
    p = li[i].getElementsById("name")[0];
    if (p.innerHTML.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}
