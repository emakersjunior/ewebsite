function myMap() {
	var mapProp= {
	    center:new google.maps.LatLng(-21.227850, -44.978601),
	    zoom:18,
	};
	var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);
}