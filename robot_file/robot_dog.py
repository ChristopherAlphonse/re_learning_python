from robot_class import Robot


class RobotDog(Robot):

    def robot_bark(self):
        print("Wooof")


dog = RobotDog("Marco")
dog.robot_bark()
dog.walk(10, 0)


# inheritance drills
