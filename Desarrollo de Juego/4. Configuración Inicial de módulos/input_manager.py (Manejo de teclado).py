class InputManager:
    def __init__(self):
        self.direction = "RIGHT"  # Dirección inicial

    def get_direction(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]: 
            return "UP"
        elif keys[pygame.K_DOWN]: 
            return "DOWN"
        # ... completar otras direcciones
        return self.direction