console.log("File script.js berhasil terhubung!");

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
      }

      if (data.blue) {
        document.getElementById("blue").style.backgroundColor = "blue";
        document.getElementById("blue").style.color = "white";
      } else {
        document.getElementById("blue").style.backgroundColor = "white";
        document.getElementById("blue").style.color = "black";
      }
    })
    .catch((err) => console.error("Gagal ambil status:", err));
}

setInterval(updateStatus, 0);
