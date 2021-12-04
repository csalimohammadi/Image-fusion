


import os, sys, os.path
import cv2
from glob import glob                                                           
import shutil
import numpy as np
from converter import HSI2RGB
from converter import RGB2HSI



images = glob('E:/article_covid19/Python-RGB-to- LAB-master/cvd-G8-T10-fused-lab-hsv-new/test/NORMAL/*.jpg', recursive=True)

for j in images:
    img = cv2.imread(j)

    #-----Converting image to HSV Color model-----------------------------------
    hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #-----Converting image to LAB Color model-----------------------------------
    lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    # fuse original hsv with orginal lab
    fused_org_lab_hsv = cv2.add(lab, hsv)


    #-----Splitting the LAB image to different channels-------------------------
    l, a, b = cv2.split(lab)
    #-----Applying CLAHE to L-channel-------------------------------------------
    clahe = cv2.createCLAHE(clipLimit=10, tileGridSize=(8,8))
    cl = clahe.apply(l)

    #Fuse result of equalized L with original L
    fuse_LAB = cv2.addWeighted(l,0.5,cl,0.5,0)
    #-----Merge the CLAHE-enhanced L*2 with a and b -----------
    limg = cv2.merge((fuse_LAB,a,b))


    fused = cv2.add(limg, fused_org_lab_hsv)


    #final
    final = cv2.cvtColor(fused, cv2.COLOR_LAB2BGR)
    cv2.imwrite( str( j[:-3]) + '.jpeg', final)

   
    
# Remove all originals
import glob
directory='E:/article_covid19/Python-RGB-to- LAB-master/cvd-G8-T10-fused-lab-hsv-new/test/NORMAL'
os.chdir(directory)
files=glob.glob('*.jpg')
for filename in files:
    os.unlink(filename)


