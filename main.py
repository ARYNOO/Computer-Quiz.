# Aryan Narayan 2022 Quiz

from tkinter import *  # for user interface
import random  # for randomising questions
from PIL import Image, ImageTk  # for images like background
from tkinter import messagebox  # for message box

# list that are names saved to

names = []

# lists

asked = []
score = 0


# randomiser method

def randomiser():
    global qnum
    qnum = random.randint(1, 10)

    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()


# component one (quiz window)

class quizwindow:

    def __init__(self, parent):
        background_color = 'lightyellow'

        self.heading_label = Label(window, text='Computer Parts Quiz!',
                                   font=('Tw Cen MT', '18', 'bold'),
                                   bg=background_color)  # heading label
        self.heading_label.place(x=200, y=150)

        self.enter_label = Label(window, text='Please enter name: ',
                                 font=('Tw Cen MT', '18', 'bold'),
                                 bg=background_color)  # enter label
        self.enter_label.place(x=215, y=200)

        self.entry_box = Entry(window)  # entry box
        self.entry_box.place(x=265, y=250)

        self.continue_button = Button(window, text='Start Quiz!',
                font=('Comic Sans MS', '13', 'bold'), bg='purple',
                command=self.name_collection)  # continue button
        self.continue_button.place(x=283, y=295)

    def name_collection(self):
        name = self.entry_box.get()

        if name == '':
            messagebox.showerror('Name is required! :(',
                                 'Please enter your name!')
        elif len(name) > 15:

            messagebox.showerror('an error has occurred!',
                                 'please enter a name between 1 and 15 characters'
                                 )
        elif name.isnumeric():
            messagebox.showerror('an error has occurred!',
                                 'Name can only consist of letters ONLY!!'
                                 )
        elif not name.isalpha():

            messagebox.showerror('an error has occurred!',
                                 'No Symbols Please! Please Try Again!')
        else:

            names.append(name)
            print (names)
            self.heading_label.destroy()
            self.enter_label.destroy()
            self.entry_box.destroy()
            self.continue_button.destroy()
            computerquizquestion(window)


class computerquizquestion:

    def __init__(self, parent):
        background_color = 'purple'

        self.questionans_dictionary = {
            1: [
                'Which type among the following expansion \n slots are used solely for a video card?'
                    ,
                'PCI',
                'AGP',
                'ISA',
                'XDA',
                'PCI',
                1,
                ],
            2: [
                'What is the brain of a computer?',
                'South Bridge',
                'Motherboard',
                'Solid State Drive',
                'Random Access Memory',
                'Motherboard',
                2,
                ],
            3: [
                'What does PSU stand for',
                'Partial supply unit',
                'Printer Supply Unit',
                'Processor supply unit',
                'Power Supply unit',
                'Power Supply unit',
                4,
                ],
            4: [
                'What\xe2\x80\x99s does RAM stand for?',
                'Rapid Access Memory',
                'Random Access Memory',
                'Rigid access memory',
                'Read/write access memory',
                'Random Access Memory',
                2,
                ],
            5: [
                'What does GPU stand for',
                'Graphics proliferation unit',
                'Graphics protocol unit',
                'Graphics processing unit',
                'General processing unit',
                'Graphics processing unit',
                3,
                ],
            6: [
                'What type of cable would you use to connect a\n Solid State drive to a motherboard'
                    ,
                'IDE Cable',
                'Sata Power',
                'Sata Data Cable',
                'USB 3.0',
                'Sata Data Cable',
                3,
                ],
            7: [
                'What Socket Fits AMD\xe2\x84\xa2 Ryzen CPUs? \n (1000-4000SERIES)'
                    ,
                'AM4',
                'LGA 1200',
                'LGA 1700',
                'AM5',
                'AM4',
                1,
                ],
            8: [
                'What Socket fits Intel\xe2\x84\xa2 12th Gen CPUs?',
                'LGA 1700',
                'LGA 1200',
                'AM3',
                'AM3 +',
                'LGA 1700',
                1,
                ],
            9: [
                'What Socket fits Amd\xe2\x84\xa2 Ryzen 7000 Series CPUs? '
                    ,
                'AM4',
                'AM5',
                'AM6',
                'AM3',
                'AM5',
                2,
                ],
            10: [
                'What is a PWM fan?',
                'Power molex motor',
                'Pluse weight motor',
                'Power Weight motor',
                'Pulse width modulation fans ',
                'Pulse width modulation fans',
                4,
                ],
            }

        # quiz frame

        self.quiz_frame = Frame(parent, bg=background_color, padx=40,
                                pady=40)

        randomiser()

        # question label

        self.question_label = Label(window,
                                    text=self.questionans_dictionary[qnum][0],
                                    font=('Tw Cen MT', '18', 'bold'),
                                    bg=background_color)
        self.question_label.grid(row=0, padx=10, pady=10)

        self.con1 = IntVar()

        self.rb1 = Radiobutton(
            window,
            text=self.questionans_dictionary[qnum][1],
            font=('Helvetica', '12'),
            bg=background_color,
            value=1,
            variable=self.con1,
            pady=10,
            )
        self.rb1.grid(row=1, sticky=W)

        self.rb2 = Radiobutton(
            window,
            text=self.questionans_dictionary[qnum][2],
            font=('Helvetica', '12'),
            bg=background_color,
            value=2,
            variable=self.con1,
            pady=10,
            )
        self.rb2.grid(row=2, sticky=W)

        self.rb3 = Radiobutton(
            window,
            text=self.questionans_dictionary[qnum][3],
            font=('Helvetica', '12'),
            bg=background_color,
            value=3,
            variable=self.con1,
            pady=10,
            )
        self.rb3.grid(row=3, sticky=W)

        self.rb4 = Radiobutton(
            window,
            text=self.questionans_dictionary[qnum][4],
            font=('Helvetica', '12'),
            bg=background_color,
            value=4,
            variable=self.con1,
            pady=10,
            )
        self.rb4.grid(row=4, sticky=W)

        self.confirm_button = Button(window, text='Confrim', bg='Blue',
                command=self.quiz_score)
        self.confirm_button.place(x=300, y=235)

        self.score_label = Label(window, text='score')
        self.score_label.place(x=390, y=240)

        self.leave = Button(window, text='Leave', font=('Helvetica',
                            '13', 'bold'), bg='red',
                            command=self.end_screen)
        self.leave.place(x=200, y=235)

    def qa_setup(self):
        randomiser()
        self.con1.set(0)
        self.question_label.config(text=self.questionans_dictionary[qnum][0])
        self.rb1.config(text=self.questionans_dictionary[qnum][1])
        self.rb2.config(text=self.questionans_dictionary[qnum][2])
        self.rb3.config(text=self.questionans_dictionary[qnum][3])
        self.rb4.config(text=self.questionans_dictionary[qnum][4])

    def quiz_score(self):
        global score
        score_label = self.score_label
        choice = self.con1.get()
        if len(asked) > 9:
            if choice == self.questionans_dictionary[qnum][6]:
                score += 1  # adds one point to score
                score_label.configure(text=score)
                self.confirm_button.config(text='Confirm')
                self.end_screen()
            else:

                score += 0  # score will stay the same
                score_label.configure(text='The correct answer was: '
                        + self.questionans_dictionary[qnum][5])
                self.confirm_button.config(text='confirm')
        else:

            if choice == 0:
                self.confirm_button.config(text="Try Again, you didn't select an option then submit again"
                        )

                choice = self.con1.get()  #
            else:

                if choice == self.questionans_dictionary[qnum][6]:
                    score += 1
                    score_label.configure(text=score)
                    self.confirm_button.config(text='confirm')
                    self.qa_setup()
                else:

                    score += 0
                    score_label.configure(text='The correct answer was: '
                             + self.questionans_dictionary[qnum][5])
                    self.confirm_button.config(text='Confirm')
                    self.qa_setup()  # move to next question

    def end_screen(self):
        window.destroy()
        name = names[0]

        open_end_object = end()


class end:

    def __init__(self):
        background_color = 'purple'
        global window2
        window2 = Tk()
        window2.title('Exit Box')
        window2.geometry('700x600')

        self.end_frame = Frame(window2, width=700, height=600,
                               bg=background_color)
        self.end_frame.grid(row=1)

        self.end_heading = Label(window2, text='You finshed the Quiz!',
                                 font=('Tw Cen Mt', 22, 'bold'),
                                 bg=background_color)
        self.end_heading.place(x=50, y=50)

        self.exit_button = Button(
            window2,
            text='Exit',
            width=10,
            bg='red',
            font=('Tw Cen Mt', 12, 'bold'),
            command=self.close_end,
            )
        self.exit_button.place(x=260, y=200)

        self.list_label = Label(window2, text='Good Job!',
                                font=('Tw Cen Mt', 12, 'bold'),
                                width=40, bg=background_color)
        self.list_label.place(x=110, y=100)

    def close_end(self):
        self.end_frame.destroy()
        self.end_heading.destroy()
        self.exit_button.destroy()
        self.list_label.destroy()
        window2.destroy()


# program runs below

if __name__ == '__main__':
    window = Tk()
    window.title('Computer Parts Quiz!')
    window.geometry('700x600')
    bg_image = Image.open('Computer.jpg')  # need to use Image if need to resize
    bg_image = bg_image.resize((1000, 600), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)

    # image label

    image_label = Label(window, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_object = quizwindow(window)

    window.mainloop()  # so the window stays in place
