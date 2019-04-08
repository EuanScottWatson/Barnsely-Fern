import pygame, os, random
from pygame.locals import *


class Fern:
    def __init__(self):
        self.points = []

        self.x = 0
        self.y = 0

    def display(self, screen):
        for point in self.points:
            if point[1] <= 142:
                pygame.draw.circle(screen, (244, 66, 223), point, 1, 0)
            elif point[1] <= 284:
                pygame.draw.circle(screen, (179, 66, 244), point, 1, 0)
            elif point[1] <= 426:
                pygame.draw.circle(screen, (66, 104, 244), point, 1, 0)
            elif point[1] <= 568:
                pygame.draw.circle(screen, (66, 244, 80), point, 1, 0)
            elif point[1] <= 710:
                pygame.draw.circle(screen, (241, 244, 66), point, 1, 0)
            elif point[1] <= 852:
                pygame.draw.circle(screen, (244, 122, 66), point, 1, 0)
            else:
                pygame.draw.circle(screen, (255, 0, 0), point, 1, 0)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return True

    def next_point(self):
        r = random.random()
        if r <= 0.01:
            next_x = 0
            next_y = 0.16 * self.y
        elif r <= 0.86:
            next_x = 0.85 * self.x + 0.04 * self.y
            next_y = -0.04 * self.x + 0.85 * self.y + 1.6
        elif r <= 0.93:
            next_x = 0.2 * self.x - 0.26 * self.y
            next_y = 0.23 * self.x + 0.22 * self.y + 1.6
        else:
            next_x = -0.15 * self.x + 0.28 * self.y
            next_y = 0.26 * self.x + 0.24 * self.y + 0.44
        self.x = next_x
        self.y = next_y
        self.points.append([900 + int(self.x*100), 1000-int(self.y*100)])

    def display_screen(self, screen):
        screen.fill((0, 0, 0))

        self.display(screen)

        pygame.display.update()
        pygame.display.flip()

    def run_logic(self):
        self.next_point()


def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Barnsley Fern")

    os.environ['SDL_VIDEO_CENTERED'] = "True"

    width, height = 1800, 1000

    screen = pygame.display.set_mode((width, height))

    done = False
    clock = pygame.time.Clock()
    barnsley = Fern()

    while not done:
        done = barnsley.events()
        barnsley.run_logic()
        barnsley.display_screen(screen)

        clock.tick(120)


if __name__ == "__main__":
    main()
