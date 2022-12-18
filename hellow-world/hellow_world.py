class HW:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        return f'Hi, {self.name}'

if __name__ == '__main__':
    hw = HW('Dima')
    print(f'{hw.say_hi()}')
