const updateTime = updateTime();
{
  fetch("/get-current-time/")
    .then((res) => res.text())
    .then((data) => {
      document.getElementById("current-time").innerHTML = data;
    });
}
setInterval(updateTime, 1000);
