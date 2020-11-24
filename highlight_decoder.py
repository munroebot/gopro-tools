import math, sys

def transform_timestamp(timestamp):
    minutes = timestamp / 60000.0
    seconds = int((math.modf(minutes)[0]) * 60)
    if len(str(seconds)) == 1:
        seconds = "0" + str(seconds)

    return str(int(minutes)) + ":" + str(seconds)

timestamps = [126459, 268134, 387153]

for time in timestamps:
    print(transform_timestamp(time))
