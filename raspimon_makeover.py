from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#makeover time! Here is a Python list. It holds  collection of string values.

names = ["Codey" , "Galbert" , "Freedy", "Voltria" , "Kat-Kat" , "Isa" , "Annie" ]

names.append("Lizardia")

sense.show_message(names[1])

#Colors:

r = (255, 0, 0 ) # RED color, stored in an another data structure called a tuple.
k = (0, 0, 0) # black means zero amounts of red, green and blue
g = (0,255,0)
p = (128,0,128)
b = (0,0,255)

#define another color. Use one letter variable names to make it easy later
heart = [
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b
]


raspimon = [
k, k, k, k, k, k, k, k,
k, r, r, r, r, r, r, k,
k, r, k, k, k, k, r, k,
k, r, r, k, r, k, r, k,
k, r, k, k, k, k, r, k,
k, r, r, r, r, r, r, k,
k, k, r, k, r, k, k, k,
k, k, r, k, r, k, k, k
]
 
sense.set_pixels(heart)

#add a one-pixel mouth
sense.set_pixel(3,4, [255,0,0])
sense.set_pixel(3,3, [255,0,0])
sense.set_pixel(3,2, [255,0,0])
sense.set_pixel(4,3, [255,0,0])
sense.set_pixel(1,2, [255,0,0])
sense.set_pixel(2,2, [0,0,0])
sense.set_pixel(4,2, [0,0,0])
sense.set_pixel(3,4, [255,0,0])
sense.set_pixel(3,3, [255,0,0])
sense.set_pixel(3,2, [255,0,0])
sense.set_pixel(2,3, [255,0,0])
sense.set_pixel(2,1, [255,0,0])
sense.set_pixel(5,2, [255,0,0])
sense.set_pixel(4,1, [255,0,0])


