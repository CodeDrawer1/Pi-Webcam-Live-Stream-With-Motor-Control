print('Importing GPIO library')
import RPi.GPIO as GPIO
print("Importing time library")
import time
print("Setting Pinmode")
GPIO.setmode(GPIO.BOARD)
print("Cleaning up possible messes")
GPIO.cleanup()
print("Initalising motors")
leftMotor = 11
rightMotor = 13
GPIO.setup(leftMotor, GPIO.OUT)
GPIO.setup(rightMotor, GPIO.OUT)
direction = raw_input("What is your favorite letter?")
print("Final setup")
direction = " "
while direction != 'terminate':
    print(" ")
    print("Type terminate to end program")
    print(" ")
    direction = raw_input("Next operation... W, A, S, or D?     ")
    print(" ")
    duration = float(raw_input("Duration of this operation? In seconds.     "))
    print(" ")
    if direction == "W":
        GPIO.output(leftMotor, 1)
        GPIO.output(rightMotor, 1)
    elif direction == "A":
        GPIO.output(rightMotor, 1)
    elif direction == "D":
        GPIO.output(leftMotor, 1)
    else:
        GPIO.output(leftMotor, 0)
        GPIO.output(rightMotor, 0)
    time.sleep(duration)

GPIO.cleanup()
print("GPIO pins cleaned up, turn off pi, and then disconnect the power source. Type 'sudo shutdown -h now' for a proper shutdown.")

