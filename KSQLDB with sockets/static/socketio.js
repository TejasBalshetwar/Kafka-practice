document.addEventListener('DOMContentLoaded', function() {
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    var room = 0;
    // Log incoming message
    socket.on('message', function(msg) {
        console.log(`Message received: ${msg}`);
    });

    // playing live logs and joining room
    document.querySelector('#play_log').onclick = function() {
        socket.emit('play_log', "start");
        newroom = Math.floor(Math.random()*10000);
        room = newroom;
        socket.emit('join', {'room': String(room)});
    };

    // stop live logs and leave room
    document.querySelector('#stop_log').onclick = function() {
        socket.emit('play_log', "stop");
        socket.emit('leave', {'room': String(room)});
        room = 0;
    };
    // display logs
    socket.on('log', function(data) {
        if (room === 0)
            return;
        const tr = document.createElement('tr');
        const td = document.createElement('td');
        const td2 = document.createElement('td');
        const td3 = document.createElement('td');
        level = data['level'];
        message = data['message'];
        timestamp = data['timestamp'];
        td.innerHTML = `${timestamp}`;
        td2.innerHTML = `${level}`;
        td3.innerHTML = `${message}`;
        tr.append(td);
        tr.append(td2);
        tr.append(td3);
        document.querySelector('#logs').prepend(tr);
    });


    
});