# IoTZSE
main.py to aktualny plik
oldmain.py to plik który wysłałem Panu za pierwszym razem na librusa


W tym kodzie głównie korzystałem z dokumentacji micropythona
http://docs.micropython.org/en/latest/esp32/quickref.html# 
https://docs.micropython.org/en/latest/esp32/quickref.html#pins-and-gpio
Podlaczony HC-SR04 przez rezystory, lacznie 3k do ESP32
micropython ma odczytac do jakich pinow jest podlaczony HC-SR04, wyslac sygnal, odczytać w jakim czasie trafi do ESP32 poprzez utime i przeliczyc dystans od obiektu, nastepnie na odpalonym serwerze na stronie ma pojawic sie wyliczony dystans od obiektu,
po linii 18(while ECHO.value() == 0) pojawia się błąd, probowalem roznych rozwiazan, innych metod definiowania stanu pinów(wysokiego i niskiego), szczerze sam już nie wiem, czy kod od 11 do 26 linijki ma poprawną składnie odnośnie micropythona

Teoretycznie można użyć biblioteki https://github.com/rsc1975/micropython-hcsr04
wtedy kod od 11 do 26 linijki zastąpić:

    import time
    import machine
    import utime
    from hcsr04 import HCSR04
    
    while True:
        sensor = HCSR04(trigger_pin=4, echo_pin=5, echo_timeout_us=1000000)
        distance = sensor.distance_cm()
        print('Distance:', distance, 'cm')
    

jednak kod powyżej zwraca wartość około -0.306... za każdym razem, niezależnie od tego czy obiekt jest oddalony o kilka centymetrów, metr czy obojętnie jaki dystans
