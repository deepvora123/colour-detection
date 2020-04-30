# made a simpe colour picker using opencv, numpy, pandas and argparse.

import cv2
import numpy as np
import pandas as pd
import argparse

ap = argparse.ArgumentParser()
# Using argparse is how you let the user of your program provide values for variables at runtime.

ap.add_argument('-i', '--image', required=True, help="Image Path")
# Here we define a method to run our program through the command promt.

args = vars(ap.parse_args())
img_path = args['image']

img = cv2.imread(img_path)
# cv2.imread() method loads an image from the specified file.

clicked = False
r = g = b = xpos = ypos = 0

index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)
# names assigns new column heading names.
# header=None is used to trim column names is already exists in CSV file.

def getColorName(R,G,B):
    minimum = 10000
    
    # we iterate through all the 800+ colour names available in the .csv file.
    for i in range(len(csv)): 
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        
        # we find the most accurate colour by comparison method.
        if(d<=minimum):
            minimum = d 
            cname = csv.loc[i,"color_name"]
    return cname 


def draw_function(event, x,y,flags,param):
    # since here we are only detecting the value of r,g,r, this draw function doesnt actually draw anything using csv.rect/circle/line.
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
       

cv2.namedWindow('image')
    # naming the window which opens with the input image as 'image'.
cv2.setMouseCallback('image',draw_function)
    # integrating the mouse and draw_function.

while(1):
    cv2.imshow("image",img)
    if (clicked):
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
        text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False
  
    if cv2.waitKey(20) & 0xFF ==27:
        break
    
cv2.destroyAllWindows()

#time required to learn the above imported extensions as much required for this project = 6 days.
#time required to implement this project = 2 days

