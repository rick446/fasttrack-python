import time
import multiprocessing

def print_time():
    while True:
        print time.ctime()
        time.sleep(1)

def main():
    t = multiprocessing.Process(target=print_time)
    t.start()
    time.sleep(10)
    t.terminate()


if __name__ == '__main__':
    main()
