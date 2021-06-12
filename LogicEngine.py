from tkinter import *
from Check import checkFormatProp,checkParenthisis,checkLiteral,checkFormatCNF
from Simplification import simplifyProp,SimplifyCNF
from Solver import solveCNF,solveProp
from string import ascii_lowercase

charactersetProp = set(ascii_lowercase+'&|~#@()')
charactersetCNF = set(ascii_lowercase+'&|~()')

def removeSpaces(string):
    return ''.join(string.split())

def placeWarning(warn):
    warn.place(relx=0.1,rely=0.7)
    warn.after(2000,warn.destroy)

def checkProp(lst):
    for ind,string in enumerate(lst):
        for char in string:
            if char not in charactersetProp:
                placeWarning(Label(mainframe,text="Character {} in input {} not valid".format(char,ind+1),font=("Arial",20),bg="white"))
                return 0
        if checkLiteral(string):
            placeWarning(Label(mainframe,text="No literal found in input {}".format(ind+1),font=("Arial",20),bg="white"))
            return 0
        if checkParenthisis(string):
            placeWarning(Label(mainframe,text="Incorrect brackets in input {}".format(ind+1),font=("Arial",20),bg="white"))
            return 0
        if checkFormatProp(string):
            placeWarning(Label(mainframe,text="input {} not valid".format(ind+1),font=("Arial",20),bg="white"))
            return 0
    return 1

def checkCNF(lst):
    for ind,string in enumerate(lst):
        for char in string:
            if char not in charactersetCNF:
                placeWarning(Label(mainframe,text="Character {} in input {} not valid".format(char,ind+1),font=("Arial",20),bg="white"))
                return 0
        if checkLiteral(string):
            placeWarning(Label(mainframe,text="No literal found in input {}".format(ind+1),font=("Arial",20),bg="white"))
            return 0
        if checkParenthisis(string):
            placeWarning(Label(mainframe,text="Incorrect brackets in input {}".format(ind+1),font=("Arial",20),bg="white"))
            return 0
        if checkFormatCNF(string):
            placeWarning(Label(mainframe,text="input {} not a valid CNF".format(ind+1),font=("Arial",20),bg="white"))
            return 0
    return 1

def Process(isCNF):
    string = text.get(1.0,"end-1c").strip()
    lst = list(map(removeSpaces,string.split('\n')))
    if isCNF:
        if checkCNF(lst):
            answer = solveCNF(SimplifyCNF(lst))
        else:
            return
    else:
        if checkProp(lst):
            answer = solveProp(simplifyProp(lst))
        else:
            return
    text.delete(1.0,END)
    # OUTPUT ANSWER
    if not len(answer):
        text.insert(END,'No solution exists')
    else:
        for i in answer:
            text.insert(END,i)
            text.insert(END,'\n\n')

mainframe = Tk()
mainframe.state('zoomed')
mainframe.configure(background='white')
mainframe.title('Logic Engine')

heading = Label(mainframe,text="Welcome to the Logic Engine",background='white',font=("Arial",35))
heading.place(relx=0.07,rely=0.05)

canvas = Canvas(mainframe,height=500,width=800)
canvas.place(relx=0.1,rely=0.2)

scrollbarY = Scrollbar(canvas,orient=VERTICAL)
scrollbarY.pack(side=RIGHT,fill=Y)
scrollbarX = Scrollbar(canvas,orient=HORIZONTAL)
scrollbarX.pack(side=BOTTOM,fill=X)

text = Text(canvas,height=20,width=80,border=4,relief='ridge',font=("Arial",15),wrap=NONE
            ,yscrollcommand=scrollbarY.set,xscrollcommand=scrollbarX.set)
text.insert(END,"Enter Propositions/CNF here\nClear before use")
text.pack()

scrollbarX.config(command=text.xview)
scrollbarY.config(command=text.yview)

submitCNF = Button(mainframe,text='Find all solutions for CNF (Fast)',command=lambda:Process(1),font=("Arial",15))
submitCNF.place(relx=0.745,rely=0.54)

submitProp = Button(mainframe,text='Find all solutions for Propositions (Slow)',command=lambda:Process(0),font=("Arial",15))
submitProp.place(relx=0.725,rely=0.59)

symbols = Label(mainframe,text="& for conjunction\n| for disjunction\n~ for negation\n# for implication"
                "\n@ for double implication\nUse lowercase letters as literals\n brackets also work\n"
                "CNF should be of the form\n(clause)&(clause)&...&(clause)",font=("Arial",20),bg="white")
symbols.place(relx=0.72,rely=0.2)

mainframe.mainloop()

# proposition
# ~~((a#(b|~~~c)@~a&r)&e) : correct
# ~~~((a#(b|~~~c)@~a&r)&e) : correct
# ~((a#~b)&~~(c@~~d)|~(e|e)) : correct
# CNF
# (~~~a|~b|~~c)&(~~a)&(~c|c) : correct
# (a|a|~a)&(a)&(~a|b)&(b|c)&(~b|d)&(d|~e) : correct