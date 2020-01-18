import time
import machine
import utime


def web_page():
    
    
    

    TRIG = machine.Pin(12, machine.Pin.OUT)
    TRIG.off()
    utime.sleep_us(2)
    TRIG.on()
    utime.sleep_us(10)
    TRIG.off()
    ECHO = machine.Pin(13, machine.Pin.IN)
    while ECHO.value() == 0:
        pass
    t1 = utime.ticks_us()
    while ECHO.value() == 1:
        pass
    t2 = utime.ticks_us()
    cm = (t2 - t1) / 58.0
    print(cm)
    utime.sleep(2)
    


 
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<Title>Text To Speech</title>
</head>
<body>

<input type="text" name="text">
<button id="gspeech" class="say">Say It</button>
<p>Dystans: <strong>""" + str(cm) + """</strong></p>
<audio src="" class="speech" hidden></audio>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<script src="https://code.responsivevoice.org/responsivevoice.js?key=HNtntKsB"></script>

<script>
$(function() {
$('#gspeech').on('click',function(){
console.log(text);
var text = $('input[name="text"]').val();
responsiveVoice.speak(`${text}`, "UK English Male");
});
});
</script>
</body>
</html>
"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
