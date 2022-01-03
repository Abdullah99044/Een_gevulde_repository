import tkinter as tk
from tkinter.constants import TRUE, X, Y
window = tk.Tk()

#button = tk.Button(text='...', bg="white", fg="black")
#button.pack(pady = 20, padx = 20 )

# schijf hier tussen je code


x = TRUE
 
def licht_functie_on():
    global window
    global x
    global y
    global button
    
    if x:
        print("Licht is on!")
        window.config(bg="yellow")
        button.config(text="Switch light on")
        x = False
    else:
        print("Licht is of!")
        window.config(bg="black")
        button.config(text="Switch light off")
        x = True

 
 

 
 

 
window.config(bg="black")
button = tk.Button(window , text="Switch light on" , bg="white"   , command=licht_functie_on )
 
button.pack(pady = 20, padx = 20 )


# schijf hier tussen je code

window.mainloop()