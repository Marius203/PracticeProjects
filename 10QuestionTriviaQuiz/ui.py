THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

class QuizUI:
    def __init__(self, quizbrain: QuizBrain) -> None:
        self.quizbrain=quizbrain
        self.window = Tk()
        self.window.title("Trivia quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,125,width=280,text="nothing at the moment", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quizbrain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quizbrain.score}")
            text = self.quizbrain.next_question()
            self.canvas.itemconfig(self.question_text, text=text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have answered 10 questions")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")



    def true_pressed(self):
        self.give_feedback(self.quizbrain.check_answer("True"))


    def false_pressed(self):
        self.give_feedback(self.quizbrain.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(200, self.get_next_question)
