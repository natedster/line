let rightsenor = 0
let leftsenor = 0
let sensordifference = 0
input.onButtonPressed(Button.A, function () {
    Kitronik_Move_Motor.stop()
})
input.onButtonPressed(Button.B, function () {
	
})
basic.forever(function () {
    while (Kitronik_Move_Motor.measure() > 4) {
        rightsenor = Kitronik_Move_Motor.readSensor(Kitronik_Move_Motor.LfSensor.Right)
        leftsenor = Kitronik_Move_Motor.readSensor(Kitronik_Move_Motor.LfSensor.Left)
        sensordifference = leftsenor - rightsenor
        if (Math.abs(sensordifference) >= 10) {
            if (leftsenor > rightsenor) {
                Kitronik_Move_Motor.motorOff(Kitronik_Move_Motor.Motors.MotorRight)
                Kitronik_Move_Motor.motorOn(Kitronik_Move_Motor.Motors.MotorLeft, Kitronik_Move_Motor.MotorDirection.Forward, 30)
            } else {
                Kitronik_Move_Motor.motorOff(Kitronik_Move_Motor.Motors.MotorLeft)
                Kitronik_Move_Motor.motorOn(Kitronik_Move_Motor.Motors.MotorRight, Kitronik_Move_Motor.MotorDirection.Forward, 30)
            }
        } else {
            Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.Forward, 50)
        }
    }
    Kitronik_Move_Motor.stop()
})
