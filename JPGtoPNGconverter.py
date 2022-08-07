import sys
import os
from PIL import Image

def run():
    if len(sys.argv) == 3:            # check correct input
        # The full path of the current dir > str
        curpath = os.path.dirname(__file__) + "\\"
        source = sys.argv[1]          # name of the pokemon dir
        newDirectory = sys.argv[2]    # name of the new dir to create
        try:
            os.makedirs(curpath + newDirectory)     # create new folder
            print(f"{newDirectory[:-1]} created succesfuly")
            loopDirectory(curpath + source, curpath + newDirectory)   # start looping with full paths
            print('all done!')
        except OSError:               # if makedirs fails
            print("folder already exists")
    else:
        print(f"{sys.argv[0]} requires 2 args to run")

def loopDirectory(source, newDirectory):
    for file in os.listdir(source):
        clean_name = os.path.splitext(file)[0]
        ext = os.path.splitext(file)[1]
        if ext == '.jpg':     # run only if the file is a .jpg image
            try:
                img = Image.open(source + file)
                img.save(newDirectory + clean_name + '.png', 'png')          
            except:
                print("somthing went wrong")

if __name__ == "__main__":
    run()