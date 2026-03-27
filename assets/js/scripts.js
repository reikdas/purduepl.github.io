document.addEventListener("DOMContentLoaded", function () {
	var toggleBtn = document.getElementById("table-collapse-btn");
	var toggleImg = document.getElementById("table-collapse-img");
	if (toggleBtn && toggleImg) {
		toggleBtn.addEventListener("click", function () {
			var table = document.getElementById("seminar-schedule-old");
			if (table.style.display === "none") {
				table.style.display = "table";
				toggleImg.src = "assets/minimize.webp";
				toggleBtn.setAttribute("aria-label", "Hide older seminars");
				toggleImg.alt = "Hide older seminars";
			} else {
				table.style.display = "none";
				toggleImg.src = "assets/maximize.webp";
				toggleBtn.setAttribute("aria-label", "Show older seminars");
				toggleImg.alt = "Show older seminars";
			}
		});
	}
});
