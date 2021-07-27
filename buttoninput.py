import OPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(12, GPIO.RISING)
if GPIO.event_detected(12):
    print("the button was pressed")
GPIO.cleanup()
