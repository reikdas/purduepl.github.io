document.addEventListener("DOMContentLoaded", function () {
	var toggleImg = document.getElementById("table-collapse-img");
	if (toggleImg) {
		toggleImg.addEventListener("click", function () {
			var table = document.getElementById("seminar-schedule-old");
			if (table.style.display === "none") {
				table.style.display = "table";
				toggleImg.src = "assets/minimize.webp";
			} else {
				table.style.display = "none";
				toggleImg.src = "assets/maximize.webp";
			}
		});
	}
});
