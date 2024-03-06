// <!-- Video control buttons -->
document.addEventListener('DOMContentLoaded', function() {
    const video = document.getElementById('video');
    const playButton = document.getElementById('play-button');

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

    stopButton.addEventListener('click', function() {
        video.pause();
        video.currentTime = 0;
        updatePlayButtonText();
    });

    // Update the button text initially
    updatePlayButtonText();
});

// video pointing
// Get the video element and video wrapper
const video = document.getElementById('video');
const videoWrapper = document.getElementById('video-wrapper');

var count = 4
var points = []

function keyPress(e) {
    if(e.key === "Escape") {
        // write your logic here.
        count = 4
        points = []
    }
}

video.addEventListener('click', function(event) {

    // Get the canvas element
    var canvas = document.getElementById("canvas");
    // Get the context
    let ctx = canvas.getContext("2d");

  // Get the click coordinates
  const { clientX, clientY } = event;

  // Create a new box element
  box = document.createElement('div');
  box.className = 'box';
  box.style.left = (clientX - videoWrapper.offsetLeft) + 'px';
  box.style.top = (clientY - videoWrapper.offsetTop) + 'px';

  // Create a text element for displaying the coordinates
  const text = document.createElement('span');
  text.textContent = `(${clientX + videoWrapper.offsetWidth/8 - videoWrapper.offsetLeft/2}, ${clientY - videoWrapper.offsetHeight/2})`;
  box.appendChild(text);

  // Append the box to the video wrapper
  videoWrapper.appendChild(box);
});