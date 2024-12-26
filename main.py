#Creating the main window and adding size, title and color
wn= Tk()
wn.geometry('600x600')
wn.title("PythonGeeks Typing Test")
wn.config(bg='LightBlue1')

#Creating a frame to show the title of the project
headingFrame1 = Frame(wn,bg="snow3",bd=5)
headingFrame1.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n PythonGeeks Typing Test", bg='azure2',fg='black', font=('Courier',15,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#Creating a button to start the game. The startGame function, given as command parameter, runs on clicking the button
btn = Button(wn,text="Start",bg='old lace', fg='black',width=20,height=2,command=startGame)
btn['font'] = font.Font( size=12)
btn.place(x=200,y=300)

wn.mainloop()#Runs the window till it is closed
