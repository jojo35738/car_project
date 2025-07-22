import RPi.GPIO as GPIO
import time

# GPIO festlegen
GPIO.setmode(GPIO.BCM)
IN1 = 17
IN2 = 18
IN3 = 27
IN4 = 22

# Ausgänge setzen
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Bewegungsfunktionen
def forward():
    print("Vorwärts")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def backward():
    print("Rückwärts")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def left():
    print("Links")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def right():
    print("Rechts")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def stop():
    print("Stop")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

# Hauptprogramm
try:
    while True:
        cmd = input("Befehl (f=vor, b=zurück, l=links, r=rechts, s=stopp, q=quit): ").strip().lower()

        if cmd == "f":
            forward()
        elif cmd == "b":
            backward()
        elif cmd == "l":
            left()
        elif cmd == "r":
            right()
        elif cmd == "s":
            stop()
        elif cmd == "q":
            print("Beende Programm.")
            break
        else:
            print("Ungültiger Befehl!")

except KeyboardInterrupt:
    print("Abbruch mit STRG+C")

finally:
    stop()
    GPIO.cleanup()
    print("GPIO aufgeräumt.")
