import time
from random import randint
import functools
import os



def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        function_name = ' '.join(word.capitalize() for word in func.__name__.split('_'))

        start_time = time.time()    # 1
        value = func(*args, **kwargs)
        end_time = time.time()      # 2
        run_time = end_time - start_time    # 3
        with open(f'{os.path.dirname(os.path.realpath(__file__))}/machine.log', 'a') as file:
            file.write(f"""(cmaxime)Running: {function_name}{''.join(' ' for i in range(20 - len(function_name)))}[ exec-time = {run_time:.3f} {"ms" if run_time < 1 else "s "} ]\n""")
        return value
    return wrapper


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":

    machine = CoffeeMachine()

    for i in range(0, 5):
        machine.make_coffee()
        
    machine.make_coffee()
    machine.add_water(70)