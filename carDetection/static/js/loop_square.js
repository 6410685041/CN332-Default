const videoWrapper = document.getElementById('video-wrapper');

let current = 0;
let points = [{x: 0, y: 0}, {x: 0, y: 0}, {x: 0, y: 0}, {x: 0, y: 0}];

function updatePointsFromInputs() {
    for (let i = 1; i <= 4; i++) {
        const x = document.getElementById(`x${i}`).value;
        const y = document.getElementById(`y${i}`).value;
        points[i - 1] = { x: parseInt(x, 10), y: parseInt(y, 10) };
    }
}

for (let i = 1; i <= 4; i++) {
    document.getElementById(`x${i}`).addEventListener('change', updatePointsFromInputs);
    document.getElementById(`y${i}`).addEventListener('change', updatePointsFromInputs);
}

videoWrapper.addEventListener('click', function(event) {
    const rect = videoWrapper.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    document.getElementById(`x${current + 1}`).value = x;
    document.getElementById(`y${current + 1}`).value = y;

    points[current] = { x, y };
});

document.addEventListener('keydown', function(event) {
    if (event.key === "0") {
        points = [{x: 0, y: 0}, {x: 0, y: 0}, {x: 0, y: 0}, {x: 0, y: 0}];
        for (let i = 1; i <= 4; i++) {
            document.getElementById(`x${i}`).value = 0;
            document.getElementById(`y${i}`).value = 0;
        }
    }
    if (event.key >= "1" && event.key <= "4") {
        current = parseInt(event.key, 10) - 1;
    }
});

// Initialize points from existing input values
updatePointsFromInputs();


video.addEventListener('click', function(event) {
    console.log('Video clicked'); // Check if this logs when the video is clicked
    const rect = videoWrapper.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    console.log(`Coordinates: ${x}, ${y}`); // Check the calculated coordinates

    document.getElementById(`x${current + 1}`).value = x;
    document.getElementById(`y${current + 1}`).value = y;

    points[current] = { x, y };
    console.log(`Current point: ${current}`, points[current]); // Check the current point's value

    if (current < 3) {
        current++;
    } else {
        current = 0;
    }
});