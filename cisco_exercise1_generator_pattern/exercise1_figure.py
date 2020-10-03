from tkinter import Canvas, Tk

mywindow = Tk()
mycanvas = Canvas(mywindow, width=400, height=400, background='white')
mycanvas.grid(row=0, column=0)

# big triangle
mycanvas.create_line(100, 300, 300, 300, fill='black')
mycanvas.create_line(100, 300, 200, 100, fill='black')
mycanvas.create_line(200, 100, 300, 300, fill='black')

# top small triangle
mycanvas.create_line(180, 120, 220, 120, fill='black')
mycanvas.create_line(180, 120, 200, 80, fill='black')
mycanvas.create_line(200, 80, 220, 120, fill='black')

# right small triangle
mycanvas.create_line(300, 280, 320, 320, fill='black')
mycanvas.create_line(300, 280, 280, 320, fill='black')
mycanvas.create_line(280, 320, 320, 320, fill='black')

# left small triangle
mycanvas.create_line(100, 280, 120, 320, fill='black')
mycanvas.create_line(100, 280, 80, 320, fill='black')
mycanvas.create_line(80, 320, 120, 320, fill='black')

mywindow.mainloop()
