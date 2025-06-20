import board, mpu6886, time, math
import display

DEMO_MODE = True
ACCEL_SENSING_INTERVAL = 1 # in seconds

i2c = board.I2C()
mpu = mpu6886.MPU6886(i2c)

# Take X, Y, and Z acceleration values in m/s^2.
# Return the pitch angle (in radian) between the ground surface
#   and the positive (right) side of the Y axis.
#
def calcPitch(x, y, z):
    accelMagnitude = math.sqrt(x**2 + y**2 + z**2)
    xNormalized = x/accelMagnitude
    yNormalized = y/accelMagnitude
    pitchY = math.asin(-yNormalized)
    if z <= 0:
        pitchY += math.pi/4
    return pitchY

if DEMO_MODE:
    display.init()
    time.sleep(3)

while True:
    accel = mpu.acceleration
    x = accel[0]
    y = accel[1]
    z = accel[2]
    pitchRadian  = calcPitch(x, y, z)
    pitchDegrees = round( math.degrees(pitchRadian) )
    print("Pitch (degrees):", pitchDegrees)
    if DEMO_MODE:
        display.resetText("Pitch:" + str(pitchDegrees))
           
    time.sleep(ACCEL_SENSING_INTERVAL)


