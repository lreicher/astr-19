# Lucas Reicher Prompt #4 Coding Journal #1

class FavAnimal():
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def print(self):
        print("Arm Length: " + str(self.arm_length))
        print("Leg Length: " + str(self.leg_length))
        print("Number of Eyes: " + str(self.num_eyes))
        print("Has a Tail: " + str(self.has_tail))
        print("Is Furry: " + str(self.is_furry))

def main():
    dog = FavAnimal(3.223, 3.234, 2, True, True)
    dog.print()

if __name__ == "__main__":
    main()
