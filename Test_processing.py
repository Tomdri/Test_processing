import cv2 as cv
import numpy as np
import PIL
import glob
from skimage import io
from matplotlib import pyplot as plt
from PIL import Image

def findContour(img, j):
    cimg = img.copy()
    finalimg = img.copy()
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.medianBlur(img, 5)
    circles = cv.HoughCircles(image=img, method=cv.HOUGH_GRADIENT_ALT, dp=0.9, 
                            minDist=1, param1=40, param2=0.1, minRadius= 100, maxRadius=175)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            centerX = i[0]
            centerY = i[1]
            radius = i[2]
            # Draw circle around tomato
            cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
            # Draw center of tomato
            cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
            # cropTomato(finalimg, centerX, centerY, radius, j)

    cv.imwrite(r"C:/Users/tomsw/Documents/Session/Test_processing/Processed_tom/new_tom"+str(j)+".jpg", cimg)

def cropTomato(img, x, y, r, j):
    crop_img = img[y-r:y+r, x-r:x+r]
    cv.imwrite(r"C:/Users/tomsw/Documents/Session/Test_processing/Processed_tom/new_tom"+str(j)+".jpg", crop_img)


def main():
    j = 0
    images = [cv.imread(file) for file in glob.glob(r"C:/Users/tomsw/Documents/Session/Test_processing/Tomates/tomate_12/*.jpg")]
    for image in images:
        findContour(image, j)
        j+=1
        # break

if __name__ == "__main__":
    main()