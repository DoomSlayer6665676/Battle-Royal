from constants import WINDOW_WIGHT, WINDOW_HEIGHT


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

        self.global_dy = 0
        self.global_dx = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dy = -(target.rect.y + target.rect.h // 2 - WINDOW_HEIGHT // 2)
        self.dx = -(target.rect.x + target.rect.w // 2 - WINDOW_WIGHT // 2)


camera = Camera()
