from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self,quiz_brain :QuizBrain ):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)
        self.canvas = Canvas(width = 300, height = 250)
        self.image_false = PhotoImage(file="false.png")
        self.image_true = PhotoImage(file="true.png")
        self.canvas.config(bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150,125,text = "Text", font = ("Arial",20,"italic"),fill = THEME_COLOR,width = 280)
        self.canvas.grid(row = 2,column = 1,columnspan = 2)

        #Score Label
        self.score_label = Label(text = "Score : 0",font = 8,bg = THEME_COLOR,fg = "white")
        self.score_label.grid(row = 1,column = 2,padx = 10, pady = 10)

        #Buttons
        self.true_button = Button(image = self.image_true, highlightthickness=0,command = self.get_next_question_true)
        self.true_button.grid(row = 3,column = 1,padx = 20, pady = 20)

        self.false_button = Button(image = self.image_false, highlightthickness=0,command = self.get_next_question_false)
        self.false_button.grid(row = 3,column = 2,padx = 20, pady = 20)

        self.get_next_question()

        self.window.mainloop()

    def change_color(self):
        self.canvas.config(bg = "white")



    def get_next_question(self):
        if self.quiz.still_has_questions() :
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text = "You have reached the end of questions")
            self.true_button.config(state = "disabled")
            self.false_button.config(state = "disabled")



    def get_next_question_true(self):

        if self.quiz.check_answer("True"):
            self.canvas.config(bg = "Green")
            self.canvas.after(1500, self.change_color)
        else:
            self.canvas.config(bg = "Red")
            self.canvas.after(1500, self.change_color)
        self.score_label.config(text = f"Score : {self.quiz.score}")
        self.canvas.after(1500,self.get_next_question)

    def get_next_question_false(self):

        if self.quiz.check_answer("True"):
            self.canvas.config(bg="Green")
            self.canvas.after(1500,self.change_color)

        else:
            self.canvas.config(bg="Red")
            self.canvas.after(1500, self.change_color)
        self.score_label.config(text = f"Score : {self.quiz.score}")
        self.canvas.after(1500, self.get_next_question)