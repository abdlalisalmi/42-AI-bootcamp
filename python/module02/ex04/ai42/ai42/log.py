import time
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