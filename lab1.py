class Jack:
    jack_count: int = 0

    def __init__(self, colour="", mass=0, maker="", max_lifting_weight=0, material="", type="", height=0):
        self.colour = colour
        self.mass = mass
        self.maker = maker
        self.max_lifting_weight = max_lifting_weight
        self.material = material
        self.type = type
        self.height = height

    def __str__(self) -> str:
        return f"Jack:\n colour: {self.colour}\n mass: {self.mass} kg\n maker: {self.maker}\n"\
               f"max_lifting_weight: {self.max_lifting_weight} ton\n type: {self.type}\n height: {self.type} cm\n"

    def __del__(self):
        del self

    @classmethod
    def get_jack_count(cls) -> int:
        return cls.jack_count

def main():
    domkrat1 = Jack("red", 5, "Nokia", 2, "mechanic", 70 )
    domkrat2 = Jack("green", 3, "Apple", 1, "electric", 40)

    print(domkrat1)
    print(domkrat2)

    Jack.get_jack_count()


if __name__ == "__main__":
    main()
