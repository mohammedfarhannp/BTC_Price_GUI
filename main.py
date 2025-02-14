# Import Section
## Importing neccessory components from modules.
from tkinter import Tk, PhotoImage, Label, Text, DISABLED, NORMAL, END, Button
from requests import get

# Variables
## Window Variables
Geometry = "400x300"
Title = "BTC Price Tracker"

## Image Paths
Logo = "imgs\Icon.ico" # Path
Image_Path = "imgs\Icon.png" # Path

## URL for bitcoin price
URL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'

# Functions
## Function to update the output field with current bitcoin price
def Update():
    Field_Data = "NAN"
    try:
        Response = get(URL)
        if str(Response.status_code) == "429":
            raise Exception
        
        Data = Response.json()
        Bitcoin_Price = Data['bitcoin']['usd']
        Field_Data = f"${Bitcoin_Price}"
    
    except Exception as Error:
        print("Try Again Later!!")
    
    Output_Field.config(state=NORMAL)
    Output_Field.delete('1.0', END)
    Output_Field.insert(END, Field_Data)
    Output_Field.config(state=DISABLED)

# Main
## Window Creation
window = Tk()
window.geometry(Geometry)
window.title(Title)
window.resizable(False, False)
window.iconbitmap(Logo)

## Creating Image Object
Image_Object = PhotoImage(file=Image_Path)

## Bitcoin Image
Bitcoin_Image = Label(window, image=Image_Object, width=100)
Bitcoin_Image.place(x=150,y=0)

## Output Field for showing bitcoin price
Output_Field = Text(window, bd=5, relief="ridge", width=30, height=2, font=('calibri', 12))
Output_Field.config(state=DISABLED)
Output_Field.place(x=75,y=130)

## Getting the bitcoin price int the output field
Update()

## Creating an update button
Refresh_Button = Button(window, text="Update", fg="white", bg="green", command=Update)
Refresh_Button.place(x=180, y=200)

# Loop
window.mainloop()