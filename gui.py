import random
import time
from tkinter import *
import main

root = Tk()
MAX_CATS = 5


def cat_loop(cat_list):
    """
    run a single instance of the cat loop, returning the appropriate random interaction

    :param cat_list: the current list of cats
    :return: will call function that will return text
    """
    count = len(cat_list)
    # while timestamp < extra:
    for cat in cat_list:
        if (time.time() - cat.birthday) > 600:
            cat.birthday = time.time()
            return cat.happy_birthday()

    rand = random.randint(0, 100)
    if (rand < 10 or count == 0) and count < MAX_CATS:
        kitty = main.Cat()
        cat_list.append(kitty)
        count += 1
        return cat_list[-1].birth()
    elif 20 < rand < 30:
        return random.choice(cat_list).eat()
    elif 30 < rand < 40:
        return random.choice(cat_list).drink()
    elif 50 < rand < 60:
        return random.choice(cat_list).nap()
    else:
        kitty_a = random.choice(cat_list)
        kitty_b = random.choice(cat_list)
        if kitty_a == kitty_b:
            return random.choice(cat_list).play()
        else:
            return kitty_a.play_with(kitty_b)


class Window(Frame):
    """
    Window Class
    """
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        self.watch_button = Button(self, text="Watch the Cats", command=self.cat_loop)
        self.watch_button.place(x=10, y=350)

        self.feed_button = Button(self, text="Feed a Cat", command=self.feed_button)
        self.feed_button.place(x=130, y=350)
        self.play_button = Button(self, text="Play with a Cat", command=self.play_button)
        self.play_button.place(x=240, y=350)
        self.call_button = Button(self, text="Call a Cat over", command=self.call_button)
        self.call_button.place(x=370, y=350)

        self.action_field = Text(root, height=20, width=100)
        self.action_field.place(x=0, y=0)
        self.action_field.insert(END, "Welcome to Mia's Cat House!\n")

        self.vsb = Scrollbar(self, orient="vertical", command=self.action_field.yview)
        self.vsb.place(x=100, y=0)

        self.action_allowed = True

        self.cat_loop()

    def cat_loop(self):
        """
        Runs a single instance of cat loop, locking the buttons while it runs

        :return: generates the text
        """
        self.action_allowed = False
        text = cat_loop(cats)
        self.update_text("\n" + text)
        time.sleep(1)
        self.action_allowed = True

    def feed_button(self):
        """
        calls feed action

        :return: updates text box
        """
        if self.action_allowed:
            text = player.feed(random.choice(cats))
            self.update_text(text)
            self.cat_loop()

    def play_button(self):
        """
        calls play action

        :return:  updates text box
        """
        if self.action_allowed:
            text = player.play_with(random.choice(cats))
            self.update_text(text)
            self.cat_loop()

    def call_button(self):
        """
        calls bring over action

        :return: updates text box
        """
        if self.action_allowed:
            text = player.bring_item(random.choice(cats))
            self.update_text(text)
            self.cat_loop()

    def update_text(self, text):
        """
        updates text field

        :param text: the text to be added
        :return: updates the text box in root
        """
        self.action_field.insert(INSERT, text)
        self.action_field.see(END)


cats = []
player = main.Player()
app = Window(root)

# set window title
root.wm_title("Mia's Cat House")

# show window
root.geometry("640x400")
root.mainloop()
