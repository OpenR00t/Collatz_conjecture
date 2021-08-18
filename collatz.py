from datetime import datetime

today = datetime.now()
fileDate = today.strftime('%Y-%m-%d-%H-%M-%S')
print("Select starting integer: ", end = '')
start = input()
start = int(start)
num = 0
calculating = True
log = open("{0}_working.log".format(fileDate), "w")


while True:
    now = datetime.now()
    timeCode = now.strftime("%Y-%m-%d %H:%M:%S")
    num = start
    log.write("{0}: testing {1}\n".format(timeCode, start))
    print("{0}: testing {1}".format(timeCode, start))
    calculating = True
    while calculating:
        if (num % 2) == 0:
            num = num / 2
            if num == 1:
                calculating = False
        elif (num % 2) != 0:
            num = (3 * num) + 1
            if num == 1:
                calculating = False
    start = start + 1