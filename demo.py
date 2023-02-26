import Flexmania

#This is a basic example of giving x,y coordinates for the matrix LED and then applying a certain level of intensity for that particular LED 
x = int(input("Which x coordinate would you like to choose?"))
y = int(input("Which x coordinate would you like to choose?"))
intensity = int(input("Choose a light intensity ranging from 0 and 255?"))
Flexmania.setupLEDMatrix(x,y,intensity)


#This is an example of the data that can be gathered from the MPU6050 which would be used to determine the position of the device
axis = str(input("Select an axis x, y, or z."))
Flexmania.setupMPU6050(axis)
