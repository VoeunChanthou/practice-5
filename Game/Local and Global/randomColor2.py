import tkinter as tk
from random import choice, randrange

root=tk.Tk()
root.geometry("600x600")
frame=tk.Frame()
frame.master.title("Random color")
canvas=tk.Canvas(frame)

# <---Main program--->
def myTrigger(event):
    # positionx=randrange(0,599)
    # positiony=randrange(0,599)
    randomColor=choice(colors)
    size=randrange(0,300)
    # print(event.x, event.y)
    canvas.create_oval(event.x-size,event.y-size,event.x+size,event.y+size, fill=randomColor)
    # canvas.create_oval(positionx,positiony,positionx+size,positiony+size, fill=randomColor)
    
    
    # <---To start--->
def toStart(event):
    canvas.delete("all")
    canvas.create_text(400,20,text="Down to delete",font="verdana, 30")
    root.bind("<Button-1>", myTrigger)
    
    
    # <---To delete--->
def deleteOval(event):
    canvas.delete("all")
    canvas.create_text(400,20,text="Down to delete",font="verdana, 30")



colors=['#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6', 
      '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
      '#80B300', '#809900', '#E6B3B3', '#6680B3', '#66991A', 
      '#FF99E6', '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC',
      '#66994D', '#B366CC', '#4D8000', '#B33300', '#CC80CC', 
      '#66664D', '#991AFF', '#E666FF', '#4DB3FF', '#1AB399',
      '#E666B3', '#33991A', '#CC9999', '#B3B31A', '#00E680', 
      '#4D8066', '#809980', '#E6FF80', '#1AFF33', '#999933',
      '#FF3380', '#CCCC00', '#66E64D', '#4D80CC', '#9900B3', 
      '#E64D66', '#4DB380', '#FF4D4D', '#99E6E6', '#6666FF']

# <---start--->
root.bind("<Return>", toStart)
ovals=canvas.create_text(200,200,text="Enter to start", font="verdana, 50")

# <---Add oval--->
# root.bind("Button-1",myTrigger)

# <---delete oval-->
root.bind("<Down>", deleteOval)

canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()

