from tkinter import *
import random

names_list = []
global questions_answers
asked = []
score=0

questions_answers = {
  1: ['qwe',
      'a', 
      'b',
      'c',
     3],


  
}

def randomiser():
  global qnum
  qnum = random.randint(1,10)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    randomiser()


class QuizStarter:
  def __init__(self, parent):
    background_color="#eb4d4b"
    #Frame set up
    self.quiz_frame = Frame(parent, bg=background_color, padx=100, pady=100)
    self.quiz_frame.grid()

    #Label the widget for our heading
    self.heading_label = Label (self.quiz_frame, text = "NZ Road Rules", font=("Tw Cen MT", "18", "bold"))
    self.heading_label.grid(row=0)

    #Label for user name prompt
    self.user_label = Label ( self.quiz_frame, text = "Please enter your name below", font=("Tw Cen MT", "16"), bg=background_color)
    self.user_label.grid(row=1, pady=20)

    #Users imput is taken by an entry widget
    self.entry_box=Entry(self.quiz_frame)
    self.entry_box.grid(row=2, pady=20)

    #Continue button
    self.continue_button = Button(self.quiz_frame, text="Continue", bg="pink", command=self.name_collection)
    self.continue_button.grid(row=3, pady=20)

  def name_collection(self):
    name = self.entry_box.get()
    names_list.append(name)
    print(names_list)
    self.quiz_frame.destroy()
  

#----------Start of program----------#
randomiser()
if __name__ == "__main__":
  root = Tk()
  root.title("NZ Road Rules Quiz")
  quiz_instance = QuizStarter(root)
  root.mainloop() 
