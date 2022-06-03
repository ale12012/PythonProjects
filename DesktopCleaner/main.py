import os
import time

os.chdir(r'C:\Users\ale12012\OneDrive - vestfold og telemark fylkeskommune\skrivebord')
folder_list = os.listdir(r'C:\Users\ale12012\OneDrive - vestfold og telemark fylkeskommune\skrivebord')
find = open(r'C:\TopVacuum\Status.txt', "r")
attribchoice = find.readline(1)
print(attribchoice)
find.close()


def hide():
    with open(r'C:\TopVacuum\Status.txt', "w") as finds:
        finds.seek(0)
        finds.write('1')
    with open(r'C:\TopVacuume\Mappenavn.txt', "w") as folders:
        for item in folder_list:
            folders.write(item + "\n")
            os.popen('attrib +h "%s"' % item)
            print('attrib +h %s' % item)


def show():
    with open(r'C:\TopVacuum\Status.txt', "w") as finds:
        finds.seek(0)
        finds.write('0')
    for i in folder_list:
        os.popen('attrib -h "%s"' % i)


if attribchoice == "0":
    hide()

elif attribchoice == "1":
    show()
else:
    print("Not Valid... Exiting")
    time.sleep(3)