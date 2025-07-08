console.log("test");

const toggle = document.getElementById("darkModeToggle");


toggle.addEventListener("change", function () {
  document.body.classList.toggle("dark-mode", this.checked);

  localStorage.setItem("theme", this.checked ? "dark" : "light");
});

window.addEventListener("DOMContentLoaded", () => {
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme === "dark") {
    document.body.classList.add("dark-mode");
    toggle.checked = true;
  }
});

function updateStatus() {
  fetch("/status")
    .then((res) => res.json())
    .then((data) => {
        console.log(data);
      if (data.red) {
        document.getElementById("red").style.backgroundColor = "red";
        document.getElementById("red").style.color = "white";
        document.getElementById("count-red").innerHTML = data.countRed;
      } else {
        document.getElementById("red").style.backgroundColor = "white";
        document.getElementById("red").style.color = "black";
        document.getElementById("count-red").innerHTML = data.countRed;
      }

      if (data.blue) {
        document.getElementById("blue").style.backgroundColor = "blue";
        document.getElementById("blue").style.color = "white";
        document.getElementById("count-blue").innerHTML = data.countBlue;
      } else {
        document.getElementById("blue").style.backgroundColor = "white";
        document.getElementById("blue").style.color = "black";
        document.getElementById("count-blue").innerHTML = data.countBlue;
      }

      if (data.green) {
        document.getElementById("green").style.backgroundColor = "green";
        document.getElementById("green").style.color = "white";
        document.getElementById("count-green").innerHTML = data.countGreen;
      } else {
        document.getElementById("green").style.backgroundColor = "white";
        document.getElementById("green").style.color = "black";
        document.getElementById("count-green").innerHTML = data.countGreen;
      }

      
    })
    .catch((err) => console.error("Gagal ambil status", err));
}

setInterval(updateStatus, 0);
