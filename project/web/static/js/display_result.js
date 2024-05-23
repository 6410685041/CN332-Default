const videoWrapper = document.getElementById('video-wrapper');
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const parameter = document.getElementById('loop_number');

createAndDisplayPoints();

function createAndDisplayPoints() {

    const taskId = window.taskId;
    const jsonUrl = `/static/json/loop_data/${taskId}.json`;

    fetch(jsonUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            data.loops.forEach(loop => {
                let before_x = loop.points[3].x;
                let before_y = loop.points[3].y;

                let TextPoint_x = loop.points[0].x;
                let TextPoint_y = loop.points[0].y;

                loop.points.forEach(point => {
                    ctx.fillStyle = '#00FF00';
                    ctx.strokeStyle = '#00FF00';
                    ctx.beginPath();
                    ctx.arc(point.x * 0.6, point.y * 0.5, 2, 0, 2 * Math.PI);
                    ctx.fill();

                    // line
                    ctx.moveTo(before_x*0.6, before_y*0.5);
                    ctx.lineTo(point.x * 0.6, point.y * 0.5, 2, 0, 2 * Math.PI);
                    ctx.stroke();

                    before_x = point.x;
                    before_y = point.y;

                    if(TextPoint_x>point.x){
                        if(TextPoint_y<point.y){
                            TextPoint_x = point.x;
                            TextPoint_y = point.y;
                        }
                    }
                });
                
                const rectX = TextPoint_x * 0.6;
                const rectY = TextPoint_y * 0.5;

                // Display text within the rectangle
                ctx.fillStyle = '#0000FF';
                ctx.font = '10px Arial';
                ctx.fillText(`Loop${loop.id}`, rectX, rectY);
            });
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}