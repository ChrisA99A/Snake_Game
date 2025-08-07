class SnakeEngine:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]  # Segmentos iniciales
        self.direction = "RIGHT"
        self.grow_pending = False

    def move(self):
        # Implementar movimiento según diagrama
        pass

    def check_collision(self):
        # Implementar detección de colisiones
        return False