setInterval(colorNavs, 100);
function colorNavs() {
	var nav_1_1 = document.getElementById("nav_1_Historia");
	var nav_1_1_1 = document.getElementById("nav_1_Inicio");
	var nav_1_1_2= document.getElementById("nav_1_MF");
	var nav_1_2 = document.getElementById("nav_1_Missao");
	var nav_1_3 = document.getElementById("nav_1_Visao");
	var nav_1_4 = document.getElementById("nav_1_Valores");
	var nav_2_1 = document.getElementById("navPortifolio_01");
	var nav_2_2 = document.getElementById("navPortifolio_02");
	var nav_2_3 = document.getElementById("navPortifolio_03");

	if(nav_2_1.className.search("active") != -1) {
		nav_2_1.style.color = "#FFFFFF";
		nav_2_1.style.backgroundColor = "#7d007d";
		nav_2_2.style.color = "#000000";
		nav_2_2.style.backgroundColor = "#FFFFFF";
		nav_2_3.style.color = "#000000";
		nav_2_3.style.backgroundColor = "#FFFFFF";
	}
	else if(nav_2_2.className.search("active") != -1) {
		nav_2_2.style.color = "#FFFFFF";
		nav_2_2.style.backgroundColor = "#7d007d";
		nav_2_1.style.color = "#000000";
		nav_2_1.style.backgroundColor = "#FFFFFF";
		nav_2_3.style.color = "#000000";
		nav_2_3.style.backgroundColor = "#FFFFFF";
	}
	else {
		nav_2_3.style.color = "#FFFFFF";
		nav_2_3.style.backgroundColor = "#7d007d";
		nav_2_1.style.color = "#000000";
		nav_2_1.style.backgroundColor = "#FFFFFF";
		nav_2_2.style.color = "#000000";
		nav_2_2.style.backgroundColor = "#FFFFFF";
	}

	if(nav_1_1_1.className.search("active") != -1) {
		nav_1_1.style.color = "#FFFFFF";
		nav_1_1.style.backgroundColor = "#7d007d";
		nav_1_1_1.style.color = "#FFFFFF";
		nav_1_1_1.style.backgroundColor = "#363636";
		nav_1_1_2.style.color = "#000000";
		nav_1_1_2.style.backgroundColor = "#FFFFFF";
		nav_1_2.style.color = "#000000";
		nav_1_2.style.backgroundColor = "#FFFFFF";
		nav_1_3.style.color = "#000000";
		nav_1_3.style.backgroundColor = "#FFFFFF";
		nav_1_4.style.color = "#000000";
		nav_1_4.style.backgroundColor = "#FFFFFF";
	}
	else if(nav_1_1_2.className.search("active") != -1) {
		nav_1_1.style.color = "#FFFFFF";
		nav_1_1.style.backgroundColor = "#7d007d";
		nav_1_1_1.style.color = "#000000";
		nav_1_1_1.style.backgroundColor = "#FFFFFF";
		nav_1_1_2.style.color = "#FFFFFF";
		nav_1_1_2.style.backgroundColor = "#363636";
		nav_1_2.style.color = "#000000";
		nav_1_2.style.backgroundColor = "#FFFFFF";
		nav_1_3.style.color = "#000000";
		nav_1_3.style.backgroundColor = "#FFFFFF";
		nav_1_4.style.color = "#000000";
		nav_1_4.style.backgroundColor = "#FFFFFF";
	}
	else if(nav_1_2.className.search("active") != -1){
		nav_1_1.style.color = "#000000";
		nav_1_1.style.backgroundColor = "#FFFFFF";
		nav_1_1_1.style.color = "#000000";
		nav_1_1_1.style.backgroundColor = "#FFFFFF";
		nav_1_1_2.style.color = "#000000";
		nav_1_1_2.style.backgroundColor = "#FFFFFF";
		nav_1_2.style.color = "#FFFFFF";
		nav_1_2.style.backgroundColor = "#7d007d";
		nav_1_3.style.color = "#000000";
		nav_1_3.style.backgroundColor = "#FFFFFF";
		nav_1_4.style.color = "#000000";
		nav_1_4.style.backgroundColor = "#FFFFFF";
	}

	else if(nav_1_3.className.search("active") != -1){
		nav_1_1.style.color = "#000000";
		nav_1_1.style.backgroundColor = "#FFFFFF";
		nav_1_1_1.style.color = "#000000";
		nav_1_1_1.style.backgroundColor = "#FFFFFF";
		nav_1_1_2.style.color = "#000000";
		nav_1_1_2.style.backgroundColor = "#FFFFFF";
		nav_1_2.style.color = "#000000";
		nav_1_2.style.backgroundColor = "#FFFFFF";
		nav_1_3.style.color = "#FFFFFF";
		nav_1_3.style.backgroundColor = "#7d007d";
		nav_1_4.style.color = "#000000";
		nav_1_4.style.backgroundColor = "#FFFFFF";
	}

	else if(nav_1_4.className.search("active") != -1){
		nav_1_1.style.color = "#000000";
		nav_1_1.style.backgroundColor = "#FFFFFF";
		nav_1_1_1.style.color = "#000000";
		nav_1_1_1.style.backgroundColor = "#FFFFFF";
		nav_1_1_2.style.color = "#000000";
		nav_1_1_2.style.backgroundColor = "#FFFFFF";
		nav_1_2.style.color = "#000000";
		nav_1_2.style.backgroundColor = "#FFFFFF";
		nav_1_3.style.color = "#000000";
		nav_1_3.style.backgroundColor = "#FFFFFF";
		nav_1_4.style.color = "#FFFFFF";
		nav_1_4.style.backgroundColor = "#7d007d";
	}

	else {
		nav_1_1.style.color = "#FFFFFF";
		nav_1_1.style.backgroundColor = "#7d007d";
		nav_1_1_1.style.color = "#000000";
		nav_1_1_1.style.backgroundColor = "#FFFFFF";
		nav_1_1_2.style.color = "#000000";
		nav_1_1_2.style.backgroundColor = "#FFFFFF";
		nav_1_2.style.color = "#000000";
		nav_1_2.style.backgroundColor = "#FFFFFF";
		nav_1_3.style.color = "#000000";
		nav_1_3.style.backgroundColor = "#FFFFFF";
		nav_1_4.style.color = "#000000";
		nav_1_4.style.backgroundColor = "#FFFFFF";

	}
}