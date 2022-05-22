import base64
import os
from appium import webdriver

def compare_b64_images(driver, input_b64):
    ...
    #take an an image as input
    with open(input_b64, "rb") as image_file:
        input_b64 = base64.b64encode(image_file.read())
    #screenshot screen as b64
    screenshot = driver.get_screenshot_as_base64()
    #compare b64 version of image 
    if input_b64 in screenshot:
        return 


def b64_test(input_b64: str):
    with open(input_b64, "rb") as image_file:
        input_b64 = base64.b64encode(image_file.read())
    return input_b64

print(b64_test("eight.png"))


def get_binary(i_value):
    bin_value = []
    if isinstance(i_value, str):
        for i in i_value:
            bin_value.append( bin(ord(i))[2:] )     
    else:
        bin_value.append( bin(i_value)[2:] )
    return bin_value

input_val = input("enter whatever you want: (as long as its either text or a number please)\n")
value = get_binary(input_val)
for item in value:
    print(item)


"""
print( ord("a") )
print( bin(ord("a")) )
print( bin(ord("a"))[2:] )

#print( '{:0b}'.format(bin(ord("a"))))
#print( format(bin(ord("a")), b))   
"""
            