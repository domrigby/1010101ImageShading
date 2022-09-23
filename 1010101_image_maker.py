import cv2 

img = cv2.imread("pricey2.JPG")

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

resized = cv2.resize(grayscale, (200,200), interpolation = cv2.INTER_AREA)

with open("pricey2.txt","w") as f:
    for line in resized :
        for pixel in line :
            if pixel > 110:
                f.write("1")
            else :
                f.write("0")
        f.write("\n")
