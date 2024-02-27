import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen_width = 700
        self.screen_height = 700
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.levelx = 0
        self.levely = 0
        self.colors = [
            (0, 0, 0),         # color 0 (black)
            (0, 0, 255),       # Color 1 (blue)
            (0, 255, 0),       # Color 2 (green)
            (255, 0, 0),       # Color 3 (red)
            (255, 255, 0),     # Color 4 (yellow)
            (255, 255, 255),   # Color 5 (white)
            (0, 255, 255),     # Color 6 (cyan)
            (255, 0, 255),     # Color 7 (magenta)
            (255, 128, 0),     # color 8 (orange)
            (175, 175, 175)    # color 9 (gray)
        ]
        self.player = Player(self)
        self.platforms = []  # Platforms list is initially empty

        # Create dictionaries to store color change rectangles for each level
        self.color_rectangles= []

        # Create a list to store color-sensitive platforms for each level
        self.color_sensitive_platforms= []

    def run(self):
        while True:
            self.screen.fill(self.colors[5])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.levely == 0:
                if self.levelx == 0:
                    self.first_level()
                elif self.levelx == 1:
                    self.second_level()
                elif self.levelx == -1:
                    self.third_level()
            elif self.levely == 1:
                if self.levelx == 0:
                    self.level_1_y()

            self.player.update()
            self.player.box_collision()

            pygame.display.flip()
            self.clock.tick(60)

    def first_level(self):
        # Set the positions of platforms for level 1
        self.platforms = [
            Platform(0, 400, 100, 25),
            Platform(200, 500, 100, 25),
            Platform(0, 700, 700, 25),
            Platform(200, 200, 100, 25),
            Platform(0, 100, 100, 25)
        ]

        self.color_rectangles = {
            self.colors[1]: pygame.Rect(400, 600, self.player.player_width, self.player.player_height),
            self.colors[2]: pygame.Rect(500, 600, self.player.player_width, self.player.player_height),
            self.colors[3]: pygame.Rect(300, 600, self.player.player_width, self.player.player_height)
        }

        self.color_sensitive_platforms = [
            ColorPlatform(400, 300, 25, 100, self.colors[1], 0),
            ColorPlatform(600, 300, 25, 100, self.colors[2], 0),
            ColorPlatform(500, 400, 25, 100, self.colors[3], 0)
        ]

        # Draw platforms
        for platform in self.platforms:
            platform.draw(self.screen, self.colors[0])  # Draw platforms with a contrasting color

        # Draw player, reset block, colored blocks, and door
        pygame.draw.rect(self.screen, self.colors[0], self.player.color_rect_reset)
        pygame.draw.rect(self.screen, self.player.current_color, self.player.player_rect)

        # Draw color change rectangles with their respective colors for level 1
        for color, color_rect in self.color_rectangles.items():
            pygame.draw.rect(self.screen, color, color_rect)

        # Handle player collision with color change rectangles
        for color, color_rect in self.color_rectangles.items():
            if self.player.current_color == self.colors[9] and self.player.player_rect.colliderect(color_rect):
                self.player.current_color = color
        
        # Draw color-sensitive platforms for level 1
        for platform in self.color_sensitive_platforms:
            pygame.draw.rect(self.screen, platform.required_color, platform.rect)

        # Handle player collision with color-sensitive platforms
        self.player.handle_color_sensitive_platforms()

    def second_level(self):
        # Set the positions of platforms for level 2
        self.platforms = [
            Platform(500, 300, 100, 25),
            Platform(0, 550, 100, 25),
            Platform(0, 700, 700, 25)
        ]

        self.color_rectangles = {
            self.colors[1]: pygame.Rect(100, 500, self.player.player_width, self.player.player_height),
            self.colors[2]: pygame.Rect(600, 400, self.player.player_width, self.player.player_height),
            self.colors[3]: pygame.Rect(200, 600, self.player.player_width, self.player.player_height)
        }

        self.color_sensitive_platforms = [
            ColorPlatform(100, 500, 100, 25, self.colors[1], 1),
            ColorPlatform(600, 400, 100, 25, self.colors[2], 1),
            ColorPlatform(200, 600, 100, 25, self.colors[3], 1)
        ]

        # Draw platforms
        for platform in self.platforms:
            platform.draw(self.screen, self.colors[0])  # Draw platforms with a contrasting color

        # Draw player, reset block, colored blocks, and door
        pygame.draw.rect(self.screen, self.colors[0], self.player.color_rect_reset)
        pygame.draw.rect(self.screen, self.player.current_color, self.player.player_rect)

        # Draw color change rectangles with their respective colors for level 2
        for color, color_rect in self.color_rectangles.items():
            pygame.draw.rect(self.screen, color, color_rect)

        # Handle player collision with color change rectangles
        for color, color_rect in self.color_rectangles.items():
            if self.player.current_color == self.colors[9] and self.player.player_rect.colliderect(color_rect):
                self.player.current_color = color

        # Draw color-sensitive platforms for level 2
        for platform in self.color_sensitive_platforms:
            pygame.draw.rect(self.screen, platform.required_color, platform.rect)

        # Handle player collision with color-sensitive platforms
        self.player.handle_color_sensitive_platforms()
    
    def third_level(self):
        # Set the positions of platforms for level 3
        self.platforms = [
            Platform(100, 300, 100, 25),
            Platform(400, 500, 100, 25),
            Platform(0, 700, 700, 25)
        ]

        self.color_rectangles = {
            self.colors[1]: pygame.Rect(200, 600, self.player.player_width, self.player.player_height),
            self.colors[2]: pygame.Rect(500, 400, self.player.player_width, self.player.player_height),
            self.colors[3]: pygame.Rect(300, 600, self.player.player_width, self.player.player_height)
        }

        self.color_sensitive_platforms = [
            ColorPlatform(200, 600, 100, 25, self.colors[1], 2),
            ColorPlatform(500, 400, 100, 25, self.colors[2], 2),
            ColorPlatform(300, 600, 100, 25, self.colors[3], 2)
        ]

        # Draw platforms
        for platform in self.platforms:
            platform.draw(self.screen, self.colors[0])  # Draw platforms with a contrasting color

        pygame.draw.rect(self.screen, self.colors[0], self.player.color_rect_reset)
        pygame.draw.rect(self.screen, self.player.current_color, self.player.player_rect)

        # Draw color change rectangles with their respective colors for level 3
        for color, color_rect in self.color_rectangles.items():
            pygame.draw.rect(self.screen, color, color_rect)

        # Handle player collision with color change rectangles
        for color, color_rect in self.color_rectangles.items():
            if self.player.current_color == self.colors[9] and self.player.player_rect.colliderect(color_rect):
                self.player.current_color = color

        # Draw color-sensitive platforms for level 3
        for platform in self.color_sensitive_platforms:
            pygame.draw.rect(self.screen, platform.required_color, platform.rect)

        # Handle player collision with color-sensitive platforms
        self.player.handle_color_sensitive_platforms()

    def level_1_y(self):
        # Set the positions of platforms for level 3
        self.platforms = [
            Platform(100, 300, 100, 25),
            Platform(400, 500, 100, 25),
            Platform(50, 675, 500, 25)
        ]

        self.color_rectangles = {
            self.colors[1]: pygame.Rect(200, 600, self.player.player_width, self.player.player_height),
            self.colors[2]: pygame.Rect(500, 400, self.player.player_width, self.player.player_height),
            self.colors[3]: pygame.Rect(300, 600, self.player.player_width, self.player.player_height)
        }

        self.color_sensitive_platforms = [
            ColorPlatform(0, 400, 100, 25, self.colors[1], 2),
            ColorPlatform(500, 400, 100, 25, self.colors[2], 2),
            ColorPlatform(300, 300, 100, 25, self.colors[3], 2)
        ]

        # Draw platforms
        for platform in self.platforms:
            platform.draw(self.screen, self.colors[0])  # Draw platforms with a contrasting color

        pygame.draw.rect(self.screen, self.colors[0], self.player.color_rect_reset)
        pygame.draw.rect(self.screen, self.player.current_color, self.player.player_rect)

        # Draw color change rectangles with their respective colors for level 3
        for color, color_rect in self.color_rectangles.items():
            pygame.draw.rect(self.screen, color, color_rect)

        # Handle player collision with color change rectangles
        for color, color_rect in self.color_rectangles.items():
            if self.player.current_color == self.colors[9] and self.player.player_rect.colliderect(color_rect):
                self.player.current_color = color

        # Draw color-sensitive platforms for level 3
        for platform in self.color_sensitive_platforms:
            pygame.draw.rect(self.screen, platform.required_color, platform.rect)

        # Handle player collision with color-sensitive platforms
        self.player.handle_color_sensitive_platforms()

class Player:
    def __init__(self, game):
        self.game = game
        self.player_width = 50
        self.player_height = 100
        self.player_rect = pygame.Rect(10, self.game.screen_height - self.player_height, self.player_width, self.player_height)
        self.is_jumping = False
        self.gravity = 1  # Adjust the gravity
        self.y_velocity = 0
        self.current_color = self.game.colors[9]
        self.color_rect_reset = pygame.Rect(0, 600, self.player_width, self.player_height)

    def player_control(self):
        key_state = pygame.key.get_pressed()
        speed = 10  # Adjust this value as needed

        # Store the previous position of the player
        prev_x = self.player_rect.x
        prev_y = self.player_rect.y

        if key_state[pygame.K_d] or key_state[pygame.K_RIGHT]:
            self.player_rect.x += speed
        if key_state[pygame.K_a] or key_state[pygame.K_LEFT]:
            self.player_rect.x -= speed

        if key_state[pygame.K_w] or key_state[pygame.K_UP]:
            if not self.is_jumping:
                self.y_velocity = -20  # Adjust the jump strength as needed
                self.is_jumping = True

        # Apply gravity continuously
        self.y_velocity += self.gravity

        # Update player's position
        self.player_rect.y += self.y_velocity

        # Check for collisions with platforms and adjust position
        for platform in self.game.platforms:
            if self.player_rect.colliderect(platform.rect):
                if self.y_velocity > 0:
                    self.player_rect.y = platform.rect.top - self.player_height
                    self.y_velocity = 0
                    self.is_jumping = False
                elif self.y_velocity < 0:
                    self.player_rect.y = platform.rect.bottom
                    self.y_velocity = 0
                else:
                    # If the player was moving horizontally, adjust the position to avoid passing through the platform
                    if prev_x < platform.rect.left:
                        self.player_rect.right = platform.rect.left
                    elif prev_x > platform.rect.right:
                        self.player_rect.left = platform.rect.right

                    # Reset y-velocity and jumping flag
                    self.y_velocity = 0
                    self.is_jumping = False

    def color_change(self):
        current_level_color_rectangles = self.game.color_rectangles
        if(self.player_rect.colliderect(self.color_rect_reset)):
            self.current_color = self.game.colors[9]

        for color, color_rect in current_level_color_rectangles.items():
            if self.current_color == self.game.colors[9] and self.player_rect.colliderect(color_rect):
                self.current_color = color
            if self.current_color == self.game.colors[1] and self.player_rect.colliderect(color_rect):
                if(color == self.game.colors[2]):
                    self.current_color = self.game.colors[6]
                if(color == self.game.colors[3]):
                    self.current_color = self.game.colors[7]
            if self.current_color == self.game.colors[2] and self.player_rect.colliderect(color_rect):
                if(color == self.game.colors[1]):
                    self.current_color = self.game.colors[6]
                if(color == self.game.colors[3]):
                    self.current_color = self.game.colors[4]
            if self.current_color == self.game.colors[3] and self.player_rect.colliderect(color_rect):
                if(color == self.game.colors[1]):
                    self.current_color = self.game.colors[7]
                if(color == self.game.colors[2]):
                    self.current_color = self.game.colors[4]
            if self.current_color == self.game.colors[4] and self.player_rect.colliderect(color_rect):
                if(color == self.game.colors[1]):
                    self.current_color = self.game.colors[2]
                if(color == self.game.colors[3]):
                    self.current_color = self.game.colors[8]

    def box_collision(self):
        if self.player_rect.right >= self.game.screen_width:
            if(self.game.levelx<1):
                self.game.levelx+=1
                self.player_rect.x=50
            else: 
                self.player_rect.right = self.game.screen_width
        if self.player_rect.bottom >= self.game.screen_height:
            if(self.game.levely>0):
                self.game.levely-=1
                self.player_rect.bottom=50
            else:
                self.player_rect.bottom = self.game.screen_height
        if self.player_rect.bottom <= 0:
            self.game.levely+=1
            self.player_rect.bottom=self.game.screen_height-50
        if self.player_rect.left <= 0:
            if(self.game.levelx>-1):
                self.game.levelx-=1
                self.player_rect.left=self.game.screen_width-50
            else: 
                self.player_rect.left = 0

    def handle_color_sensitive_platforms(self):
        current_level_platforms = self.game.color_sensitive_platforms

        for platform in current_level_platforms:
            if self.player_rect.colliderect(platform.rect):
                if self.current_color != platform.required_color:
                    # The player has the incorrect color and should fall through the platform
                    self.player_rect.y = platform.rect.bottom
                    self.y_velocity = 0
                    self.is_jumping = False

    def update(self):
        self.player_control()
        self.color_change()
        self.handle_color_sensitive_platforms()

class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)

class ColorPlatform:
    def __init__(self, x, y, width, height, required_color, level):
        self.rect = pygame.Rect(x, y, width, height)
        self.required_color = required_color
        self.level = level
        
# moving platform

# menu

if __name__ == "__main__":
    game = Game()
    game.run()