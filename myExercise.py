import sys

with open(sys.argv[1]) as data: dict, list = {}, [i.split(":") for i in data.read().splitlines()]

for j in list: dict[j[0]]=str(j[1])

for k in sys.argv[2].split(","):
    try:
        uni = dict[k]
        print("Name:" + str(k) + ", University:" + str(uni))
    except:
        print("No record of '{}' was found!".format(k))


