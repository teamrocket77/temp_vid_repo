import cv2
import numpy as np
import sklearn.cluster
from collections import Counter
from PIL import Image
from os import mkdir, chdir, getcwd
from datetime import datetime

#please note program is a little slow due to the importing of the files 
#remember to divide up the files and export tuple as a text file that way the same test doesn't take a long time

'''The function create takes a picture and an amount of colors that you want to detect and returns a tuple'''
#FileName is the name of the file in the folder
def create(fileName, color_codes):
    print("Getting colors")
    image = cv2.imread(fileName)
    image =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    modified_image = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)
    number_of_colors = color_codes
    clf = sklearn.cluster.KMeans(number_of_colors)
    labels = clf.fit_predict(modified_image)
    counts = Counter(labels)
    center_color = clf.cluster_centers_
    ordered_colors = [center_color[i] for i in counts.keys()]
    print("Returning Colors")
    return ordered_colors



#edited_pics creates an 1080px1920p image -> pastes the orginal image and fills in whatever part of the picture that was blank with one of the primary colors 
def edited_pics(imageName,color_list):
    im1 = Image.open(imageName)
    print("image is open now")

    day = datetime.now()
    year = day.strftime('_%Y')
    month = day.strftime('%m')
    day = day.strftime("%d")


    dayAndName = imageName+year+month+day
    mkdir(dayAndName)
    print("Directory has been made")

    chdir(getcwd()+'\\'+dayAndName)
    print("Directory has been changed")



    oWidth, oheight = im1.size
    dimw = int((1920-oWidth)/2)
    dimh = int((1024-oheight)/2)

    someCounter =len(color_list)


    for i in range(len(color_list)):
        print("Creating images")
        im = Image.new(mode='RGB',size =(1920, 1080), color =tuple(l[i]))
        im.paste(im1, (dimw,dimh))
        print('Attempting to save image no'+str(i+1))
        im.save(str(i)+'.jpg')

    #this makes a standard black and white image
    im = Image.new(mode="RGB", size=(1920, 1080))
    im.paste(im1, (dimw,dimh))
    print("attempting to save image number "+ str(i+2))
    im.save(str(someCounter)+'.jpg')


    #this converts the image to black and white
    im1 = im1.convert('1')
    im.paste(im1,(dimw, dimh))
    im.save(str(someCounter+1)+'.jpg')
    print("Attempting to Save the final image")

    



l = create("first.jpg", 3)
l  = np.round(l)
l = l.astype(int)
edited_pics('first.jpg',l)
