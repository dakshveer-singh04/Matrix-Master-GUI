import tkinter as tk

class instructionWindow:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)
        self.root._offsetx = 0
        self.root._offsety = 0

        self.create_canvas()
        self.create_labels()
        self.create_frame()

        self.bind_events()

    def create_canvas(self):
        self.canvas = tk.Canvas(self.root, height=200, width=800)
        self.canvas.config(bg='blue', width=500, height=150)
        self.canvas.create_arc(10, 10, 150, 150, start=45, extent=260, fill="Red", outline="yellow", width=2)
        self.canvas.grid(row=0, column=0, columnspan=6, sticky=tk.EW)

    def create_labels(self):
        self.label1 = tk.Label(self.root, text="Hello", bg="Yellow", width=10)
        self.label1.grid(row=1, column=0, sticky=tk.NS, rowspan=15)

        self.label2 = tk.Label(self.root, text="Hello", bg="Orange", fg="White", width=10)
        self.label2.grid(row=1, column=5, sticky=tk.NS, rowspan=15)

        self.label3 = tk.Label(self.root, text="Welcome to Details Page", bg="Red", height=7)
        self.label3.grid(row=1, column=1, columnspan=4, sticky=tk.EW)

        self.label4 = tk.Label(self.root, text="All rights reserved", bg="Black", fg='white')
        self.label4.grid(row=15, column=1, columnspan=4, sticky=tk.EW)

        self.label5 = tk.Label(self.root, bg='light blue', text="Instructions Page")
        self.label5.grid(row=2, column=1, columnspan=4, sticky=tk.EW)

        tk.Label(self.root).grid(row=3, column=1)

    def create_frame(self):
        self.frame = tk.Frame(self.root)
        instructions = [
            'Trying to present conspectus of instructions',
            'for further information contact us.',
            '1: Order is to be entered like (m x n)',
            '2: You can either press enter or press Refresh to generate matrix',
            '3: For defaults and scalar factor press enter (twice for confirmation) to lock values',
            '4: For moving in one box just use arrow keys',
            '5: For moving focus to a nearby box, use Shift + respective arrow key'
        ]
        for i, instruction in enumerate(instructions):
            label = tk.Label(self.frame, text=instruction, bg='ivory2')
            label.grid(row=i, sticky=tk.W)

        self.label6 = tk.Label(self.frame, text='To all esteemed, feel free to mail me for suggestion or faults on', bg='ivory2')
        self.label6.grid(row=len(instructions), sticky=tk.W)

        self.label7 = tk.Label(self.frame, text='       dakshveersinghchauhan@gmail.com', bg='ivory3')
        self.label7.grid(row=len(instructions) + 1)

        self.label8 = tk.Label(self.frame, text='', bg='ivory2')
        self.label8.grid(row=len(instructions) + 2)

        self.label9 = tk.Label(self.frame, text='- Dakshveer Singh Chauahn', bg='ivory3')
        self.label9.grid(row=len(instructions) + 3, sticky=tk.E)

        self.label10 = tk.Label(self.frame, text='{ a noob programmer}', bg='ivory3')
        self.label10.grid(row=len(instructions) + 4, sticky=tk.E)

        tk.Button(self.frame, text='   EXIT   ', bg='red', command=self.root.destroy).grid(row=len(instructions) + 5)

        self.frame.grid(row=4, column=1)

    def bind_events(self):
        self.root.bind('<Button-1>', self.clickwin)
        self.root.bind('<B1-Motion>', self.dragwin)

    def dragwin(self, event):
        x = self.root.winfo_pointerx() - self.root._offsetx
        y = self.root.winfo_pointery() - self.root._offsety
        self.root.geometry('+{X}+{Y}'.format(X=x, Y=y))

    def clickwin(self, event):
        self.root._offsetx = event.x
        self.root._offsety = event.y