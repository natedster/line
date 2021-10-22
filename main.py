rightsenor = 0
leftsenor = 0
sensordifference = 0

def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global rightsenor, leftsenor, sensordifference
    while Kitronik_Move_Motor.measure() > 4:
        rightsenor = Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.RIGHT)
        leftsenor = Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.LEFT)
        sensordifference = leftsenor - rightsenor
        if abs(sensordifference) >= 10:
            if leftsenor > rightsenor:
                Kitronik_Move_Motor.motor_off(Kitronik_Move_Motor.Motors.MOTOR_RIGHT)
                Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_LEFT,
                    Kitronik_Move_Motor.MotorDirection.FORWARD,
                    15)
            else:
                Kitronik_Move_Motor.motor_off(Kitronik_Move_Motor.Motors.MOTOR_LEFT)
                Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_RIGHT,
                    Kitronik_Move_Motor.MotorDirection.FORWARD,
                    15)
        else:
            Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 33)
    Kitronik_Move_Motor.stop()
basic.forever(on_forever)
