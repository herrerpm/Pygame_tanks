import pygame


class Figure:
    def __init__(self, screen, position, color):
        self.screen = screen
        self.x, self.y = position
        self.color = color


class Square(Figure):
    """The square class creates a square on the pygame screen
    with the coordinates provided for its top left corner"""

    def __init__(self, screen, position, color, width, height):
        super().__init__(screen, position, color)
        self.width = width
        self.height = height

    def display(self, pos=None):
        """The create method displays the square object to the screen
        after it is initialized"""
        if pos:
            addx, addy = pos
            self.x += addx
            self.y += addy
        pygame.draw.rect(
            self.screen,
            self.color,
            (self.x,
             self.y,
             self.width,
             self.height)
            )


class Circle(Figure):

    def __init__(self, screen, position, color, radius):
        super().__init__(screen, position, color)
        self.radius = radius

    def display(self, pos=None):
        """The create method displays the square object to the screen
        after it is initialized"""
        if pos:
            addx, addy = pos
            self.x += addx
            self.y += addy
        pygame.draw.circle(self.screen,
                           self.color,
                           (self.x, self.y),
                           self.radius)


class Text(Figure):
    """The text class displays text into a pygame screen"""
    def display(self, font, message):
        img = font.render(message, True, self.color)
        self.screen.blit(img, (self.x, self.y))
