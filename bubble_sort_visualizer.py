from tkinter import *
from tkinter import ttk
import random
import time

main_window = Tk()
main_window.title("SORTING ALGORITHM VISUALIZATION")
main_window.geometry('1200x700')
main_window.maxsize(1500, 900)
main_window.config(bg='light blue')

my_list = []
data = []

def drawData(data, color):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))
    final_window.update_idletasks()

def bubbleSort(data, drawData, timeTrick):
    for _ in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                drawData(data, ["black" if x == j or x == j + 1 else "pink" for x in range(len(data))])
                time.sleep(timeTrick)
    drawData(data, ["black" for x in range(len(data))])

def StartAlgorithm():
    global data
    bubbleSort(data, drawData, speedScale.get())

def Generate():
    global data
    data.clear()
    try:
        xx = int(sizeEntry.get())
    except:
        return
    for i in range(xx):
        try:
            data.append(float(my_list[i].get()))
        except:
            data.append(0)
    drawData(data, ['light blue' for _ in range(len(data))])

def close():
    main_window.destroy()
    final_window.destroy()

def Input():
    global my_list
    my_list.clear()
    try:
        xx = int(sizeEntry.get())
    except:
        return
    Label(main_window, text="Fill the elements of the array in these boxes:", bg='grey',
          font=('Times New Roman', 15, 'bold')).grid(row=3, column=0, padx=550, pady=5, sticky=W)
    global UI_frame2
    UI_frame2 = Frame(main_window, width=500, height=200, bg='grey')
    UI_frame2.grid(row=4, column=0, padx=5, pady=5, columnspan=5)
    r = 4
    c = 0
    for widget in UI_frame2.winfo_children():
        widget.destroy()
    for x in range(xx):
        if x % 10 == 0:
            r += 1
            c = 0
        my_entry = Entry(UI_frame2, width=5)
        my_entry.grid(row=r, column=c, padx=5, pady=5, sticky=W)
        my_list.append(my_entry)
        c += 1
    Button(UI_frame2, text="Add", command=Generate).grid(row=r + 1, column=0, pady=5)

Label(main_window, text="BUBBLE SORT VISUALIZER", bg='grey',
      font=('Times New Roman', 25, 'bold')).grid(row=0, padx=500, pady=100, sticky=W)

main_frame = Frame(main_window, width=500, height=200, bg='grey')
main_frame.grid(row=2, column=0, padx=50, pady=5)

Label(main_frame, text="Enter the size of the array:", bg='grey',
      font=('Times New Roman', 20, 'bold')).grid(row=0, column=0, padx=5, pady=30, columnspan=5)

sizeEntry = Entry(main_frame)
sizeEntry.grid(row=2, column=1, padx=5, pady=5, columnspan=3)

Button(main_frame, text="Submit", command=Input, bg='light blue').grid(row=2, column=4, padx=5, pady=5)

final_window = Tk()
final_window.title("SORTING ALGORITHM VISUALIZATION")
final_window.geometry("1200x700")
final_window.maxsize(1500, 900)
final_window.config(bg="pink")

UI_frame = Frame(final_window, width=200, height=200, bg="black")
UI_frame.grid(row=3, column=0, padx=200, pady=5)

speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2,
                   resolution=0.2, orient=HORIZONTAL, bg='pink', label="SET SPEED: ")
speedScale.grid(row=1, column=0, padx=5, pady=5, columnspan=4)

Button(UI_frame, text="START", command=StartAlgorithm, bg="light blue").grid(row=1, column=4, padx=5, pady=5)
Button(UI_frame, text="END", command=close, bg="light blue").grid(row=1, column=5, padx=5, pady=5)

canvas = Canvas(final_window, width=1000, height=380, bg='pink')
canvas.grid(row=1, column=0, padx=200, pady=5, columnspan=5)

main_window.mainloop()
