document.addEventListener('DOMContentLoaded', function() {
    const video = document.getElementById('video');
    const playButton = document.getElementById('play-button');

    function updatePlayButtonText() {
        playButton.textContent = video.paused ? 'Play' : 'Pause';
        playButton.style

        if (video.paused) {
            playButton.style.background = "green";
         } else {
            playButton.style.background = "skyblue";
         }
    }

    playButton.addEventListener('click', function() {
        if (video.paused) {
            video.play();
        } else {
            video.pause();
        }
        updatePlayButtonText();
    });

    updatePlayButtonText();
});