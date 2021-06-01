import random
import time

timestamp = 0

MAX_CATS = 5


class Cat:
    player_relation = 0
    birthday = 0
    age = 0
    sex = 'N'
    breed = ''
    name = ''
    food = {"salmon": "", "cat food": "", 'chicken': "", "mouse": "", "peppers": "", "tuna": ""}
    friends = []

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

    def check_friend(self, entity):
        if random.randint(0, 100) > 90 and entity not in self.friends:
            self.friends.append(entity)
            entity.friends.append(self)
            if type(entity) == Player:
                return f"{entity.name} is now your friend! <3"
            else:
                return f"{entity.name} and {self.name} are now friends!"
        return ""

    def play(self):
        games = ["feathers", "bells", "you", 'a rubber mouse', "a cardboard box", "yarn"]
        return f"{self.name} is playing with {random.choice(games)}"

    def play_with(self, partner):
        games = ['chasing a ball', "playing on a cat tree", "playing with yarn", "play fighting"]
        return f"{self.name} is playing with {partner.name}. " \
               f"They are {random.choice(games)}!\n{self.check_friend(partner)}"

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


class Player:
    name = ''

    friends = []

    def __init__(self):
        self.name = input("What is your name?").strip().capitalize()

    def feed(self, kitty: Cat):
        kitty.player_relation += 1
        return f"You fed {kitty.name}.\n{kitty.eat()}\n{kitty.check_friend(self)}"

    def play_with(self, kitty: Cat):
        kitty.player_relation += 1
        return f"You played with {kitty.name}.\n{kitty.play_with(self)}\n{kitty.check_friend(self)}"


def cat_loop(duration, cats):
    count = len(cats)
    global timestamp
    extra = timestamp + duration
    while timestamp < extra:

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

        time.sleep(5)
        timestamp += 5

        for cat in cats:
            if (timestamp - cat.birthday) % 100 == 0:
                print(cat.happy_birthday())

    return cats


def main():
    cats = []

    player = Player()
    print(f"Welcome to your cat house, {player.name}!")
    while True:
        cats = cat_loop(5, cats)
        desire = input("What would you like to do? You can feed a kitty, play with one, or just watch them.\n")
        if desire.lower().startswith("feed"):
            print(player.feed(random.choice(cats)))
        elif desire.lower().startswith("play"):
            print(player.play_with(random.choice(cats)))
        elif desire.lower().startswith("watch"):
            cats = cat_loop(10, cats)
        else:
            print("I didnt catch that. Lets watch them!")


if __name__ == '__main__':
    main()
