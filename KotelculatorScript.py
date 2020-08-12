import tkinter as tk

# Colors' constants
Colors = {'BorderCol': '#388C77', 'BgCol': '#4B9985',
          'FgCol': '#A7C7B5', 'YellowCol': '#C5CC04', 'BlackCol': '#000000'}

# Creating main window's widget
Kotel = tk.Tk()

# Constants for storing window's size and position
HEIGHT = 500
WIDTH = 600
# Padding for the window from the screen edges
PADX = 50
PADY = 50
# Window's title
TITLE = 'Kotelculator'
# Path to the icon file
ICONPATH = 'appicon.ico'

# Setting size and position
Kotel.geometry(f'{HEIGHT}x{WIDTH}+{PADX}+{PADY}')
# Setting window's title
Kotel.title(TITLE)
# Fixing size by turning False the window's resizability
Kotel.resizable(False, False)
# Setting window's icon
Kotel.iconbitmap(ICONPATH)
# Setting background color
Kotel.config(bg=Colors['BorderCol'])

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
OutputLabel = tk.Label(MathFrame, height=3, text=OutputString,
                       bg=Colors['FgCol'],
                       fg=Colors['BlackCol'], font='Terminal 16 bold',
                       anchor='e')


# I will use these functions in input buttons----------------------------------
# Adding symbol to the input string
def add_symbol(symbol):
    global MathString
    global MathLabel
    MathString += str(symbol)
    MathLabel.config(text=MathString)


def del_symbol():
    global MathString
    global MathLabel
    del(MathString[len(MathString) - 1])
    MathLabel.config(text=MathString)


def evaluate():
    global OutputString
    global OutputLabel
    x = eval(MathString)
    if x // 1 == 0:
        x = round(x)
    OutputString = str(x)
    OutputLabel.config(text=OutputString)


# Creating nine input buttons--------------------------------------------------

# This is how i wanted to create them
"""
But1 = tk.Button(Kotel, background=Colors['BorderCol'],
                 borderwidth=10, relief='groove', text='1',
                 font='Terminal 44 bold')
But2 = tk.Button(Kotel, background=Colors['BorderCol'],
                 borderwidth=10, relief='groove', text='2',
                 font='Terminal 44 bold')
But3 = tk.Button(Kotel, background=Colors['BorderCol'],
                 borderwidth=10, relief='groove', text='3',
                 font='Terminal 44 bold')
But4 = tk.Button(Kotel, background=Colors['BorderCol'],
                 borderwidth=10, relief='groove', text='4',
                 font='Terminal 44 bold')
But5 = tk.Button(Kotel, background=Colors['BorderCol'],
                 borderwidth=10, relief='groove', text='5',
                 font='Terminal 44 bold')
But6 = tk.Button(Kotel, background=Colors['BorderCol'],
                 borderwidth=10, relief='groove', text='6',
                 font='Terminal 44 bold')
But7 = tk.Button(Kotel, background=Colors['BorderCol'],
                 borderwidth=10, relief='groove', text='7',
                 font='Terminal 44 bold')
But8 = tk.Button(Kotel, background=Colors['BorderCol'],
                 borderwidth=10, relief='groove', text='8',
                 font='Terminal 44 bold')
But9 = tk.Button(Kotel, background=Colors['BorderCol'],
                 borderwidth=10, relief='groove', text='9',
                 font='Terminal 44 bold')
"""
# This is how i created them later
for i in range(1, 10):
    exec(f"""But{i} = tk.Button(Kotel, background=Colors['BgCol'],
        borderwidth=10, relief='groove', text='{i}',
        font='Terminal 44 bold')""")

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
                     borderwidth=10, relief='groove', text='Clear',
                     font='Terminal 25 bold').place(x=10, y=480,
                                                    height=100, width=100)

ButZero = tk.Button(Kotel, background=Colors['BgCol'],
                    borderwidth=10, relief='groove', text='0',
                    font='Terminal 44 bold').place(x=120, y=480,
                                                   height=100, width=100)

ButPower = tk.Button(Kotel, background=Colors['BgCol'],
                     command=lambda: exit(),
                     borderwidth=10, relief='groove', text='OFF',
                     font='Terminal 36 bold').place(x=230, y=480,
                                                    height=100, width=100)

ButEval = tk.Button(Kotel, background=Colors['YellowCol'],
                    command=evaluate,
                    borderwidth=10, relief='groove', text='=',
                    font='Terminal 69 bold').place(x=340, y=480,
                                                   height=100, width=150)
# Fixing commands to each button-----------------------------------------------
for i in range(1, 10):
    eval(f"But{i}.config(command=lambda: add_symbol({i}))")

# Placing widgets using pack()
MathFrame.pack(fill=tk.X, side=tk.TOP)
MathLabel.pack(fill=tk.X, side=tk.TOP)
OutputLabel.pack(fill=tk.X, side=tk.TOP)


# This is how i wanted to place input buttons
"""
But1.place(x=10, y=150, height=100, width=100)
But2.place(x=10, y=150, height=100, width=100)
But3.place(x=10, y=150, height=100, width=100)
But4.place(x=120, y=260, height=100, width=100)
But5.place(x=120, y=260, height=100, width=100)
But6.place(x=120, y=260, height=100, width=100)
But7.place(x=230, y=370, height=100, width=100)
But8.place(x=230, y=370, height=100, width=100)
But9.place(x=230, y=370, height=100, width=100)
"""

# This is how i placed them later

# Placing input buttons using a loop-------------------------------------------
xstart = 10
ystart = 150
for i in range(1, 10):
    eval(f"But{i}.place(x={xstart}, y={ystart}, height=100, width=100)")
    xstart += 110
    i += 1
    if xstart > 230:
        xstart = 10
        ystart += 110

# Starting app's lifecycle loop
Kotel.mainloop()
