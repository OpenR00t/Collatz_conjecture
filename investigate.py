from datetime import datetime

today = datetime.now()
fileDate = today.strftime('%Y-%m-%d-%H-%M-%S')
print("Enter number needing verification: ", end = '')
start = input()
start = int(start)
log = open("{0}_investigate.log".format(fileDate), "w")
run = True
num  = start
while run:
    now = datetime.now()
    timeCode = now.strftime("%Y-%m-%d %H:%M:%S")
    print("{0}: {1}".format(timeCode, num))
    log.write("{0}: {1}\n".format(timeCode, num))
    if (num % 2) == 0:
        num = num / 2
        if num == 1:
            run = False
    elif (num % 2) != 0:
        num = (3 * num) + 1
        if num == 1:
            run = False
print("{0}: verification of {1} failed".format(timeCode, start))
log.write("{0}: verification of {1} failed".format(timeCode, start))