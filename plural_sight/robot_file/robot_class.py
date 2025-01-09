class Robot:
    # class variable
    robot_armor = "Titanium"

    def __init__(
        self,
        name: str,
    ):
        # instance variable
        self.name = name
        self.position = [0, 0]
        print(f"My name is, {name}!")

    def walk(self, x, y):
        self.position[0] = x + y
        print(f"New position: {self.position}")
