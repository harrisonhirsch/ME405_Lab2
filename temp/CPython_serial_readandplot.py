import time
import serial
import matplotlib.pyplot as plt


def main():
    with(serial.Serial('COM4', 115200) as ser):
        ser.flush()
        plt.close()
        data_list_x = []
        data_list_y = []
        try:
            while True:
                if ser.inWaiting() > 0:
                    data = ser.readline().strip(b'\r\n').split(b', ')
                    data_list_x.append(float(data[0]))
                    data_list_y.append(float(data[1]))
                    if len(data_list_x) >= 600:
                        break
                else:
                    time.sleep(0.01)
        except (ValueError, IndexError) as e:
            print(e)
    print('checkpoint')
    plt.plot(data_list_x, data_list_y, 'r-')
    plt.xlabel('Time [ms]')
    plt.ylabel('Position [encoder counts]')
    plt.annotate(f'{data_list_y[len(data_list_y)-1]} Counts', xy=(data_list_x[len(data_list_x)-1]-1000, data_list_y[len(data_list_y)-1]-5000))
    plt.show()


# def is_number(pt):          # Helper function to test if number
#     try:
#         float(pt)
#         return True
#     except ValueError:
#         return False


if __name__ == '__main__':
    main()
        