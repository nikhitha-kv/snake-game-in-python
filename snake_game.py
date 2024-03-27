import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

class Snake:
    def __init__(self):
        self.body = [(200, 200), (210, 200), (220, 200)]
        self.direction = 'RIGHT'

    def move(self):
        head = list(self.body[0])
        if self.direction == 'UP':
            head[1] -= GRID_SIZE
        elif self.direction == 'DOWN':
            head[1] += GRID_SIZE
        elif self.direction == 'LEFT':
            head[0] -= GRID_SIZE
        elif self.direction == 'RIGHT':
            head[0] += GRID_SIZE
        self.body.insert(0, tuple(head))
        self.body.pop()

    def grow(self):
        tail = list(self.body[-1])
        self.body.append(tuple(tail))

    def draw(self, win):
        for segment in self.body:
            pygame.draw.rect(win, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

class Food:
    def __init__(self):
        self.x = random.randrange(0, WIDTH - GRID_SIZE, GRID_SIZE)
        self.y = random.randrange(0, HEIGHT - GRID_SIZE, GRID_SIZE)

    def draw(self, win):
        pygame.draw.rect(win, RED, (self.x, self.y, GRID_SIZE, GRID_SIZE))

def game_over(win):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Game Over!", True, BLACK)
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(2000)

def main():
    snake = Snake()
    food = Food()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != 'DOWN':
                    snake.direction = 'UP'
                elif event.key == pygame.K_DOWN and snake.direction != 'UP':
                    snake.direction = 'DOWN'
                elif event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                    snake.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                    snake.direction = 'RIGHT'

        snake.move()

        if snake.body[0] == (food.x, food.y):
            snake.grow()
            food = Food()

        if (snake.body[0][0] < 0 or snake.body[0][0] >= WIDTH or
            snake.body[0][1] < 0 or snake.body[0][1] >= HEIGHT or
            snake.body[0] in snake.body[1:]):
            running = False

        win.fill(WHITE)
        snake.draw(win)
        food.draw(win)
        pygame.display.update()
        clock.tick(10)

    game_over(win)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
