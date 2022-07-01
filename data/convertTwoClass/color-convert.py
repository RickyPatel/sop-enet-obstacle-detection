import cv2
import numpy as np
import sys
import imutils

# convert the output of the model such that it has only 3 colors: obstacle, non-obstacle, unlabelled


# masking the colors in "masking_colours" array to "target_colour"
def mask_colours(masking_colours, target_colour, image):
    for mask_colour in masking_colours.values():
        mask=cv2.inRange(image,np.array(mask_colour),np.array(mask_colour))
        image[mask>0]=target_colour


# Load the image
filename = sys.argv[1]
input_folder = sys.argv[2]
output_folder = sys.argv[3]
image = cv2.imread(input_folder+filename)
image =cv2.resize(image, (512, 256))
# cv2.imshow("Input", image)


#Specify the target colours here
red = (0,0,255)
green = (0,255,0)



#making arrays of colour for non-obstacles
#reverse RGB to BGR for applying masking

non_obs_color_dict= {
    'road': [128,64,128],
    'sidewalk': [232,35,244],
    'terrain':  [152,251,152],
    'sky': [180,130,70],
    'ground': [81,0,81],
    'dynamic': [0,74,111],
    'parking': [160,170,250]
}


mask_colours(non_obs_color_dict, green, image)


#making arrays of colour for obstacles
#reverse RGB to BGR for applying masking

obs_color_dict= {
    'Building': [70, 70, 70],
    'Wall': [156,102,102],
    'Fence': [153,153,190],
    'Pole': [153,153,153],
    'TrafficLight': [30,170,250],
    'TrafficSign': [0,220,220],
    'Vegetation': [35,142,107],
    'Person': [60,20,220],
    'Rider': [0,0,255],
    'Car': [142,0,0],
    'Truck': [70,0,0],
    'Bus': [100,60,0],
    'Train':[100,80,0],
    'Motorcycle':[230,0,0],
    'Bicycle':[32,11,119],
    'rail track': [140,150,230],
    'guard rail': [180,165,180],
    'bridge': [100,100,150],
    'tunnel': [90,120,150],
    'carawan': [90,0,0],
    'trailer':[110,0,0],
    'license plate': [142,0,0]
    
}
mask_colours(obs_color_dict, red, image)



#Coloring all other colours as red

# special color which should not be changed
colors = [ (0,0,0), (0,0,255), (0, 255, 0) ]


# all other colors
mask = np.zeros(image.shape[:2], dtype=bool)

for color in colors:   
    mask |= (image == color).all(-1)

image[~mask] = (0,0,255)



#converting to grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Input2", image)
# print(image)



#Creating output images with each pixel labelled to one of the 3 classes 
rows = len(image)
pixels = len(image[0])

for i in range(0,rows):
    for j in range(0, pixels):
        if(image[i][j]==76):
            image[i][j]=1
        elif(image[i][j]==150):
            image[i][j]= 2

# cv2.imshow("Input3", image)
# print(image)

cv2.imwrite(output_folder+filename,image)
# cv2.imwrite(""+filename,image)




cv2.waitKey(0)
