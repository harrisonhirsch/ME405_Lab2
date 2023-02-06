import utime
import serial

with(serial.serial('COM4', 115200) as ser):
    ser.flush()
    data_list = []
    while True:
        if ser.in_waiting() > 0:
            data_list.append(ser.readline())
            print(datalist)
        else:
            utime.sleep_ms(10)
        