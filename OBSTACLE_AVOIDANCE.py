import time
import serial

ser = serial.Serial(
  
   port='/dev/ttyUSB0',
   baudrate = 9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)
counter=0

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
trigger_pin = 8
echo_pin = 10


GPIO.setup(trigger_pin,0)
GPIO.setup(echo_pin,1)

def front():
    GPIO.output(31,True)
    GPIO.output(33,False)
    GPIO.output(35,True)
    GPIO.output(37,False)#front
    print('Moving forward')

def right():
    GPIO.output(31,True)
    GPIO.output(33,False)
    GPIO.output(35,True)
    GPIO.output(37,False)#right
    print('turning right..')

def stop():
    GPIO.output(31,False)
    GPIO.output(33,False)
    GPIO.output(35,False)
    GPIO.output(37,False)#stop
    print('turning right..')
    

def send_trigger_pulse():
    GPIO.output(trigger_pin, True)
    time.sleep(0.0001)
    GPIO.output(trigger_pin, False)
def wait_for_echo(value, timeout):
    count = timeout
    while GPIO.input(echo_pin) != value and count > 0:
        count = count - 1
def get_distance():
    send_trigger_pulse()
    wait_for_echo(True, 10000)
    start = time.time()
    wait_for_echo(False, 10000)
    finish = time.time()
    pulse_len = finish - start
    distance_cm = (pulse_len *34300)/2
    print(distance_cm)
    return (distance_cm)

    
while 1:    
    distance=get_distance()
    if(distance<30):
        ser.write('1')
        time.sleep(1)
        stop()
        time.sleep(60)
        right()
        time.sleep(3)
        front()
        time.sleep(5)
        left()
        time.sleep(3)
    else:
        front()
