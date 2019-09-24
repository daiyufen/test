from time import sleep
import os


class Clock(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.hour += 1
                self.minute = 0
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        print('%d:%d:%d' % (self.hour,self.minute,self.second))


def main():
 clock = Clock(23,58,59)

 while True:
     clock.show()
     sleep(1)
     clock.run()

if __name__ == '__main__':
    main()





