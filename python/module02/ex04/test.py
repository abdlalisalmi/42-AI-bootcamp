from ai42.progressbar import ft_progress
import time






if __name__ == '__main__':
    listy = range(3000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)