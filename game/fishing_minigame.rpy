# Fishing Minigame for Ren'Py
# Adapted from the Pygame version

init python:
    import random
    import time
    import math
    
    # Define the FishingMinigame class
    class FishingMinigame:
        def __init__(self):
            # Game dimensions
            self.WIDTH, self.HEIGHT = 1440, 810
            
            # Game elements positions and sizes
            self.container_x = (self.WIDTH // 2) + 40
            self.container_y = 50
            self.container_width = 60
            self.container_height = self.HEIGHT - 100
            
            # Bobber properties
            self.bobber_x = (self.WIDTH // 2) - 120
            self.bobber_y = (self.container_y + self.container_height // 2) - 80
            self.bobber_width = 80
            self.bobber_height = 160
            self.bobber_speed = 5
            self.bobber_direction = 1  # Default to moving down
            
            # Fish properties
            self.fish_x = (self.WIDTH // 2) - 115
            self.fish_y = random.randint(self.container_y, self.container_y + self.container_height - 70)
            self.fish_width = 70
            self.fish_height = 70
            self.fish_speed = 2
            self.fish_direction = 1
            
            # Catching mechanics
            self.catch_time = 0
            self.catch_threshold = 5000  # Time in milliseconds required to catch the fish
            self.catch_decrement = 50  # Decrement speed for the catch time when the bobber loses the fish
            
            # Timer
            self.timer_start = 10  # 10 seconds countdown
            self.timer = self.timer_start
            self.last_time = time.time()
            
            # Game state
            self.game_over = False
            self.caught = False
            self.game_over_text = ""
            
            # Load images
            self.load_images()
        
        def load_images(self):
            # In Ren'Py, we'll use the Image function to load images
            # These paths are relative to the game directory
            self.background_image = "fishing-minigame/water.png"
            self.bobber_image = "fishing-minigame/bobber.png"
            self.fish_image = "fishing-minigame/fish.png"
            self.catch_text_image = "fishing-minigame/catch-text.png"
            self.away_text_image = "fishing-minigame/away-text.png"
        
        def reset_game(self):
            self.bobber_y = (self.container_y + self.container_height // 2) - 80
            self.fish_y = random.randint(self.container_y, self.container_y + self.container_height - 70)
            self.catch_time = 0
            self.game_over = False
            self.caught = False
            self.timer = self.timer_start
            self.last_time = time.time()
            self.game_over_text = ""
        
        def move_fish(self, dt):
            # Occasionally change the fish's speed and direction
            if random.randint(0, 100) < 5:  # 5% chance to change direction and speed
                self.fish_direction = random.choice([-1, 1])
                self.fish_speed = random.randint(2, 6)  # Random speed between 2 and 6
            
            self.fish_y += self.fish_speed * self.fish_direction * dt * 30  # Scale by dt and target 30 FPS
            self.fish_y = max(self.container_y, min(self.fish_y, self.container_y + self.container_height - self.fish_height))
        
        def update(self, dt):
            if not self.game_over:
                # Update timer
                self.timer -= dt
                if self.timer <= 0:
                    self.timer = 0
                    self.game_over = True
                    self.game_over_text = "IT SWAM AWAY..."
                
                # Move the bobber based on mouse position
                mouse_y = renpy.get_mouse_pos()[1]
                target_y = mouse_y - self.bobber_height / 2
                self.bobber_y += (target_y - self.bobber_y) * 0.1
                self.bobber_y = max(self.container_y, min(self.bobber_y, self.container_y + self.container_height - self.bobber_height + 2))
                
                # Move the fish
                self.move_fish(dt)
                
                # Check collision
                if self.check_collision():
                    self.catch_time += dt * 1000  # Convert to milliseconds
                    if self.catch_time >= self.catch_threshold and not self.game_over:
                        self.game_over = True
                        self.caught = True
                        self.game_over_text = "IT'S A CATCH!"
                else:
                    self.catch_time -= self.catch_decrement * dt
                    self.catch_time = max(0, self.catch_time)  # Ensure catch_time doesn't go below 0
            
            # Additional check to ensure game state consistency
            if self.game_over and not self.caught:
                self.game_over_text = "IT SWAM AWAY..."
        
        def check_collision(self):
            # Simple rectangle collision detection
            return (self.bobber_x < self.fish_x + self.fish_width and
                    self.bobber_x + self.bobber_width > self.fish_x and
                    self.bobber_y < self.fish_y + self.fish_height and
                    self.bobber_y + self.bobber_height > self.fish_y)
    
    # Create a global instance of the fishing minigame
    fishing_game = FishingMinigame()
    
    # Function to run the fishing minigame
    def run_fishing_minigame():
        # Reset the game state
        fishing_game.reset_game()
        
        # Return to this label when the minigame is done
        renpy.call_screen("fishing_minigame_screen")
        
        # Return the result (True if caught, False if not)
        return fishing_game.caught
    
    # Function to update the game state (called by the timer)
    def update_fishing_game():
        # Calculate delta time
        current_time = time.time()
        dt = current_time - fishing_game.last_time
        fishing_game.last_time = current_time
        
        # Update game state
        fishing_game.update(dt)

# Define the fishing minigame screen
screen fishing_minigame_screen():
    modal True
    
    # Add a timer event that updates the game state
    timer 0.033 repeat True action Function(update_fishing_game)
    
    # Background
    add fishing_game.background_image
    
    # Only show game elements if the game is not over
    if not fishing_game.game_over:
        # Bobber
        add fishing_game.bobber_image:
            pos (fishing_game.bobber_x, fishing_game.bobber_y)
            size (fishing_game.bobber_width, fishing_game.bobber_height)
        
        # Fish
        add fishing_game.fish_image:
            pos (fishing_game.fish_x, fishing_game.fish_y)
            size (fishing_game.fish_width, fishing_game.fish_height)
        
        # Progress bar container
        frame:
            pos (fishing_game.container_x, fishing_game.container_y)
            xsize fishing_game.container_width + 4
            ysize fishing_game.container_height + 4
            background "#c8c8c8"  # Light gray
            
            # Progress bar - fixed to use vertical bar correctly
            bar:
                value fishing_game.catch_time
                range fishing_game.catch_threshold
                xpos 2
                ypos 2
                xsize fishing_game.container_width
                ysize fishing_game.container_height
                bar_vertical True
        
        # Timer display
        frame:
            pos (fishing_game.WIDTH - 150, 10)
            background "#164C72"  # Blue color
            padding (10, 5)
            
            text "Time: [fishing_game.timer:.0f]":
                color "#FFFFFF"
                size 36
    else:
        # Game over screen
        if fishing_game.game_over_text == "IT'S A CATCH!":
            add fishing_game.catch_text_image
        else:
            add fishing_game.away_text_image
    
    # Retry button (always visible)
    frame:
        pos (10, 10)
        background "#164C72"  # Blue color
        padding (10, 5)
        
        textbutton "Retry":
            text_color "#FFFFFF"
            text_size 36
            action Function(fishing_game.reset_game)
    
    # Instructions text
    frame:
        pos (fishing_game.WIDTH // 2 - 150, fishing_game.HEIGHT - 100)
        background "#164C72"  # Blue color
        padding (10, 5)
        
        text "MOVE MOUSE TO CONTROL BOBBER":
            color "#FFFFFF"
            size 24
    
    # Return button (only visible when game is over)
    if fishing_game.game_over:
        frame:
            align (0.5, 0.9)
            background "#164C72"  # Blue color
            padding (20, 10)
            
            textbutton "Continue":
                text_color "#FFFFFF"
                text_size 36
                action Return()

# Label to start the fishing minigame
label fishing_minigame:
    $ caught_fish = run_fishing_minigame()
    
    if caught_fish:
        # Player caught the fish
        "You caught a fish!"
    else:
        # Player didn't catch the fish
        "The fish got away..."
    
    return 