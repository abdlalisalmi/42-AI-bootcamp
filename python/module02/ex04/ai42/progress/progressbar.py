import sys
from time import sleep


def ft_progress(listy, file=sys.stdout):
    size=30
    count = len(listy)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i %s\r" % ("ETA: 8.67s [ 23%] ", "="*x, " "*(size-x), j, count, " | elapsed time 2.33s"))
        file.flush()        
    show(0)
    for i, item in enumerate(listy):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()



if __name__ == '__main__':
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    # print()
    # print(ret)