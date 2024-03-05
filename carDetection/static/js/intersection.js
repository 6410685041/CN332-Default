// Initialize the map
var map = L.map('map').setView([13.7563, 100.5018], 13); // Centered on Bangkok, Thailand

// Add a tile layer to the map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

function onMapClick(e) {
    var latitude = e.latlng.lat;
    var longitude = e.latlng.lng;
    
    // Concatenate latitude and longitude
    var location = latitude + "," + longitude;

    // Update PlainLocationField value
    document.getElementById('location').value = location;
    
    var popup = L.popup()
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(map);
}

map.on('click', onMapClick);