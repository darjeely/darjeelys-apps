from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random

class QuizApp(App): #create a class for our app
    def build(self):
        self.window = GridLayout()
        self.window.cols=1
        self.window.size_hint=(0.6, 0.7)
        self.window.pos_hint={"center_x": 0.5, "center_y": 0.5}

        # add widgets to window
        self.window.add_widget(Image(source="logo.png"))

        # create a list of questions and answers
        self.questions = [("What is the probability of getting two heads 105 times when tossing a fair coin 500 times?", "0.21", 10),
                          ("What is the probability of getting one head 275 times when tossing a fair coin 500 times?", "0.55", 20),
                          #("What is the currency of Japan?", "yen", 15),
                          #("What is the smallest country in the world?", "vatican city", 25)
                          ]

        # select two questions randomly
        self.question1, self.answer1, self.reward1 = random.choice(self.questions)
        self.question2, self.answer2, self.reward2 = random.choice(self.questions)

        # label widget
        self.question_label = Label(
                        text=self.question1,
                        font_size=40,
                        color="#456eba")

        # add label widget to window
        self.window.add_widget(self.question_label)

        # text input widget
        self.answer_input = TextInput(
                    multiline=False,
                    padding_y=(20,20),
                    size_hint=(1,0.5))

        # add text input widget to window
        self.window.add_widget(self.answer_input)

        # button widget
        self.button=Button(
                    text="Submit",
                    size_hint=(1,0.5),
                    bold=True,
                    background_color="#456eba",
                    background_normal="")
        self.button.bind(on_press=self.check_answer)

        # add button widget to window
        self.window.add_widget(self.button)

        return self.window

    def check_answer(self, instance):
        answer = self.answer_input.text.lower()

        if answer == self.answer1:
            self.question_label.text = f"Correct! You have earned {self.reward1} points."
        elif answer == self.answer2:
            self.question_label.text = f"Correct! You have earned {self.reward2} points."
        else:
            self.question_label.text = "Incorrect."

if __name__ == "__main__":
    QuizApp().run()
