import tkinter as tk

# Colors' constants
Colors = {'BorderCol': '#388C77', 'BgCol': '#4B9985',
          'FgCol': '#A7C7B5', 'YellowCol': '#C5CC04', 'BlackCol': '#000000'}

# Creating main window's widget
Kotel = tk.Tk()

# Constants for storing window's size and position
HEIGHT = 500; WIDTH = 600
# Padding for the window from the screen edges
PADX = 50; PADY = 50
# Window's title
TITLE = 'Kotelculator'
# Setting size and position
Kotel.geometry(f'{HEIGHT}x{WIDTH}+{PADX}+{PADY}')
# Setting window's title
Kotel.title(TITLE)
# Fixing size by turning False the window's resizability
Kotel.resizable(False, False)
# Setting background color
Kotel.config(bg=Colors['BorderCol'])

# This variables will help me with configuring my kotelculator
operatorList = ['+', '.', '/', '-', '*']
# After output was show, lockes the input and output
locked = False
# This string will contain user's input
MathString = ''
# This string will contain output
OutputString = ''

# This frame will contain needed labels for output
MathFrame = tk.Frame(Kotel, bg=Colors['BorderCol'],
                     borderwidth=10, relief='groove')

# This label will output users' input
MathLabel = tk.Label(MathFrame, height=3, text=MathString,
                     bg=Colors['FgCol'], fg=Colors['BlackCol'],
                     font='Terminal 16 bold', anchor='e')

# This label will output the result of the MathLabel
OutputLabel = tk.Label(MathFrame, height=3, text='',
                       bg=Colors['FgCol'],
                       fg=Colors['BlackCol'], font='Terminal 16 bold',
                       anchor='e')

# This is decorative label
DecorativeLabel = tk.Label(Kotel, bg=Colors['FgCol'],
                           fg=Colors['BlackCol'], text='BMO',
                           anchor='sw',
                           font='Terminal 16 bold').place(x=5, y=5)


# I will use these functions in input buttons----------------------------------
def updatemath():
    global MathLabel
    global MathString
    MathLabel.config(text=MathString)


# Adding symbol to the input string
def clear():
    global MathString
    global locked
    MathString = ''
    OutputLabel.config(text='')
    locked = False
    updatemath()


def add_symbol(symbol):
    global MathString
    global operatorList
    if str(symbol) == '0' and not locked and MathString != '0':
        MathString += str(symbol)
    if str(symbol) == '0' and locked and MathString != '0':
        clear()
        MathString += str(symbol)
    elif not str(symbol).isdigit() and not locked:
        if MathString[len(MathString) - 1] != ' ' and MathString[len(MathString) - 1] != '.':
            MathString += str(symbol)
    elif str(symbol).isdigit() and not locked and str(symbol) != '0' and MathString != '0':
        MathString += str(symbol)
    elif str(symbol).isdigit() and locked and str(symbol) != '0':
        clear()
        MathString += str(symbol)
    updatemath()


def del_symbol():
    global MathString
    global locked
    if not locked:
        if MathString[len(MathString) - 1] != ' ':
            MathString = MathString[: len(MathString) - 1]
        else:
            MathString = MathString[: len(MathString) - 3]
    updatemath()


def evaluate():
    global OutputLabel
    global locked
    global MathString
    if len(MathString) > 0:
        try:
            s = eval(MathString)
            if type(s) == float and s % 1 == 0:
                s = round(s)
            OutputLabel.config(text=str(s))
        except ZeroDivisionError:
            OutputLabel.config(text='Error: dividing by zero')
        finally:
            locked = True


# Creating nine input buttons--------------------------------------------------
for i in range(1, 10):
    exec(f"""But{i} = tk.Button(Kotel, background=Colors['BgCol'],
        borderwidth=10, relief='groove', text='{i}',
        font='Terminal 44 bold', command=lambda: add_symbol({i}))""")

# Also creating +, -, *, / buttons and delete button, clear button
ButPlus = tk.Button(Kotel, background=Colors['BgCol'],
                    command=lambda: add_symbol(' + '),
                    borderwidth=10, relief='groove', text='+',
                    font='Terminal 69 bold').place(x=340, y=260,
                                                   height=100, width=70)

ButDot = tk.Button(Kotel, background=Colors['BgCol'],
                   command=lambda: add_symbol('.'),
                   borderwidth=10, relief='groove', text='.',
                   font='Terminal 69 bold').place(x=340, y=370,
                                                  height=100, width=70)

ButMinus = tk.Button(Kotel, background=Colors['BgCol'],
                     command=lambda: add_symbol(' - '),
                     borderwidth=10, relief='groove', text='-',
                     font='Terminal 44 bold').place(x=340, y=150,
                                                    height=100, width=70)

ButDivide = tk.Button(Kotel, background=Colors['BgCol'],
                      command=lambda: add_symbol(' / '),
                      borderwidth=10, relief='groove', text='/',
                      font='Terminal 44 bold').place(x=420, y=260,
                                                     height=100, width=70)

ButMult = tk.Button(Kotel, background=Colors['BgCol'],
                    command=lambda: add_symbol(' * '),
                    borderwidth=10, relief='groove', text='*',
                    font='Terminal 44 bold').place(x=420, y=370,
                                                   height=100, width=70)

ButDel = tk.Button(Kotel, background=Colors['BgCol'],
                   command=lambda: del_symbol(),
                   borderwidth=10, relief='groove', text='<-',
                   font='Terminal 36 bold').place(x=420, y=150,
                                                  height=100, width=70)

ButClear = tk.Button(Kotel, background=Colors['YellowCol'],
                     command=clear,
                     borderwidth=10, relief='groove', text='Clear',
                     font='Terminal 25 bold').place(x=10, y=480,
                                                    height=100, width=100)

ButZero = tk.Button(Kotel, background=Colors['BgCol'],
                    command=lambda: add_symbol('0'),
                    borderwidth=10, relief='groove', text='0',
                    font='Terminal 44 bold').place(x=120, y=480,
                                                   height=100, width=100)

ButPower = tk.Button(Kotel, background=Colors['BgCol'],
                     command=lambda: Kotel.destroy(),
                     borderwidth=10, relief='groove', text='OFF',
                     font='Terminal 36 bold').place(x=230, y=480,
                                                    height=100, width=100)

ButEval = tk.Button(Kotel, background=Colors['YellowCol'],
                    command=evaluate,
                    borderwidth=10, relief='groove', text='=',
                    font='Terminal 69 bold').place(x=340, y=480,
                                                   height=100, width=150)

# Placing widgets using pack()
MathFrame.pack(fill=tk.X, side=tk.TOP)
MathLabel.pack(fill=tk.X, side=tk.TOP)
OutputLabel.pack(fill=tk.X, side=tk.TOP)

# Placing input buttons using a loop-------------------------------------------
xstart = 10
ystart = 150
for i in range(1, 10):
    eval(f"But{i}.place(x={xstart}, y={ystart}, height=100, width=100)")
    xstart += 110
    if xstart > 230:
        xstart = 10
        ystart += 110

# Starting app's lifecycle loop
Kotel.mainloop()