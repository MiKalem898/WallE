import pygame
import animation

class WallE(animation.AminateSprite):
    def __init__(self, screen):
        super().__init__('walle', 'idle')
        self.image = pygame.transform.scale(self.image, (306, 384))
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_size()[0] / 3 - self.rect.width / 2
        self.rect.y = screen.get_size()[1] / 2 - self.rect.height / 2
        self.is_sleeping = False
        self.start_animation()
        self.life = 100

    def update(self):
        self.animate('advance', loop=not self.is_animating_once)

        if not self.is_animating_once:
            if not self.is_sleeping and self.action == 'sleep':
                self.start_animation('idle', direction='advance', loop=True)

    def update_life_bar(self, surface):
        bw = surface.get_width() * .33 - 35
        bh = 7
        bx = surface.get_width() * .66 + 30
        by = 20

        bg_position = [bx, by, bw, bh]
        bar_position = [bx, by, bw, bh / 100 * self.life]

        pygame.draw.rect(surface, (255, 153, 153), bg_position)
        pygame.draw.rect(surface, (255, 77, 77), bar_position)

    def sleep(self):
        if not self.is_animating_once and not self.is_sleeping:
            print('Sleeping')
            self.is_sleeping = True
            self.is_animating_once = True
            self.start_animation('sleep', 'advance', False)


    def wake_up(self):
        if not self.is_animating_once and self.is_sleeping:
            print('Wake up')
            self.is_sleeping = False
            self.is_animating_once = True
            self.start_animation('sleep', 'reverse', False)
