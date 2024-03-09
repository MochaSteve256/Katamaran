document.addEventListener('DOMContentLoaded', function () {
    const socket = io.connect('http://' + document.domain + ':' + location.port);
});

function shiz() {
    
}

const listener = new GamepadListener();
listener.start()

listener.on("gamepad:axis", (event) => {
    console.log(event);
});
