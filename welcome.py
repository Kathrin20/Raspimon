from sense_hat import SenseHat
from time import sleep

#below are simple print statments. 
#Any code between quotation marks are considered Strings, or text.

print("Hello! Welcome to the Raspimon training academy.")

#We can import other Python code to help us. Sleep is like a pause in the code.
#Change the value inside the sleep() function call to change the pause amount.
sleep(1) 

print("Let's Start!")

sleep(2)

print("what's your name?")
print("Where do you want to travel?")

#input is used to get text input from a keyboard. We store it as a variable called name
#the \n forces a new line.
name = input("my name is: \n")
place = input ("Where do you want to travel? \n")

sleep(1)

#Use the name in a new print statement. You can combine strings with the + symbol.
print("Nice to meet you, " + name)
print("I want to go to" + place + "too")

sleep(1)

print("I think you are ready to meet your Raspimon in Lab 2.")



 
