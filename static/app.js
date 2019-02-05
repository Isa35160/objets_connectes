$(function () {
    socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('TempLive', function (data) {
        $('#tempDetectInterne').text(data)
    });

    socket.on('LightLive', function (data) {
        $('#lightDetect').html();
        {
            if (data >= 80) {
                $('#lightDetect').css({
                        "background-color": 'white',
                        "color":'black'
                })
            }
            ;
        }
    });
});
