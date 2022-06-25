from tkinter import *
import random
from PIL import Image, ImageTk
names = []
global questions_answers
asked = []   

questions_answers = {
    1: ["What must you do when you see blue and red flashing lights behind you?", 'Speed up to get out of the way', 'Slow down and drive carefully','Slow down and stop', 'Drive on as usual' ,'Slow down and stop',3],
    2: ["You may stop on a motorway only:",'if there is an emergency','To let down or pick up passengers','to make a U-turn','to stop and take a photo', 'if there is an emergency',1],
    3: ["When coming up to a pedestrian crossing without a raised traffic island, what must you do?", 'Speed up before the pedestrians cross','Stop and give way to pedestrians on any part of the crossing', 'Sound the horn on your vehicle to warn the perestrians','slow down to 30kmh','Stop and give way to pedestrians on any part of the crossing',2],
}

def randomiser():
    global qnum
    qnum = random.randint(1,3)
    if qnum not in asked:
      asked.append(qnum)
    elif qnum in asked:
      randomiser()
     

class QuizStarter:
  def __init__(self, parent):
    background_color="lightyellow" 

    self.heading_label=Label(window, text = "Computer Parts Quiz!", font =( "Tw Cen MT","18","bold"),bg=background_color)
    self.heading_label.grid(row= 0, padx=350)

    self.var1=IntVar()

    self.user_label=Label(window, text="Please Enter your Username Below: ", font=( "Tw Cen MT","18","bold"),bg=background_color)
    self.user_label.grid(row=1, padx=20, pady=20)

    self.entry_box=Entry(window)
    self.entry_box.grid(row=2,padx=20, pady=20)

    self.continue_button = Button(window, text="Continue", font=( "Helvetica","13","bold"), bg="darkgrey",command=self.name_collection)
    self.continue_button.grid(row=3,padx=20, pady=20)

  def name_collection(self):
        name=self.entry_box.get()
        names.append(name)
        self.heading_label.destroy()
        self.user_label.destroy()
        self.entry_box.destroy()
        self.continue_button.destroy()
        Quiz(window)

class Quiz:

   def __init__(self, parent):
    background_color="lightgrey"
   
    self.quiz_frame = Frame(parent, bg = background_color, padx=40, pady=40)
    self.quiz_frame.grid()

    randomiser()

    self.question_label=Label(self.quiz_frame, text = questions_answers[qnum][0], font =( "Tw Cen MT","18","bold"))
    self.question_label.grid(row= 0, padx=10, pady=10)  

    self.var1=IntVar()

    self.rb1 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.var1, pady=10)
    self.rb1.grid(row=1, sticky=W)

    self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.var1, pady=10)
    self.rb2.grid(row=2, sticky=W)

    self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.var1, pady=10)
    self.rb3.grid(row=3, sticky=W)

    self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.var1, pady=10)
    self.rb4.grid(row=4, sticky=W)

    self.confirm_button = Button(self.quiz_frame, text="Confrim",bg="white")
    self.confirm_button.grid(row=6)

     
if __name__== "__main__":
    window = Tk()
    window.title("12CSC Quiz")
    window.geometry("500x600")
    bg_image = Image.open("Computer.jpg")
    bg_image = bg_image.resize((1000,600),Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label= Label(window, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_object = QuizStarter(window)

    window.mainloop()

