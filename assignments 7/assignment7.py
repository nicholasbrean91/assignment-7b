import ui
from enum import *

#possible shape information 


def circle(sender):
    #input
    radius = int(view['radius_textfield'].text)
    
    #calcualte circumfrence
    area = 2*3.14*radius**2
    
    if area < 0:
        view['output_label'].text = 'The area is: ' + str(area)
    else:
        view['output_label'].text = 'the numbers inputed are invaild'
        
    view['output_label'].text = 'The area is: ' + str(area)

def triangle(sender):
    #input
    height = int(view['height_textfield'].text)
    base = int(view['base_textfield'].text)
    
    #area
    area = (base * height)
    
    if area < 0:
        view['output_label'].text = 'The area is: ' + str(area)
    else:
        view['output_label'].text = 'the numbers inputed are invaild'

def square(sender):
    #input
    height = int(view['height_textfield'].text)
    base = int(view['base_textfield'].text)
    
    #calculating the area
    
    area = height * base
    
    if area < 0:
        view['output_label'].text = 'The area is: ' + str(area)
    else:
        view['output_label'].text = 'the numbers inputed are invaild'
    
    #return values here
    view['output_label'].text = 'The area is: ' + str(area)
    
    
    

view = ui.load_view()
view.present('sheet')
