import math


def formated(arg):
    return arg if len(str(arg)) == 2 else '0'+str(arg)


t = ( 0, 4, 132.42222, 10000, 12345.67)

print(f"day_{formated(t[0])}, ex_{formated(t[1])} : {t[2]:.2f}, {t[3]:.2e}, {t[4]:.2e}")
