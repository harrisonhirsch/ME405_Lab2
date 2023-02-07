import time
import serial
import matplotlib.pyplot as plt


def main():
    with(serial.Serial('COM4', 115200) as ser):
        ser.flush()
        plt.close()
        data_list_x = []
        data_list_y = []
        # line = 0
        while True:
            if ser.inWaiting() > 0:
                # line = str(ser.readline())
                # line = line.replace('\\n', '')
                # line = line.split(',')
                # data_list.append(line)
                # print(line)
                data = ser.readline().strip(b'\n').split(b', ')
                data_list_x.append(float(data[0]))
                data_list_y.append(float(data[1]))
                if data_list_x[len(data_list_x)-1] > 6000:
                    break
            else:
                time.sleep(0.01)
    print('checkpoint')
    # print(data_list_y)
    # fig, graph = plt.subplots()
    # graph.plot(data_list_x, data_list_y, 'r-')
    # graph.set_xlabel('Time [ms]')
    # graph.set_ylabel('Position [encoder counts]')
    plt.plot(data_list_x, data_list_y, 'r-')
    plt.xlabel('Time [ms]')
    plt.ylabel('Position [encoder counts]')
    plt.show()


def is_number(pt):          # Helper function to test if number
    try:
        float(pt)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    main()
        