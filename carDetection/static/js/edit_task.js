document.addEventListener('DOMContentLoaded', function() {
    const video = document.getElementById('video');
    const playButton = document.getElementById('play-button');
    const canvas = document.getElementById('canvas');

    let current = 0;
    let points = [];

    // Function to update points array with input field values
    function updatePointsFromInputs() {
        const x = document.getElementById(`x${current+1}`).value;
        const y = document.getElementById(`y${current+1}`).value;

        // Only add point if both coordinates are provided
        if (x !== '' && y !== '') {
            points.push({ x: parseFloat(x), y: parseFloat(y) });
        }
    }

    // Call the function to initially populate the points array
    updatePointsFromInputs();

    // Optionally, listen for changes in input fields to update points array dynamically
    for (let i = 1; i <= 4; i++) {
        document.getElementById(`x${i}`).addEventListener('change', updatePointsFromInputs);
        document.getElementById(`y${i}`).addEventListener('change', updatePointsFromInputs);
    }

    function updatePlayButtonText() {
        playButton.textContent = video.paused ? 'Play' : 'Pause';
    }

    playButton.addEventListener('click', function() {
        if (video.paused) {
            video.play();
        } else {
            video.pause();
        }
        updatePlayButtonText();
    });

    // Canvas click event for video pointing
    canvas.addEventListener('click', function(event) {
        
        // Get click coordinates relative to the canvas
        const rect = canvas.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;
        points.push({ x, y });

        // Implement logic to display points on canvas or use them as needed
    });

    // Keydown event for resetting points
    document.addEventListener('keydown', function(event) {
        if(event.key === "Escape") {
            points = [];
        }
        if(event.key === "1") {
            current = 0
        }
        else if(event.key === "2") {
            current = 1
        }
        else if(event.key === "3") {
            current = 2
        }
        else if(event.key === "4") {
            current = 3
        }
    });

    updatePlayButtonText();
});