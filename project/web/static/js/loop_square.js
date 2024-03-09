const videoWrapper = document.getElementById('video-wrapper');
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

let current = 0;
let points = [{x: 0, y: 0}, {x: 0, y: 0}, {x: 0, y: 0}, {x: 0, y: 0}];

function updatePointsFromInputs() {
    for (let i = 1; i <= 4; i++) {
        const x = document.getElementById(`x${i}`).value;
        const y = document.getElementById(`y${i}`).value;
        points[i - 1] = { x: parseInt(x, 10), y: parseInt(y, 10) };
    }
    drawPoints();
}

for (let i = 1; i <= 4; i++) {
    document.getElementById(`x${i}`).addEventListener('change', updatePointsFromInputs);
    document.getElementById(`y${i}`).addEventListener('change', updatePointsFromInputs);
}

videoWrapper.addEventListener('click', function(event) {
    const rect = video.getBoundingClientRect(); // Use video instead of videoWrapper to get the correct scaling factor
    const scaleX = video.videoWidth / rect.width;
    const scaleY = video.videoHeight / rect.height;

    const x = (event.clientX - rect.left) * scaleX;
    const y = (event.clientY - rect.top) * scaleY;

    document.getElementById(`x${current + 1}`).value = Math.round(x);
    document.getElementById(`y${current + 1}`).value = Math.round(y);

    points[current] = { x: Math.round(x), y: Math.round(y) };

    if (current < 3) {
        current++;
    } else {
        current = 0;
    }
    drawPoints();
});

function drawPoints() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    points.forEach(point => {
        ctx.fillStyle = '#FF0000';
        ctx.beginPath();
        ctx.arc(point.x, point.y, 2, 0, 2 * Math.PI);
        ctx.fill();
    });
}

// Initialize points from existing input values
updatePointsFromInputs();

document.addEventListener('keypress', function(event) {
    if (event.key === '1') {
        current = 0;
    } else if (event.key === '2') {
        current = 1;
    } else if (event.key === '3') {
        current = 2;
    } else if (event.key === '4') {
        current = 3;
    }
});