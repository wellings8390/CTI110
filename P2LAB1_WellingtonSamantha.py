 # Samantha Wellington  
 # 03/25/2025
 # P2LAB1
 # Given the radius as user input, return various dimensions of a circle as outputs

import math

#collect radius 
radius = float(input('What is your radius? '))

#calculate diameter 2r
diameter = 2*radius

#calculate circumfrence 2pi*r
circumfrence = 2*math.pi*radius

#calculate area pi*r*r
area = math.pi*radius*radius

print('The diameter of your circle is', f'{diameter:.1f}')
print('The circumfrence of your circle is', f'{circumfrence:.2f}')
print('The area of your circle is', f'{area:.3f}')