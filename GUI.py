from tkinter import *
import GUIPractice


choices = {"Australia",
    "Bangladesh",
    "England",
    "India",
    "South Africa",
    "New Zealand",
    "Sri Lanka",
    "Zimbabwe",
    "Pakistan",
    "Afghanistan",
    "West Indies",
    "Ireland"
}

groundsNames ={ "Observatory Lane, Rathmines",
          "Grace Road","Sheikh Zayed Stadium","Sheikh Kamal International Cricket Stadium","Nahar Singh Stadium","Rawalpindi Cricket Stadium",
          "Jaffery Sports Club Ground","Keenan Stadium","Gaddafi Stadium","Queenstown Events Centre","Madhavrao Scindia Cricket Ground","Jade Stadium",
          "Nondescripts Cricket Club Ground","Sheikh Abu Naser Stadium","Brabourne Stadium","Edgbaston","Antigua Recreation Ground, St John's","Headingley","Maharashtra Cricket Association Stadium",
           "Punjab Cricket Association Stadium"
          }
myTeam=None
myGround=None
myOver=None
myRun=None
myWicket=None


root = Tk()
root.title("Cricket Result Predictor")
root.config(background="light sea green")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=50, padx=50)


# Create a Tkinter variable
tkvar1 = StringVar(root)
tkvar1.set("Bangladesh")  # set the default option

popupMenu = OptionMenu(mainframe, tkvar1, *choices)
Label(mainframe, text="Choose team").grid(row=0, column=0,sticky=E)
popupMenu.grid(row=0, column=1,)


# on change dropdown value
def change_dropdown1(*args):
    #print(tkvar1.get())
    global myTeam
    myTeam = tkvar1.get()
    return myTeam




#Create a Tkinter variable for ground
tkvar2 = StringVar(root)
tkvar2.set("Ground")  # set the default option

popupMenu2 = OptionMenu(mainframe, tkvar2, *groundsNames)
Label(mainframe, text="Choose ground").grid(row=1, column=0,sticky=E)
popupMenu2.grid(row=1, column=1,)


# on change dropdown value
def change_dropdown2(*args):
    #print(tkvar1.get())
    global myGround
    myGround = tkvar2.get()
    return myGround



def get_Runs():
    return runs.get()

def get_Overs():
    return overs.get()

def get_Wickets():
    return wickets.get()

def get_Ground():
    print(tkvar2.get())

def printPrediction(event):
    print("Ok ok")
    team= tkvar1.get()
    ground= tkvar2.get()
    runs= get_Runs()
    wickets= get_Wickets()
    overs= get_Overs()

    overs= int(overs)
    runs= int(runs)
    wickets= int(wickets)
    #print(team," ",ground,  " ",overs," " , runs, " ", wickets)

    pr_run, pr_wicket= GUIPractice.main1(team, ground, overs, runs, wickets)

    root1= Tk()
    root1.title("Result ")
    #root1.config(background= 'blue')

    label1= Label(root1, text= "Predicted Runs: ")
    label2= Label(root1, text=pr_run)

    label3 = Label(root1, text="Predicted Wickets: ")
    label4 = Label(root1, text=pr_wicket)

    label1.pack()
    label2.pack()
    label3.pack()
    label4.pack()

    root1.mainloop()

    print(pr_run, " ", pr_wicket)
    #print(myTeam)


#def executeCalculation(tkvar1,ground,overs,runs,wickets):
 #   print("Calculating")

# link function to change dropdown
tkvar1.trace('w', change_dropdown1)

groundsLabel=Label(mainframe,text="Ground")
# groundsLabel.grid(row=1,column=0,sticky=E)
# ground=Entry(mainframe)
# ground.grid(row=1,column=1)

overLabel=Label(mainframe,text="Overs Completed")
overLabel.grid(row=3,column=0,sticky=E)
overs=Entry(mainframe)
overs.grid(row=3,column=1)

runsLabel=Label(mainframe,text="Runs")
runsLabel.grid(row=4,column=0,sticky=E)
runs=Entry(mainframe)
runs.grid(row=4,column=1)

wicketsLabel=Label(mainframe,text="Wickets")
wicketsLabel.grid(row=5,column=0,sticky=E)
wickets=Entry(mainframe)
wickets.grid(row=5,column=1)

def something():
    print()


button_1=Button(mainframe,text="Predict score")
button_1.grid(row=6,column=1)
button_1.bind("<Button-1>",printPrediction)

change_dropdown1(choices)
get_Runs()

res=Label(mainframe)
res.grid(row=10)

root.mainloop()