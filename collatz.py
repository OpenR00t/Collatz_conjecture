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
    #log.write("{0}: testing {1}\n".format(timeCode, start))
        #logs were far too large to work with
    print("{0}: testing {1}".format(timeCode, start))
    calculating = True
    count = 0
    while calculating:
        if (num % 2) == 0:
            num = num / 2
            if num == 1:
                calculating = False
        elif (num % 2) != 0:
            num = (3 * num) + 1
            if num == 1:
                calculating = False
        count += 1
        if count > 1000:
            calculating = False
            print("{0}: {1} reached 1000 iterations without hitting 1".format(timeCode, start))
            log.write("{0}: {1} reached 1000 iterations without hitting 1".format(timeCode, start))
    start = start + 1