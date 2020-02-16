from tkinter import *
from dataStructs import *


class SimpleTable(Frame):
    def __init__(self, parent, rows=10, columns=2, **kw):
        # use black background so it "peeks through" to
        # form grid lines
        self.parent = parent
        super().__init__(**kw)
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = Label(self.parent, text="%s/%s" % (row, column), borderwidth=0, width=10)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)


class mainWindow(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        # self.master.resizable(False, False)
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
        self.midf.pack(side="top")
        self.lbl_info = Label(self.midf, text="RE:")
        self.lbl_info.pack(side="top")
        self.txtvarRE = StringVar("")
        self.lbl_re = Label(self.midf, textvariable=self.txtvarRE)
        self.lbl_re.pack(side="top")
        self.lbl_test = Label(self.midf, text="test string:")
        self.lbl_test.pack(side="top")
        self.txt_teststr = Entry(self.midf, width=80)
        self.txt_teststr.pack(side='left')
        self.btmf = Frame(self.master)
        self.btmf.pack(side="top")

        # Binding
        self.txt_teststr.bind("<KeyRelease>", self.getTestInput)

        # Initializing Automata
        self.eNFA = None
        self.i = self.j = 0  # i for row, j for column
        self.states = []  # list of states generated
        self.state_count = 0

    def getRE(self):
        self.i = self.j = 0
        self.states = []
        string = self.txt_re.get()
        if string == "":
            return
            # print("empty string")
        else:
            # print("RE: " + string)
            self.txtvarRE.set(string)
            self.eNFA = self.compile(string)

            # printing all states test--------------------------------------------
            # print(type(self.eNFA))
            self.printallstates(self.eNFA.start)  # printing all states
            # for x in self.states:
            #     print(x.name)
            # print("num of states: " + str(self.i))
            # print("num of inputs: " + str(self.j))
            self.i += 1  # add 1 row for heading
            self.j += 2  # add 2 column for state and epsilon
            ttable = SimpleTable(self.btmf, self.i, self.j)  # transition table initialized

            # heading for transition table-----------------------------------------
            char = []  # storing input characters / alphanumerics
            for x in string:
                if x.isalnum():
                    char.append(x)
            for x in range(0, self.j):
                heading = ["State"]
                for y in char:
                    heading.append(y)
                heading.append("Epsilon")
                ttable.set(0, x, heading[x])
            # heading end------------------------------------------------------------

            # Inserting states and transitions to transition table-------------------
            for idx, x in enumerate(self.states):
                row = [x.name]
                trans = []
                eps = []
                ctr = 0
                while ctr < len(char):
                    row.append("empty set")
                    ctr += 1

                for y in x.transitions:
                    if y is char[0]:
                        row[1] = x.transitions[y].name
                    elif y is char[1]:
                        row[2] = x.transitions[y].name
                    elif y is char[2]:
                        row[3] = x.transitions[y].name
                    elif y is char[3]:
                        row[4] = x.transitions[y].name
                    elif y is char[4]:
                        row[5] = x.transitions[y].name
                    elif y is char[5]:
                        row[6] = x.transitions[y].name
                    elif y is char[6]:
                        row[7] = x.transitions[y].name
                    elif y is char[7]:
                        row[8] = x.transitions[y].name
                    elif y is char[8]:
                        row[9] = x.transitions[y].name
                    elif y is char[9]:
                        row[10] = x.transitions[y].name
                    elif y is char[10]:
                        row[11] = x.transitions[y].name
                    elif y is char[11]:
                        row[12] = x.transitions[y].name
                    elif y is char[12]:
                        row[13] = x.transitions[y].name
                    elif y is char[13]:
                        row[14] = x.transitions[y].name
                    elif y is char[14]:
                        row[15] = x.transitions[y].name
                    elif y is char[15]:
                        row[16] = x.transitions[y].name
                    elif y is char[16]:
                        row[17] = x.transitions[y].name
                    elif y is char[17]:
                        row[18] = x.transitions[y].name
                    elif y is char[18]:
                        row[19] = x.transitions[y].name
                    elif y is char[19]:
                        row[20] = x.transitions[y].name
                    elif y is char[20]:
                        row[21] = x.transitions[y].name
                    elif y is char[21]:
                        row[22] = x.transitions[y].name
                    elif y is char[22]:
                        row[23] = x.transitions[y].name
                    elif y is char[23]:
                        row[24] = x.transitions[y].name
                    elif y is char[24]:
                        row[25] = x.transitions[y].name
                    elif y is char[25]:
                        row[26] = x.transitions[y].name

                if len(x.epsilon) is 0:
                    row.append("empty set")
                else:
                    for y in x.epsilon:
                        row.append(y.name)

                for y in x.transitions:
                    trans.append((y, x.transitions[y].name))
                for y in x.epsilon:
                    eps.append(y.name)
                # print(x.name, trans, eps)
                # print(row)
                ctr = 0
                while ctr < self.j:
                    ttable.set(idx+1, ctr, row[ctr])
                    ctr += 1

    def printallstates(self, start):
        if self.state_count is 0:
            return
        self.state_count -= 1
        curr = start
        self.i += 1
        # print(curr.name)
        # print(curr.transitions)
        # print(curr.epsilon)
        self.states.append(curr)

        for x in curr.transitions:
            self.j += 1
            self.printallstates(curr.transitions[x])

        for idx, x in enumerate(curr.epsilon):
            self.printallstates(curr.epsilon[idx])

    def getTestInput(self, *args):
        string = self.txt_teststr.get()
        if NFA.match(self.eNFA, string):
            self.txt_teststr.config(bg="green")
        else:
            self.txt_teststr.config(bg="red")

    def compile(self, p, debug=False):
        self.state_count = 0
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

        self.state_count = handler.state_count
        assert len(nfa_stack) == 1
        return nfa_stack.pop()


root = Tk()
run = mainWindow(root)
run.mainloop()
