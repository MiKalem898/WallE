import pygame
import os

class AminateSprite(pygame.sprite.Sprite):
    def __init__(self, name, action):
        super().__init__()
        self.image = pygame.image.load(f'./assets/actions/{action}/{name}0.png')
        self.current_image = 0
        self.images = anims.get(action)[0]
        self.is_animating_once = False
        self.is_animating = False
        self.name = name
        self.animating_once = [False, '']
        self.action = 'idle'
        self.current_delay = 0

    def start_animation(self, action='idle', direction='advance', loop=False):
        self.is_animating = True
        self.action = action
        self.current_delay = 0
        self.current_image = 0

        self.images = anims.get(self.action)[0]
        if direction == 'reverse':
            self.images = list(reversed(self.images))

        self.animate(direction, loop)

    def animate(self, direction, loop=False):
        if self.is_animating:
            delay = anims.get(self.action)[1]

            if self.current_delay >= delay:
                self.current_image += 1
                self.current_delay = 0

            else:
                self.current_delay += 1

            if not loop and self.current_image == len(self.images):
                self.is_animating = False
                self.is_animating_once = False
                self.current_image = 0

            else:
                if self.current_image == len(self.images):
                    self.current_image = 0

                self.image = self.images[self.current_image]
                self.image = pygame.transform.scale(self.image, (306, 384))


def load(name, action):
    imgs = []

    for file in os.listdir(f'./assets/actions/{action}'):
        imgs.append(pygame.image.load(f'./assets/actions/{action}/{file}'))

    return imgs

anims = {
    'idle': (load('walle', 'idle'), 9),
    'sleep': (load('walle', 'sleep'), 7)
}
