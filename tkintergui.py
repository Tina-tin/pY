from tkinter import *


def action():
    try:
        s1 = float(scoresField1.get())
        s2 = float(scoresField2.get())
        g1 = float(goalsField1.get())
        g2 = float(goalsField2.get())
    except ValueError as e:
        result.insert(0, 'Invalid typees')

    result.delete(0, 300)

    if s1 > s2:
        result.insert(0, 'Team 1 proceeds to next match')
    elif s2 > s1:
        result.insert(0, 'Team 2 proceeds to next match')
    else:
        if g1 > g2:
            result.insert(0, 'Team 1 proceeds to next match')
        elif g2 > g1:
            result.insert(0, 'Team 2 proceeds to next match')
        else:
            result.insert(0, 'Polnoe Bezobrazie')


master = Tk()

master.config(background='gray')
master.title('Tkinter Practice')
master.geometry('1000x600')

# scores
scoresLabel1 = Label(master, text='Team 1 score', background='gray')
scoresLabel1.place(x=50, y=90)
scoresField1 = Entry(master, background='white', width=30)
scoresField1.place(x=50, y=120)

scoresLabel2 = Label(master, text='Team 2 score', background='gray')
scoresLabel2.place(x=350, y=90)
scoresField2 = Entry(master, background='white', width=30)
scoresField2.place(x=350, y=120)

# goals
goalsLabel1 = Label(master, text='Team 1 goals', background='gray')
goalsLabel1.place(x=50, y=190)
goalsField1 = Entry(master, background='white', width=30)
goalsField1.place(x=50, y=210)

goalsLabel2 = Label(master, text='Team 2 goals', background='gray')
goalsLabel2.place(x=350, y=190)
goalsField2 = Entry(master, background='white', width=30)
goalsField2.place(x=350, y=210)

# actions

btn = Button(master, text='click', command=action)
btn.place(x=200, y=280)
result = Entry(master)
result.place(x=200, y=310)
master.mainloop()