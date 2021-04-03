import time
import sys


def ft_progress(listy):
    size=25
    total = len(listy)

    start_time = time.time()

    est = (0.00003 * total) + (0.01 * total)

    def show_progress(actual):
        x = int(size * actual / total)
        sys.stdout.write(f"ETA: {est:.2f}s [ {int((actual/total) * 100)}%][{'='*x}>{' ' * (size-x)}] {actual}/{total} | elapsed time {time.time() - start_time:.2f}s\r")
        sys.stdout.flush()        

    for i, item in enumerate(listy):
        yield item
        show_progress(i+1)
    sys.stdout.write("\n...")
    sys.stdout.flush()



if __name__ == '__main__':
    listy = range(3000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)