
# Import module 
from tkinter import *

# Create object 
root = Tk() 

# Adjust size 
root.geometry( "500x500" ) 

# Change the label text 
def show(): 
	label.config( text = clicked.get() ) 

# Dropdown menu options 
options = [ 
	"Transportation",
    "Package Tours",
    "Cruises",
    "Flight Ticket",
    'Trekking Service',
    "Guide Service"   
] 

# datatype of menu text 
clicked = StringVar() 

# initial menu text 
clicked.set( "Please select your Purpose of travel" ) 

# Create Dropdown menu 
drop = OptionMenu( root , clicked , *options ) 
drop.pack() 

# Create Label 
label = Label( root , text = " " ) 
label.pack() 

# Execute tkinter 
root.mainloop() 











