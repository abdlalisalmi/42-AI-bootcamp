
def formated(arg):
    return arg if len(str(arg)) == 2 else '0'+str(arg)


tm = (3,30,2019,9,25)

hour = formated(tm[0])
minutes = formated(tm[1])
month = formated(tm[3])
day = formated(tm[4])

print(f"{month}/{day}/{tm[2]} {hour}:{minutes}")