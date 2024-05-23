document.addEventListener('DOMContentLoaded', function() {
    const video = document.getElementById('video');
    const playButton = document.getElementById('play-button');

    function updatePlayButtonText() {
        playButton.textContent = video.paused ? '\u23F5 Play' : '\u275A\u275A Pause';
        playButton.style

        if (video.paused) {
            playButton.style.background = "#" + hexFromRGB(2, 158, 95);
         } else {
            playButton.style.background = "#" + hexFromRGB(235, 115, 115);
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

    /* use for color */
    function hexFromRGB(r, g, b) {
        var hex = [
          r.toString( 16 ),
          g.toString( 16 ),
          b.toString( 16 )
        ];
        $.each( hex, function( nr, val ) {
          if ( val.length === 1 ) {
            hex[ nr ] = "0" + val;
          }
        });
        return hex.join( "" ).toUpperCase();
      }
});