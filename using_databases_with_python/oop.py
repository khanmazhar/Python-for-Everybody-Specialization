# class PartyAnimal:
#     x = 0

#     def __init__(self):
#         print("I am constructed")

#     def increase(self):
#         self.x = self.x+1
#         print('X:', self.x)

#     def __del__(self):
#         print('I am destructed')


# an = PartyAnimal()
# an.increase()
# an.increase()
# an.increase()
# an = 42
# print("an contains", an)

# class PartyAnimal:
#     x = 0
#     name = ""

#     def __init__(self, name):
#         self.name = name
#         print(self.name, " constructed!")

#     def party(self):
#         self.x += 1
#         print(self.name, " is now", self.x)


# s = PartyAnimal("Sally")
# s.party()

# j = PartyAnimal("Jim")
# j.party()
# s.party()


class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, name):
        self.name = name
        print(self.name, " constructed! with value", self.x)

    def party(self):
        self.x += 1
        print(self.name, " is now", self.x)


class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points += 7
        print(self.name, " has now points", self.points)
        self.party()
        print(self.name, " has x", self.x)


s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.touchdown()
j.party()
