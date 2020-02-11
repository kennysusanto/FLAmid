from tkinter import *
from dataStructs import *


class mainWindow(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.master.resizable(False, False)
        self.master = master
        self.master.title("RE to eNFA")
        self.width = 640
        self.height = 240
        distx = disty = 100
        windowsize = str(self.width) + "x" + str(self.height) + "+" + str(distx) + "+" + str(disty)
        self.master.geometry(windowsize)
        self.topf = Frame(self.master)
        self.topf.pack(side="top")
        self.txt_re = Entry(self.topf, width=65)
        self.txt_re.pack(side="left")
        self.btn_build = Button(self.topf, text="Build Automata", command=self.getRE)
        self.btn_build.pack(side="left")
        self.midf = Frame(self.master)
        self.midf.pack(sid="top")
        self.lbl_info = Label(self.midf, text="RE:")
        self.lbl_info.pack(side="top")
        self.txtvarRE = StringVar("")
        self.lbl_re = Label(self.midf, textvariable=self.txtvarRE)
        self.lbl_re.pack(side="top")
        self.lbl_test = Label(self.midf, text="test string:")
        self.lbl_test.pack(side="top")
        self.txt_teststr = Entry(self.midf, width=80)
        self.txt_teststr.pack(side='left')

        # Binding
        self.txt_teststr.bind("<KeyRelease>", self.getTestInput)

        # Initializing Automata
        self.eNFA = None

    def getRE(self):
        string = self.txt_re.get()
        if string == "":
            print("empty string")
        else:
            print("RE: " + string)
            self.txtvarRE.set(string)
            self.eNFA = self.compile(string)

    def getTestInput(self, *args):
        string = self.txt_teststr.get()
        if NFA.match(self.eNFA, string):
            self.txt_teststr.config(bg="green")
        else:
            self.txt_teststr.config(bg="red")


    def compile(self, p, debug=True):
        def print_tokens(tokens):
            for t in tokens:
                print(t)

        lexer = Lexer(p)
        parser = Parser(lexer)
        tokens = parser.parse()

        handler = Handler()

        if debug:
            print_tokens(tokens)

        nfa_stack = []

        for t in tokens:
            handler.handlers[t.name](t, nfa_stack)

        assert len(nfa_stack) == 1
        return nfa_stack.pop()


root = Tk()
run = mainWindow(root)
run.mainloop()
