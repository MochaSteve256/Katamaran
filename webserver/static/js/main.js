document.addEventListener('DOMContentLoaded', function () {
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    // Initialize JoyStick object in the DIV 'joyDiv'
    var joy = new JoyStick('joyDiv', {}, function (stickData) {
        // Send joystick data to the server
        socket.emit('joystick_data', stickData);
    });

    // Optional: If you want to update server every 50 milliseconds
    setInterval(function () {
        socket.emit('joystick_data', joy.GetX()); // Adjust as needed
    }, 50);
})
