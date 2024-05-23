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

    // Clear the location field when the popup is closed
    popup.on('remove', function() {
        document.getElementById('location').value = null;
    });
}

map.on('click', onMapClick);

// view location for each intersection
function updateMap(event, intersectionId) {
    event.preventDefault();  // Prevent form submission

    // Get the location value from the hidden input
    var locationValue = document.getElementById('location_' + intersectionId).value;

    // Assuming locationValue is in "latitude,longitude" format
    var parts = locationValue.split(',');
    var latitude = parseFloat(parts[0]);
    var longitude = parseFloat(parts[1]);

    // Assuming 'map' is your Leaflet map variable
    map.setView([latitude, longitude], 13);  // 13 is the zoom level, adjust as needed

    // Creating a LatLng object for the popup
    var latLng = L.latLng(latitude, longitude);

    // Creating and opening the popup
    var popup = L.popup()
        .setLatLng(latLng)
        .setContent("Location: " + latitude + ", " + longitude)
        .openOn(map);
}