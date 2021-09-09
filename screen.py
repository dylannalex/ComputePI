import pygame
from random import randint


class Dot:
    RADIUS = 2

    def __init__(self, win, screen_side_length, color):
        self.x = randint(0, screen_side_length)
        self.y = randint(0, screen_side_length)
        self._draw(win, color)

    def in_circle(self, circle_radius):
        """
        Returns True if dot is inside the screen circle, else returns False.
        """
        fixed_x = self.x - circle_radius
        fixed_y = circle_radius - self.y

        if fixed_x ** 2 + fixed_y ** 2 <= circle_radius ** 2:
            return True

        return False

    def _draw(self, win, color):
        """
        Draws the dot at a random place on screen.
        """
        pygame.draw.circle(win, color, (self.x, self.y), Dot.RADIUS)
        pygame.display.update()


class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.radius, self.radius), self.radius)
        pygame.display.update()


class Screen:
    def __init__(self, circle_radius, screen_color, circle_color, dot_color):
        self._screen_side_length = circle_radius * 2
        self._screen_area = self._screen_side_length ** 2
        self._win = pygame.display.set_mode((circle_radius * 2, circle_radius * 2))
        self._circle = Circle(circle_radius, circle_color)
        self._screen_color = screen_color
        self.dot_color = dot_color
        self.clear()

    def clear(self):
        """
        Redraws the screen. Dots drawn are removed.
        """
        self._win.fill(self._screen_color)
        self._circle.draw(self._win)
        self._dots = []
        self._dots_in_circle = 0

    def start_simulation(self, total_dots, show_steps=True):
        """
        Starts filling the screen with dots for computing PI.
        """
        for _ in range(total_dots):
            dot = Dot(self._win, self._screen_side_length, self.dot_color)
            self._dots.append(dot)
            if dot.in_circle(self._screen_side_length):
                self._dots_in_circle += 1
            if show_steps:
                print(self.compute_pi())

    def compute_pi(self):
        """
        Computes PI by estimating the area of the circle by counting the number
        of dots that fell in the circle and those which don't.
        Since circle area is PI * r ** 2 (where r is the radius of the circle),
        PI can be calculated by dividing the area of the circle by r ** 2.

                        A = PI * r ** 2 --> PI = A / (r ** 2)
        """
        dots_in_circle = self._dots_in_circle
        total_dots = len(self._dots)
        estimated_circle_area = self._screen_area * (dots_in_circle / total_dots)
        return estimated_circle_area / (self._circle.radius ** 2)

    def wait(self, milliseconds):
        pygame.time.wait(milliseconds)
