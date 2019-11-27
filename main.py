    import time
    import machine
    import utime
    
    TRIG = machine.Pin(4, machine.Pin.OUT)
    TRIG.off()
    utime.sleep_us(2)
    TRIG.on()
    utime.sleep_us(10)
    TRIG.off()
    ECHO = machine.Pin(5, machine.Pin.IN)
    while ECHO.value() == 0:
        continue
    t1 = utime.ticks_us()
    while ECHO.value() == 1:
        continue
    t2 = utime.ticks_us()
    cm = (t2 - t1) / 58.0
    print(cm)
    utime.sleep(2)
