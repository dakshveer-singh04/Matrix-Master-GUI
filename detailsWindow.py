import tkinter as tk

class detailsWindow:
    def __init__(self, root):
        self.root = root

        self.Canvas1 = tk.Canvas(self.root, height=200, width=800)
        self.Canvas1.config(bg='blue', width=500, height=150)
        self.Canvas1.create_arc(10, 10, 150, 150, start=45, extent=260, fill="Red", outline="yellow", width=2)
        self.Canvas1.grid(row=0, column=0, columnspan=6, sticky=tk.EW)
        
        self.create_labels()
        self.create_frame()
        
        self.root.overrideredirect(True)
        self.root._offsetx = 0
        self.root._offsety = 0

        self.root.bind('<Button-1>', self.clickwin)
        self.root.bind('<B1-Motion>', self.dragwin)

    def create_labels(self):
        self.la1 = tk.Label(self.root, text="Hello", bg="Yellow", width=10)
        self.la1.grid(row=1, column=0, sticky=tk.NS, rowspan=15)
        self.la1 = tk.Label(self.root, text="Hello", bg="Orange", fg="White", width=10)
        self.la1.grid(row=1, column=5, sticky=tk.NS, rowspan=15)
        self.la1 = tk.Label(self.root, text="Welcome to Details Page", bg="Red", height=7)
        self.la1.grid(row=1, column=1, columnspan=4, sticky=tk.EW)
        self.la1 = tk.Label(self.root, text="All rights reserved", bg="Black", fg='white')
        self.la1.grid(row=15, column=1, columnspan=4, sticky=tk.EW)
        self.la1 = tk.Label(self.root, bg='light blue', text="Details Page")
        self.la1.grid(row=2, column=1, columnspan=4, sticky=tk.EW)
        tk.Label(self.root).grid(row=3, column=1)

    def create_frame(self):
        self.fr1 = tk.Frame(self.root)
        self.la1 = tk.Label(self.fr1, text='Very felicific to present Matrix Master 2.0', bg='ivory2')
        self.la1.grid(row=0)
        self.la1 = tk.Label(self.fr1, text=' ', bg='ivory2')
        self.la1.grid(row=1)
        self.la1 = tk.Label(self.fr1, text='It would be a sin not to acknowledge the support of family and teachers',bg='ivory2')
        self.la1.grid(row=2)
        self.la1 = tk.Label(self.fr1, text='and friends (Yash and Rishi) who showered constructive feedbacks.',bg='ivory2')
        self.la1.grid(row=3)
        self.la1 = tk.Label(self.fr1, text=' ', bg='ivory2')
        self.la1.grid(row=4)
        self.la1 = tk.Label(self.fr1, text='Thank you all for your support and guidance and valuable time',bg='ivory2')
        self.la1.grid(row=5)
        self.la1 = tk.Label(self.fr1, text='', bg='ivory2')
        self.la1.grid(row=6)
        self.la1 = tk.Label(self.fr1, text='To all esteemed, feel free to mail me for suggestion or faults on\n',bg='ivory2')
        self.la1.grid(row=7)
        self.la1 = tk.Label(self.fr1, text='       dakshveersinghchauhan@gmail.com', bg='ivory3')
        self.la1.grid(row=8)
        self.la1 = tk.Label(self.fr1, text=' ', bg='ivory2')
        self.la1.grid(row=9)
        self.la1 = tk.Label(self.fr1, text='', bg='ivory2')
        self.la1.grid(row=10)

        self.la1 = tk.Label(self.fr1, text='- Dakshveer Singh Chauahn', bg='ivory3')
        self.la1.grid(row=11, sticky=tk.E)
        self.la1 = tk.Label(self.fr1, text='{ a noob programmer}', bg='ivory3')
        self.la1.grid(row=12, sticky=tk.E)

        tk.Button(self.fr1, text='   EXIT   ', bg='red', command=self.root.destroy).grid(row=15)

        self.fr1.grid(row=4, column=1)

    def dragwin(self, event):
        x = self.root.winfo_pointerx() - self.root._offsetx
        y = self.root.winfo_pointery() - self.root._offsety
        self.root.geometry('+{X}+{Y}'.format(X=x, Y=y))

    def clickwin(self, event):
        self.root._offsetx = event.x
        self.root._offsety = event.y