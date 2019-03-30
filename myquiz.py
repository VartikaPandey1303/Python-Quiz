# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 01:17:14 2019

@author: user
"""

from tkinter import *

from tqq import *

root = Tk()
root.configure(bg="white")
root.geometry('1000x600')

#WIDGETS FOR INTRO PAGE
name_label = Label(root, text="NAME: ", bg = "white", fg = "black",anchor = CENTER, height = 2, font = 'Arial -30 bold')
name_entry = Entry(root, bd=10, font = 'Arial -30 italic')
number_label = Label(root, text = "ROLL NUMBER ", bg = "white", fg = "black", anchor = CENTER, height = 2, font = 'Arial -30 bold')
number_entry = Entry (root, bd = 10, font = 'Arial -30 italic')


#INITIALIZING VARIABLES RO STORE THE ENTRY VALUES
name = ""
number = 0

#LEVEL OF DIFFICULTY=LEVEL,QUESTION NUMBER=I
level = 1
i = 0
score = 0

#PAGE TWO TO APPEAR
hello = Label(root)
intro = Label(root, text = "QUIZ", bg = "white", fg = "Violet", anchor = CENTER, height = 2, font = 'Arial -40 bold')

#LABEL TO DEFINE LEVEL
level_label = Label(root, height = 2, bg = "white", fg = "grey", font = "Arial -30 bold")

#AFTER PRSSING SUBMIT1 BUTTON, COMMAND ATTRIBUTE LEADS TO THIS FUNCTION
def get_details():
	global name   #TO STORE NAME OF THE PARTICIPANT
	global number #TO STORE ID NUMBER
	name = name_entry.get()  #VALUE ENTERED IN ENTRY WIDGET STORED 
	number = number_entry.get()
	
	#DESTROY OLD WIDGETS WHICH ARE NO LONGER REQUIRED IN THE WINDOW
	name_label.destroy()  #DESTROY/UNPACK LABEL FROM WINDOW
	name_entry.destroy()  #DESTROY ENTRY FROM WINDOW
	number_label.destroy() 
	number_entry.destroy()
	submit1.destroy() #DESTROY THE BUTTON
	hello.config(text = "Hello, "+name+"! \n Let's start the quiz!", bg="white", height = 7, font ='Arial -30 bold', fg = 'black')
	hello.pack()
	b.pack()

#SUBMIT BUTTON
submit1 = Button(root, text = "NEXT", height = 2, width = 5, relief=RAISED,fg = "yellow", bg = "black", font = 'Arial -15 bold', command = get_details)

#PACKING THE WIDGETS IN THE WINDOWS 
intro.pack(fill = X)
name_label.pack()
name_entry.pack()
number_label.pack()
number_entry.pack()
submit1.pack(expand = True)  #EXPANSION OF PARENT WIDGET

##############################################################################################################################

#CREATE LIST OF QUESTIONS
#QUESTIONS ARE IMPORTED FROM OTHER FILE]
qlist = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13]
#CREATE AN EMPTY LIST TO STORE THE RESPONSES
alist = []

#LISTS TO STORE CORRECT AND INCORRECT ANSWERS
correct = []
wrong = []


#WIDGETS: QUESTION LABEL, OPTIONS RADIOBUTTONS
question = Label(root, height = 5,bg = "white",fg="blue", font ='Arial -25 bold' )
answer = IntVar()
#VARIALBLE ANSWER IS IntVar() AND WILL STORE THE VALUE OF RADIOBUTTON AS AN INTEGER

b1 = Radiobutton(root, variable = answer, value = 1,bg = "white", font ='Arial -15 bold' )
b2 = Radiobutton(root, variable = answer, value = 2,bg = "white", font ='Arial -15 bold' )
b3 = Radiobutton(root, variable = answer, value = 3,bg = "white", font ='Arial -15 bold' )
b4 = Radiobutton(root, variable = answer, value = 4,bg = "white", font ='Arial -15 bold' )

#OPTIONS STORED IN B1,B2,V3,B4 
options = [b1, b2, b3, b4]
submit2 = Button(root, text = "SUBMIT", relief = RAISED, fg = "pink", bg = "black", font = "Arial -15 italic")

##############################################################################################################################

#TO BEGIN THE QUIZ
def begin():
	hello.destroy()
	b.destroy()
	level_label.config(text = "Level 1")
	level_label.pack(fill=X)
	Button(root, text = "Quit", bg = "yellow", fg = "black", font = "Arial -15 bold", relief = RAISED, anchor = S, command = root.quit).pack(fill = Y, side = BOTTOM)
	questions()

#BUTTON WITH COMMAND TO DISPLAY QUESTIONS
b = Button(root, text = "Begin",  bg = "white", fg = "black", relief=RAISED,font = "Arial -15 bold", command = begin)
#LABEL FOR WHEN QUIZ ENDS
over = Label(root, text = 'Quiz over!', bg = "white", fg = "black", font = 'Arial -30 bold', height = 5)

#QUIZ RESULT
def result():
	score=0
	#CALCULATE SCORE
	for x in range(13):
		if alist[x] == rlist[x]:
			correct.append(x+1)
			score+=1
		else:
			wrong.append(x+1)
	
	level_label.destroy()
	over.destroy()
	seeresult.destroy()
	
	Label(root, text = "Total score: "+str(score), font = 'Arial -25 bold', bg = "white", height = 5, fg = 'blue').pack()
	Label(root, text = "Correct answers: "+str(len(correct)), font = 'Arial -25 bold',bg = "white", height = 5, fg = 'green').pack()
	Label(root, text = "Wrong answers: "+str(len(wrong)), font = 'Arial -25 bold', bg = "white",height = 5, fg = 'red').pack()

seeresult = Button(root, text = "Show result",font = 'Arial -10 italic', fg = 'Blue', bg = 'white', height = 4, width = 10, command = result)

#TO GO TO NEXT LEVEL
def next_level():
	global level
	level+=1
	changelevel.pack_forget()
	seeresult.pack_forget()
	level_label.config(text = "Level "+str(level))
	submit2.config(state = NORMAL)
	questions()

changelevel= Button(root, text = "Go to the next level", font = 'Arial -10 italic', fg = 'pink', bg = 'black', height = 3, width = 20, command = next_level)

#SUBMIT AN ANSWER
def submit(x):
	alist.append(x)
	answer.set(0)
	if not (i==4 or i==8 or i==12) and i<13:
		questions()
	elif (i==4 or i==8 or i==12):
		submit2.pack_forget()
		question.pack_forget()
		b1.pack_forget()
		b2.pack_forget()
		b3.pack_forget()
		b4.pack_forget()
		changelevel.pack(expand = True)
	elif i==13:	
		submit2.pack_forget()
		question.pack_forget()
		b1.pack_forget()
		b2.pack_forget()
		b3.pack_forget()
		b4.pack_forget()
		over.pack(fill=X)
		seeresult.config(text = "See result", command = result)
		seeresult.pack()

#QUESTIONS AND OPTIONS PACKED AS WIDGETS
def questions():
	global i
	question.config(text = qlist[i].q)
	question.pack()
	b1.config(text = qlist[i].a1)
	b1.pack()
	b2.config(text = qlist[i].a2)
	b2.pack()
	b3.config(text = qlist[i].a3)
	b3.pack()
	b4.config(text = qlist[i].a4)
	b4.pack()
	i+=1
	submit2.config(command = lambda: submit(answer.get()))
	submit2.pack(expand=True)

mainloop()