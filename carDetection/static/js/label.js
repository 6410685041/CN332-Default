document.getElementById('labelForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    
    fetch('', {
        method: 'POST',
        body: formData,
        headers: {'X-CSRFToken': '{{ csrf_token }}'},
    })
    .then(response => response.json())
    .then(data => {
        alert(JSON.stringify(data));
        // Process the returned JSON data as needed
    })
    .catch(error => console.error('Error:', error));
});