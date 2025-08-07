import pygame
from input_manager import InputManager
from snake_engine import SnakeEngine
from food_system import FoodSystem
from score_tracker import ScoreTracker
from renderer import Renderer

class GameController:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.fps = 30
        
        # Inicializar módulos
        self.input_manager = InputManager()
        self.snake = SnakeEngine()
        self.food_system = FoodSystem()
        self.score_tracker = ScoreTracker()
        self.renderer = Renderer(self.screen)
        
        self.game_over = False

    def start_game(self):
        self.run_game_loop()

    def run_game_loop(self):
        running = True
        while running:
            # Manejo de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Lógica principal aquí
            # ...
            
            pygame.display.flip()
            self.clock.tick(self.fps)
        
        pygame.quit()