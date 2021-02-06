import cv2 as cv
import numpy as np
from skimage import io
from matplotlib import pyplot as plt
import PIL 
from PIL import Image
import glob

def noiseReduction(img, i):
    dst = cv.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    cv.imwrite(r"C:/Users/tomsw/Documents/Session/Projy/New_images_noise/new_tom"+str(i)+".jpg", dst)
    
    # Afficher l'image
    # plt.subplot(121),plt.imshow(img)
    # plt.subplot(122),plt.imshow(dst)
    # plt.show()

def findCountour(img, i):
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    _, binary = cv.threshold(gray, 90, 255, cv.THRESH_BINARY_INV)
    contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for i in range(len(contours)):
            # cv.drawContours(thresh,findLargestContour(contours),-1,(150,10,255),3)
            if len(contours[i]) >= 5:
                img = cv.drawContours(img,contours,-1,(150,10,255),3)
                # ellipse=cv.fitEllipse(contours[i])
            # else:
            #     img = cv.drawContours(img,contours,-1,(0,0,0),-1)

    cv.imwrite(r"C:/Users/tomsw/Documents/Session/Projy/New_images_cont/new_tom"+str(i)+".jpg", img)

def findLargestContour(contours):
    areas = [cv.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    return contours[max_index]

def main():
    i = 0
    images = [cv.imread(file) for file in glob.glob(r"C:/Users/tomsw/Documents/Session/Projy/Tomates/tomate_12/*.jpg")]
    for image in images:
        noiseReduction(image, i)
        findCountour(image, i)
        i+=1
        break

if __name__ == "__main__":
    main()