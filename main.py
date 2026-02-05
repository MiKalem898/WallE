import cv2
import pygame
from game import Game
from yolovision import YoloVision

FPS = 60
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, FPS / 2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

clock = pygame.time.Clock()
# clock.tick(FPS)
pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Wall-E")
pygame.display.set_icon(pygame.image.load("./assets/actions/idle/walle0.png"))
bg = pygame.image.load('./assets/bg.png')
bg = pygame.transform.scale(bg, (1200, 700))

game = Game(screen)
yolo = YoloVision()

while True:
    ret, frame = cap.read()

    seen = yolo.see(frame)

    screen.blit(bg, (0, 0))
    game.update(screen, seen)

    pygame.display.flip()

    if cv2.waitKey(1) == ord('a'):
        pygame.quit()
        break

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            break
