let availableTimes = [
    {times: ['13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00']}
];

let SlideshowIndex = 0;

function changeSlideshowImage() {
    const img = document.getElementById('slideshowImage');
    SlideshowIndex = (SlideshowIndex + 1) % SlideshowImagesList.length;
}