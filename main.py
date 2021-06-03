import random
import time

timestamp = 0

MAX_CATS = 5


class Cat:
    """
    The cat class
    """
    player_relation = 0
    birthday = 0
    age = 0
    sex = 'N'
    breed = ''
    name = ''
    food = {"salmon": "", "dry food": "", 'chicken': "", "wet food": "", "peppers": "", "tuna": ""}
    friends = []

    def __init__(self):
        self.birthday = time.time()
        self.sex = random.choice(["F", "M"])
        self.name = random.choice(open('names.txt', 'r').readlines()).strip()
        self.breed = random.choice(open('breeds.txt', 'r').readlines()).strip()
        # generate feelings for each food
        emotion = ["like", "don't like", "love", "adore", "stand"]
        for key in self.food.keys():
            self.food[key] = random.choice(emotion)

    def birth(self):
        """
        runs each time a cat is born

        :return: the text for the cat
        """
        return f"{self.name} was born! They are a cute {self.breed}."

    def happy_birthday(self):
        """
        Runs each time the birthday is hit

        :return: the birthday text
        """
        self.age += 1
        return f"""It is {self.name}'s birthday! Yay! They are now {self.age}.
                         (\\_/)
                     (  =(^Y^)=
                  ____\\_(m___m)_______"""

    def check_friend(self, entity):
        """
        checks to see if the cat has made a friend

        :param entity: the entity to check, either player or another cat
        :return: the friendsip text
        """
        if (random.randint(0, 100) > 90 or self.player_relation > 10) and entity not in self.friends:
            self.friends.append(entity)
            entity.friends.append(self)
            if type(entity) == Player:
                return f"{self.name} is now your friend! <3"
            else:
                return f"""{entity.name} and {self.name} are now friends!
                      /^--^\\     /^--^\\    
                      \\____/     \\____/  
                     /      \\   /      \\ 
                    |        | |        | |       
                     \\__  __/   \\__  __/  
                """
        return ""

    def play(self):
        """
        Play alone with random item

        :return: the play with text
        """
        games = ["feathers", "bells", "you", 'a rubber mouse', "a cardboard box", "yarn"]
        return f"""{self.name} is playing with {random.choice(games)}
                     |\\__/,|   (`
                   _.|o o  |_   ) )
                  -(((---(((--------"""

    def play_with(self, partner):
        """
        play with another entity

        :param partner: the other entity
        :return: the play text
        """
        games = ['chasing a ball', "playing on a cat tree", "playing with yarn", "play fighting"]
        return f"{self.name} is playing with {partner.name}. " \
               f"""They are {random.choice(games)}!\n{self.check_friend(partner)}
                           __..--''``---....___   _..._    __
                 /// //_.-'    .-/";  `        ``<._  ``.''_ `. / // /
                ///_.-' _..--.'_    /                    `( ) ) // //
                / (_..-' // (< _     ;_..__               ; `' / ///
                 / // // //  `-._,_)' // / ``--...____..-' /// / //"""

    def eat(self):
        """
        eat random food, working applying emotion

        :return: the eat text
        """
        food, emotion = random.choice(list(self.food.items()))
        return f"{self.name} is eating {food}. I think they {emotion} it!"

    def drink(self):
        """
        drink random drink

        :return: the drink text
        """
        drink = ["milk", "water", "formula", "bone broth", "apple juice"]
        return f"{self.name} is drinking {random.choice(drink)}. Ahhhh."

    def nap(self):
        """
        sleep kitty

        :return: sleep text
        """
        return f"""{self.name} is taking a nap.
                      |\\      _,,,---,,_
                ZZZzz /,`.-'`'    -.  ;-;;,_
                     |,4-  ) )-,_. ,\\ (  `'-'
                    '---''(_/--'  `-'\\_)  
                """


class Player:
    name = ''

    friends = []

    def __init__(self):
        self.name = input("What is your name?").strip().capitalize()

    def feed(self, kitty: Cat):
        """
        feed a cat with a random food item, check for friend

        :param kitty: the cat to feed
        :return: the feed text
        """
        kitty.player_relation += 1
        return f"\nYou fed {kitty.name}.\n{kitty.eat()}\n{kitty.check_friend(self)}"

    def play_with(self, kitty: Cat):
        """
        Play a random game with a cat

        :param kitty: the cat to play with
        :return: the play text
        """
        kitty.player_relation += 1
        return f"\nYou played with {kitty.name}.\n{kitty.play_with(self)}\n{kitty.check_friend(self)}"

    def bring_item(self, kitty: Cat):
        """
        Bring item over interaction

        :param kitty: the cat to play with
        :return: the interaction text
        """
        kitty.player_relation += 1
        items = ["piece of string", "spare treat", "quarter", "dead bug. Ew!", "ball", "hair tie", " piece of trash",
                 "plushie"]
        return f"\n{kitty.name} brought you a {random.choice(items)}.\n{kitty.check_friend(self)}"


def cat_loop(duration, cats):
    """
    run the cat loop for the set duration, 5 seconds == 1 interaction

    :param duration: the set duration to loop for
    :param cats: the list of cats that can be interacted with
    :return: prints the interaction
    """
    count = len(cats)
    global timestamp
    extra = timestamp + duration
    while timestamp < extra:

        rand = random.randint(0, 100)
        if (rand < 10 or count == 0) and count < MAX_CATS:
            kitty = Cat()
            cats.append(kitty)
            print(cats[-1].birth())
            count += 1
        elif 20 < rand < 30:
            print(random.choice(cats).eat())
        elif 30 < rand < 40:
            print(random.choice(cats).drink())
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

        # check birthday
        for cat in cats:
            if (time.time() - cat.birthday) > 600:
                print(cat.happy_birthday())

    return cats


if __name__ == '__main__':
    cat_list = []

    player = Player()
    print(f"Welcome to your cat house, {player.name}!")
    while True:
        cat_list = cat_loop(5, cat_list)
        desire = input("What would you like to do? "
                       "You can feed a kitty, play with one, call one over or just watch them.\n")
        if desire.lower().startswith("feed"):
            print(player.feed(random.choice(cat_list)))
        elif desire.lower().startswith("play"):
            print(player.play_with(random.choice(cat_list)))
        elif desire.lower().startswith("call"):
            print(player.bring_item(random.choice(cat_list)))
        elif desire.lower().startswith("watch"):
            cat_list = cat_loop(10, cat_list)
        else:
            print("I didnt catch that. Lets watch them!")
