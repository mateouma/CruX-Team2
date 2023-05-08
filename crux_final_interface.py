#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
import random

# Function to toggle square color
def toggle_color(canvas,label,speed):
    current_color = canvas.cget("bg")
    if current_color == "gray":
        canvas.configure(bg="white")
        label.configure(bg="white")
    else:
        canvas.configure(bg="gray")
        label.configure(bg="gray")
    gui.after(speed, lambda: toggle_color(canvas, label, speed))  # Call toggle_color after specified speed

gui = tk.Tk(className='Python Examples - Window Color')
gui.title("Team 2")
gui.attributes('-fullscreen', True)
gui.configure(bg='black')

# Create the squares
square1 = tk.Canvas(gui, width=250, height=250, bg="gray")
square2 = tk.Canvas(gui, width=250, height=250, bg="gray")
square3 = tk.Canvas(gui, width=250, height=250, bg="gray")
square4 = tk.Canvas(gui, width=250, height=250, bg="gray")
square5 = tk.Canvas(gui, width=250, height=250, bg="gray")

# Create labels for the squares
label1 = tk.Label(square1, text="FWD", bg="gray", fg="#3b61d6", font=("Arial", 20))
label2 = tk.Label(square2, text="REV", bg="gray", fg="#3b61d6", font=("Arial", 20))
label3 = tk.Label(square3, text="LEFT", bg="gray", fg="#3b61d6", font=("Arial", 20))
label4 = tk.Label(square4, text="RIGHT", bg="gray", fg="#3b61d6", font=("Arial", 20))
label5 = tk.Label(square5, text="STOP", bg="gray", fg="#3b61d6", font=("Arial", 20))

# Pack the labels in the center of the squares
label1.place(relx=0.5, rely=0.5, anchor="center")
label2.place(relx=0.5, rely=0.5, anchor="center")
label3.place(relx=0.5, rely=0.5, anchor="center")
label4.place(relx=0.5, rely=0.5, anchor="center")
label5.place(relx=0.5, rely=0.5, anchor="center")

# Pack the squares in the appropriate order
square1.pack(side="top")
square2.pack(side="bottom")
square3.pack(side="left")
square4.pack(side="right")
square5.place(relx=0.5, rely=0.5, anchor="center")

# Call toggle_color function for each square with different speeds
toggle_color(square1, label1, 143) 
toggle_color(square2, label2,111)  
toggle_color(square3, label3,91)  
toggle_color(square4, label4,77)  
toggle_color(square5, label5,59) 



# Create the decoded direction label
decoded_label = tk.Label(gui, text="Decoded Direction: ", bg="black", fg="white", font=("Arial", 16))

# Place the decoded label at the bottom right of the screen
decoded_label.place(relx=1.0, rely=1.0, anchor="se")


gui.mainloop()


# In[ ]:





# In[ ]:




