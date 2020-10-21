__author__ = 'Souvik'

from PIL import ImageGrab

def grab_snap(name = 0):

    try:
        name = str(name) + '.jpg'
        img = ImageGrab.grab(bbox= None)
        img.save(name)
    except:
        print("ERROR : Screen-shot not taken")

if __name__ == '__main__':
    pass
