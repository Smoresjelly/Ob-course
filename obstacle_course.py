class ObstacleCourse:
    def __init__(self):
        self.obstacles = []

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def navigate(self):
        for obstacle in self.obstacles:
            if not obstacle.pass_obstacle():
                print(f"Obstacle {obstacle.name} is blocking the way!")
                return False
        print("Congratulations! You've completed the obstacle course!")
        return True

class Obstacle:
    def __init__(self, name):
        self.name = name

    def pass_obstacle(self):
        raise NotImplementedError("Subclasses must implement pass_obstacle method!")

class Wall(Obstacle):
    def pass_obstacle(self):
        print(f"Jumping over the {self.name}!")
        return True

class River(Obstacle):
    def pass_obstacle(self):
        print(f"Swimming across the {self.name}!")
        return True

if __name__ == "__main__":
    course = ObstacleCourse()
    course.add_obstacle(Wall("Brick Wall"))
    course.add_obstacle(River("Fast-flowing River"))
    course.add_obstacle(Wall("Wooden Fence"))

    course.navigate()
