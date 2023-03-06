from f_MotorModule import Motor
import f_KeyPressModule as kp

motor = Motor(7, 11, 12, 13, 15, 16, 18, 22, 29, 31, 32, 33, 35, 36, 37, 38)

kp.init()


def main():
    #直流减速
    if kp.getKey('LEFT'):
        motor.move1(0.5, 0.01)
    elif kp.getKey('RIGHT'):
        motor.back1(0.5, 0.01)
    #推杆
    elif kp.getKey('DOWN'):
        motor.move2(0.5, 0.01)
    elif kp.getKey('UP'):
        motor.back2(0.5, 0.01)
    #步进1
    elif kp.getKey('w'):
        motor.move3(0.002, 10)
    elif kp.getKey('s'):
        motor.back3(0.002, 10)
    #步进2
    elif kp.getKey('a'):
        motor.move4(0.002, 10)
    elif kp.getKey('d'):
        motor.back4(0.002, 10)
    else:
        motor.stop1()
        motor.stop2()


if __name__ == '__main__':
    while True:
        main()