import serial
s=serial.Serial("/dev/cu.usbmodem1431",9600)
for i in range(10):
     data=s.read(s.inWaiting()).decode("utf-8")
     print('size = %d, buffer = %d' % (len(data),s.inWaiting()))
     data = data.splitlines()
     print(data)
     # imu = data[0].split(',')
     # print(imu)
