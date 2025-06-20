import board, mpu6886, time, math

i2c = board.I2C()  # uses board.SCL and board.SDA
mpu = mpu6886.MPU6886(i2c)

# Take X, Y, and Z acceleration values in m/s^2
# Return pitch angle bertween the ground surface and the positive (right) side of the Y axis
#
def pitch(x, y, z):
    accelMagnitude = math.sqrt(x**2 + y**2 + z**2)
    xNormalized = x/accelMagnitude
    yNormalized = y/accelMagnitude
    pitchY = math.asin(-yNormalized)
    if z <= 0:
        pitchY += math.pi/4
    return pitchY

while True:
    accel = mpu.acceleration
    x = accel[0]
    y = accel[1]
    z = accel[2]
    print(f"Acceleration: X:{x:.2f}, Y:{y:.2f}, Z:{z:.2f} m/s^2")
    pitchY = pitch(x, y, z)
    print("radian:", pitchY)
    print("degrees:", math.degrees(pitchY))
           
#  gy = mpu.gyro
# 
#     print(f"Gyro X:{gy[0]:.2f}, Y:{gy[1]:.2f}, Z:{gy[2]:.2f} rad/s")
#     print(f"Temperature: {mpu.temperature:.2f} C")
#     print("")
    time.sleep(1)

# mpu.gyro_range = 1
# time.sleep(0.05)
# mpu.accelerometer_range = 1
# time.sleep(0.05)
