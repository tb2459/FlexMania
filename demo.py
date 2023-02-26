import Flexmania

#This is a basic example of giving x,y coordinates for the matrix LED and then applying a certain level of intensity for that particular LED 
x = int(input("Which x coordinate would you like to choose?"))
y = int(input("Which x coordinate would you like to choose?"))
intensity = int(input("Choose a light intensity ranging from 0 and 255?"))
Flexmania.setupLEDMatrix(x,y,intensity)
