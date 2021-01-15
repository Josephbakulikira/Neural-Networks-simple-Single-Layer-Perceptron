import pygame

class Point:
    def __init__(self, x, y, breed):
        self.x = x
        self.y = y
        self.breed = breed
        self.color = (255, 255, 255)

        if self.breed == 1:
            self.color = (255, 1, 54)
        else:
            self.color = (136, 255, 1)
    def GetInputs(self):
        return [self.x, self.y]
    def Display(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 8)
