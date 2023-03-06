import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class Motor():
    def __init__(self, ENA1, In1, In2, ENB1, In3, In4, ENA2, In5, In6, In7, In8, ENB2, In9, In10, In11, In12):
        # 指尖直流电机ENA1, In1, In2与直流推杆ENB1, In3, In4
        self.ENA1 = ENA1
        self.In1 = In1
        self.In2 = In2
        GPIO.setup(self.ENA1, GPIO.OUT)
        GPIO.setup(self.In1, GPIO.OUT)
        GPIO.setup(self.In2, GPIO.OUT)
        self.pwm1 = GPIO.PWM(self.ENA1, 100)
        self.pwm1.start(0)
        self.ENB1 = ENB1
        self.In3 = In3
        self.In4 = In4
        GPIO.setup(self.ENB1, GPIO.OUT)
        GPIO.setup(self.In3, GPIO.OUT)
        GPIO.setup(self.In4, GPIO.OUT)
        self.pwm2 = GPIO.PWM(self.ENB1, 100)
        self.pwm2.start(0)
        #步进电机3和步进电机4
        self.ENA2 = ENA2
        self.In5 = In5
        self.In6 = In6
        self.In7 = In7
        self.In8 = In8
        self.ENB2 = ENB2
        GPIO.setup(self.ENA2, GPIO.OUT)
        GPIO.setup(self.In5, GPIO.OUT)
        GPIO.setup(self.In6, GPIO.OUT)
        GPIO.setup(self.In7, GPIO.OUT)
        GPIO.setup(self.In8, GPIO.OUT)
        GPIO.setup(self.ENB2, GPIO.OUT)
        self.In9 = In9
        self.In10 = In10
        self.In11 = In11
        self.In12 = In12
        GPIO.setup(self.In9, GPIO.OUT)
        GPIO.setup(self.In10, GPIO.OUT)
        GPIO.setup(self.In11, GPIO.OUT)
        GPIO.setup(self.In12, GPIO.OUT)



#指尖直流电机1与直流推杆2
    def move1(self, speed, t):
        speed *= 100
        self.pwm1.ChangeDutyCycle(abs(speed))
        GPIO.output(self.In1, GPIO.LOW)
        GPIO.output(self.In2, GPIO.HIGH)
        time.sleep(t)
    def move2(self, speed, t):
        speed *= 100
        self.pwm2.ChangeDutyCycle(abs(speed))
        GPIO.output(self.In3, GPIO.LOW)
        GPIO.output(self.In4, GPIO.HIGH)
        time.sleep(t)

    def back1(self, speed, t):
        speed *= 100
        self.pwm1.ChangeDutyCycle(abs(speed))
        GPIO.output(self.In1, GPIO.HIGH)
        GPIO.output(self.In2, GPIO.LOW)
        time.sleep(t)
    def back2(self, speed, t):
        speed *= 100
        self.pwm2.ChangeDutyCycle(abs(speed))
        GPIO.output(self.In3, GPIO.HIGH)
        GPIO.output(self.In4, GPIO.LOW)
        time.sleep(t)

    def stop1(self, t=0):
        self.pwm1.ChangeDutyCycle(0)
        time.sleep(t)
    def stop2(self, t=0):
            self.pwm2.ChangeDutyCycle(0)
            time.sleep(t)

    def setStep1(self, w1, w2, w3, w4, w5, w6):
        GPIO.output(self.ENA2, w1)
        GPIO.output(self.In5, w2)
        GPIO.output(self.In6, w3)
        GPIO.output(self.In7, w4)
        GPIO.output(self.In8, w5)
        GPIO.output(self.ENB2, w6)

    def setStep2(self, w1, w2, w3, w4):
        GPIO.output(self.In9, w1)
        GPIO.output(self.In10, w2)
        GPIO.output(self.In11, w3)
        GPIO.output(self.In12, w4)

    def move3(self, delay, steps):
        for i in range(0, steps):
            self.setStep1(1, 1, 0, 0, 0, 1)
            time.sleep(delay)
            self.setStep1(1, 0, 1, 0, 0, 1)
            time.sleep(delay)
            self.setStep1(1, 0, 0, 1, 0, 1)
            time.sleep(delay)
            self.setStep1(1, 0, 0, 0, 1, 1)
            time.sleep(delay)

    def back3(self, delay, steps):
        for i in range(0, steps):
            self.setStep1(1, 0, 0, 0, 1, 1)
            time.sleep(delay)
            self.setStep1(1, 0, 0, 1, 0, 1)
            time.sleep(delay)
            self.setStep1(1, 0, 1, 0, 0, 1)
            time.sleep(delay)
            self.setStep1(1, 1, 0, 0, 0, 1)
            time.sleep(delay)

    def move4(self, delay, steps):
        for i in range(0, steps):
            self.setStep2(1, 0, 0, 0)
            time.sleep(delay)
            self.setStep2(0, 1, 0, 0)
            time.sleep(delay)
            self.setStep2(0, 0, 1, 0)
            time.sleep(delay)
            self.setStep2(0, 0, 0, 1)
            time.sleep(delay)

    def back4(self, delay, steps):
        for i in range(0, steps):
            self.setStep2(0, 0, 0, 1)
            time.sleep(delay)
            self.setStep2(0, 0, 1, 0)
            time.sleep(delay)
            self.setStep2(0, 1, 0, 0)
            time.sleep(delay)
            self.setStep2(1, 0, 0, 0)
            time.sleep(delay)