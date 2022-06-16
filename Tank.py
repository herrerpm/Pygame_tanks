import pygame_utils


class Tank(pygame_utils.Figure):
    SPEED = 5

    def __init__(self, screen, position, color, angle):
        super().__init__(screen, position, color)
        self.canon_angle = angle
        self.body = pygame_utils.Square(screen, (self.x, self.y), self.color, 100, 30)
        self.top = pygame_utils.Square(screen, (self.body.x + ((self.body.width - 70) / 2), self.body.y - 20),
                                       self.color, 70, 20)
        self.canon = pygame_utils.Square(screen, (self.top.x + (self.top.width / 2), self.top.y), (0, 0, 0), 70, 5)
        self.first_wheel = pygame_utils.Circle(screen, (self.top.x, self.body.y + (self.body.height + 10)), (0, 0, 0),
                                               15)
        self.second_wheel = pygame_utils.Circle(screen,
                                                (self.top.x + self.top.width, self.body.y + (self.body.height + 10)),
                                                (0, 0, 0), 15)
        self.components = (
            self.body,
            self.canon,
            self.top,
            self.first_wheel,
            self.second_wheel
        )

    def display(self, pos=None):
        if pos:
            addx, addy = pos
            self.x += addx
            self.y += addy
            for i in self.components:
                i.display(pos)
        else:
            for i in self.components:
                i.display()