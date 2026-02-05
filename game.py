from walle import WallE
from yolovision import YoloVision

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.walle = WallE(self.screen)
        self.current_names = []
        self.boxes_as_been_detected = False

    def update(self, screen, seen):
        screen.blit(self.walle.image, self.walle.rect)
        self.current_names = []

        # Wall-E
        self.walle.update()
        self.walle.update_life_bar(screen)

        if seen[0]:
            for box in seen[0].boxes:
                class_id = int(box.cls[0])
                name = seen[0].names[class_id]

                self.current_names.append(name)

            self.boxes_as_been_detected = True

        if not 'person' in self.current_names and self.boxes_as_been_detected:
            self.walle.sleep()

        elif 'person' in self.current_names and self.boxes_as_been_detected:
            self.walle.wake_up()
