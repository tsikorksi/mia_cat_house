import random
import time

timestamp = 0

MAX_CATS = 5


class Cat:
    birthday = 0
    age = 0
    sex = 'N'
    breed = ''
    name = ''
    food = {"salmon": "", "cat food": "", 'chicken': "", "mouse": "", "peppers": "", "tuna": ""}

    def __init__(self):
        self.birthday = timestamp
        self.sex = random.choice(["F", "M"])
        self.name = random.choice(open('names.txt', 'r').readlines()).strip()
        self.breed = random.choice(open('breeds.txt', 'r').readlines()).strip()
        emotion = ["like", "don't like", "love", "adore", "stand"]
        for key in self.food.keys():
            self.food[key] = random.choice(emotion)

    def birth(self):
        return f"{self.name} was born! They are a cute {self.breed}."

    def happy_birthday(self):
        self.age += 1
        return f"""It is {self.name}'s birthday! Yay! They are now {self.age}.
                         (\_/)
                     (  =(^Y^)=
                  ____\_(m___m)_______"""

    def play(self):
        games = ["feathers", "bells", "you", 'a rubber mouse', "a cardboard box", "yarn"]
        return f"{self.name} is playing with {random.choice(games)}"

    def play_with(self, partner):
        games = ['chasing a ball', "playing on a cat tree", "playing with yarn", "play fighting"]
        return f"{self.name} is playing with {partner.name}. They are {random.choice(games)}!"

    def eat(self):
        food, emotion = random.choice(list(self.food.items()))
        return f"{self.name} is eating {food}. I think they {emotion} it!"

    def nap(self):
        return f"""{self.name} is taking a nap.
                      |\      _,,,---,,_
                ZZZzz /,`.-'`'    -.  ;-;;,_
                     |,4-  ) )-,_. ,\ (  `'-'
                    '---''(_/--'  `-'\_)  
                """


def main():
    count = 0
    cats = []
    global timestamp
    while True:

        rand = random.randint(0, 100)
        if (rand < 5 or count == 0) and count < MAX_CATS:
            kitty = Cat()
            cats.append(kitty)
            print(cats[-1].birth())
            count += 1
        elif 5 < rand < 30:
            print(random.choice(cats).eat())
        elif 50 < rand < 60:
            print(random.choice(cats).nap())
        else:
            kitty_a = random.choice(cats)
            kitty_b = random.choice(cats)
            if kitty_a == kitty_b:
                print(random.choice(cats).play())
            else:
                print(kitty_a.play_with(kitty_b))

        time.sleep(0.1)
        timestamp += 5

        for cat in cats:
            if (timestamp - cat.birthday) % 100 == 0:
                print(cat.happy_birthday())


if __name__ == '__main__':
    main()
