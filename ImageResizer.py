from PIL import Image
import os
import math

loaddirname = "C:/u/PyScripts/img2resize/"

savedirname= loaddirname + "resized/"
if not os.path.exists(savedirname):
    os.makedirs(savedirname)
maxw = 1600
maxh = 1600


def resizethat(im):
        print("processing", filename)
        
        inw, inh = im.size

        #ruza's sweet solution
        #take the smaller of two possible scale factors
        scalefactor = min(maxw / float(inw), maxh / float(inh))

        outw = int(inw * scalefactor)
        outh = int(inh * scalefactor)
        
        #this may call for the image to be made bigger
        #which is going to be ugly so warn human and antialias
        if scalefactor > 1:
            print("low res on", filename, im.size)
            out = im.resize((outw, outh), Image.ANTIALIAS)
        else:
            out = im.resize((outw, outh), Image.ANTIALIAS)

        #save that file
        newname, ext = os.path.splitext(filename)
        out.save(savedirname + newname + ".jpg")


#main loop

for filename in os.listdir(loaddirname):
    try:
        im = Image.open(loaddirname + filename)
        resizethat(im)
    except IOError:
        print ("failed", str(filename))
        