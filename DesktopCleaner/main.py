import os

programFiles = os.environ['PROGRAMFILES']
workingPath = programFiles + "\DesktopCleaner"
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# get the contents of status.txt in the current directory
def get_status():
    with open(f"{workingPath}\status.txt", "r") as f:
        status = f.readline()
        f.close()
    return status


#define a function to get all files in the current directory uing os module
def get_files():
    files = os.listdir(desktop)
    return files


def change_status():
    status = get_status()
    
    with open(f"{workingPath}\status.txt", "w") as f:
        if status == "0":
            f.writelines("1")
            f.close()
        else:
            f.writelines("0")
            f.close()

def get_status():
    with open(f"{workingPath}\status.txt", "r") as f:
        status = f.readline()
        f.close()
    return status

def write_files():
    files = get_files()
    with open(workingPath + R"\\files.txt", "w") as f:
        for file in files:
            f.writelines(file + "\n")
        f.close()

def hide_files():
    files = get_files()
    for i in files:
        os.popen(f'attrib +h "{desktop}\{i}"')
    write_files()

def show_files():
    files = get_files()
    for i in files:
        os.popen(f'attrib -h "{desktop}\{i}"')


if __name__ == "__main__":
    status = get_status()
    if status == "0":
        hide_files()
        change_status()
    elif status == "1":
        show_files()
        change_status()
    else:
        print("error")