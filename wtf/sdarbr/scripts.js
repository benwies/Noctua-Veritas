document.getElementById("link").addEventListener("click", function (e) {
    e.preventDefault();
    history.replaceState({}, "", "second.html");
    window.location.href = "second.html";
  });