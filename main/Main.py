from datetime import datetime

import glob2

a = []


def writer(c):
    date = datetime.now()
    name = date.strftime("%Y-%m-%d")
    with open(name + ".txt", "w") as newfile:
        for i in c:
            newfile.write(str(i) + "\n")


def get_content():
    for file in glob2.glob("file*.txt"):
        with open(file) as myfile:
            a.append(myfile.readlines())


get_content()
writer(a)
