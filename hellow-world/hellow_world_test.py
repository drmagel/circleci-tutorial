from hellow_world import HW

class TestHW:

    def test_one(self):
        name = 'Dima'
        hw = HW(name)
        hw.say_hi()
        assert hw.say_hi() == f'Hi, {name}'

