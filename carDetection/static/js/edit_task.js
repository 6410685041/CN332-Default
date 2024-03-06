// document.addEventListener('DOMContentLoaded', function() {
//   const video = document.getElementById('video');
//   const canvas = document.getElementById('video-overlay');
//   const ctx = canvas.getContext('2d');
//   let points = [];

//   function resizeCanvas() {
//       canvas.width = video.offsetWidth;
//       canvas.height = video.offsetHeight;
//       canvas.style.position = 'absolute';
//       canvas.style.left = video.offsetLeft + 'px';
//       canvas.style.top = video.offsetTop + 'px';
//   }

//   function drawPoint(x, y) {
//       const radius = 5; // Radius of the point
//       ctx.fillStyle = 'red';
//       ctx.beginPath();
//       ctx.arc(x, y, radius, 0, 2 * Math.PI);
//       ctx.fill();
//   }

//   function updateCanvas() {
//       ctx.clearRect(0, 0, canvas.width, canvas.height);
//       if (points.length > 0) {
//           points.forEach(point => {
//               drawPoint(point.x, point.y);
//           });

//           if (points.length > 1) {
//               ctx.beginPath();
//               ctx.moveTo(points[0].x, points[0].y);
//               for (let i = 1; i < points.length; i++) {
//                   ctx.lineTo(points[i].x, points[i].y);
//               }
//               if (points.length === 4) {
//                   ctx.lineTo(points[0].x, points[0].y); // Close the rectangle
//               }
//               ctx.strokeStyle = 'red';
//               ctx.stroke();
//           }
//       }
//   }

//   function captureClick(e) {
//       if (points.length >= 4) {
//           points = []; // Reset points if there are already 4
//       }

//       const rect = canvas.getBoundingClientRect();
//       const x = e.clientX - rect.left;
//       const y = e.clientY - rect.top;
//       points.push({ x: x, y: y });

//       if (points.length === 4) {
//           // Update input fields with the points
//           document.getElementById('x1').value = points[0].x;
//           document.getElementById('y1').value = points[0].y;
//           document.getElementById('x2').value = points[1].x;
//           document.getElementById('y2').value = points[1].y;
//           document.getElementById('x3').value = points[2].x;
//           document.getElementById('y3').value = points[2].y;
//           document.getElementById('x4').value = points[3].x;
//           document.getElementById('y4').value = points[3].y;
//       }

//       updateCanvas();
//   }

//   function resetPoints(e) {
//       if (e.key === "Escape") {
//           points = [];
//           updateCanvas();
//       }
//   }

//   window.addEventListener('resize', resizeCanvas);
//   canvas.addEventListener('click', captureClick);
//   document.addEventListener('keydown', resetPoints);

//   resizeCanvas();
// });

// Get the canvas element
let canvas = document.getElementById("myCanvas");
// Get the context
let ctx = canvas.getContext("2d");
// Create the video - can use any video url
let video = document.createElement("video");
video.src = "video.mp4";
video.play();
// Set the video to loop
video.loop = true;

// Create a function to draw frames on the canvas
let draw = function () {
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
  // Repeat the draw loop
  requestAnimationFrame(draw);
};

// Call the draw loop
draw();