const video = document.getElementById('video');
const videoWrapper = document.getElementById('video-wrapper');

let box = null; // Reference to the box element
// Add a click event listener to the video
video.addEventListener('click', function(event) {
  // Remove the previous box if it exists
  if (box) {
    videoWrapper.removeChild(box);
    box = null;
  }

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
