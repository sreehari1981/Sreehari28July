# Programe to calculate area of a Triangle
side1 = float(input('Enter the first side of a triangle: '))
side2 = float(input('Enter the second side of a triangle: '))
side3 = float(input('Enter the third side of a triangle: '))
S = (side1+side2+side3)/2
#Sreehari Triangle
area = (S*(S-side1)*(S-side2)*(S-side3)) ** 0.5
print('The area of the triangle is: ',area)


