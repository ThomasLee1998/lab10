##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()


# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)


# my house with my roof
house = drawpad.create_rectangle(300,300,400,400)
roof1 = drawpad.create_line(300,300,350,200)
roof2 = drawpad.create_line(400,300,350,200)
#windows+door
window=drawpad.create_rectangle(310,310,340,340)
window2=drawpad.create_rectangle(360,310,390,340)
door= drawpad.create_rectangle(340,360,360,400)
door
root.mainloop()
