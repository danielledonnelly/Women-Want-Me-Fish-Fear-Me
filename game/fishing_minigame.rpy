# Simple Fishing Minigame for Ren'Py

# Define the intro text images
image it_text_image = "fishing-minigame/it.png"
image her_text_image = "fishing-minigame/her.png"
image fumble_text_image = "fishing-minigame/fumble-text.png"

init python:
    import random
    
    class FishingGame:
        def __init__(self):
            self.reset()
        
        def reset(self):
            # Game dimensions
            self.WIDTH = 1440
            self.HEIGHT = 810
            
            # Simple bounds
            self.TOP_BOUND = 100
            self.BOTTOM_BOUND = self.HEIGHT - 50
            self.PLAY_HEIGHT = self.BOTTOM_BOUND - self.TOP_BOUND + 60
            
            # Center position
            self.CENTER_X = self.WIDTH // 2 + 100
            
            # Bobber starts at bottom
            self.bobber_x = self.CENTER_X
            self.bobber_y = self.BOTTOM_BOUND - 160
            
            # Super simple fish/heart properties
            self.fish_x = self.CENTER_X + 5
            self.fish_y = 300  # Start in middle
            self.fish_going_up = True
            
            # Basic game state
            self.timer = 10.0
            self.overlap_time = 0.0
            self.caught = False
            self.game_over = False
            self.game_started = False  # New flag for intro state
            
            # Type of game (fish or heart)
            self.game_type = "fish"
        
        def update(self, dt):
            if self.game_over or not self.game_started:  # Don't update if in intro or game over
                return
            
            # Update timer
            self.timer -= dt
            if self.timer <= 0:
                self.timer = 0
                self.game_over = True
                return
            
            # More random fish movement
            # 2% chance to change direction each frame
            if random.random() < 0.02:
                self.fish_going_up = not self.fish_going_up
            
            # Move fish
            if self.fish_going_up:
                self.fish_y -= 2
                # If at top, force downward
                if self.fish_y < self.TOP_BOUND + 100:
                    self.fish_going_up = False
            else:
                self.fish_y += 2
                # If at bottom, force upward
                if self.fish_y > self.BOTTOM_BOUND - 100:
                    self.fish_going_up = True
            
            # Better overlap detection - check if any part overlaps
            bobber_top = self.bobber_y
            bobber_bottom = self.bobber_y + 160  # Bobber height
            fish_top = self.fish_y
            fish_bottom = self.fish_y + 70  # Fish height
            
            # If there's any overlap between the ranges
            if bobber_bottom >= fish_top and bobber_top <= fish_bottom:
                self.overlap_time += dt * 0.5  # Increased rate for better feedback
                if self.overlap_time >= 2.0:
                    self.caught = True
                    self.game_over = True
            else:
                self.overlap_time = max(0, self.overlap_time - dt * 0.3)  # Faster decrease when not overlapping

        def start_game(self):
            self.game_started = True

# Create global instances for both game types
default fishing = FishingGame()
default heart_fishing = FishingGame()

# Main minigame screen - now accepts a game_type parameter
screen fishing_minigame(game_type="fish"):
    modal True
    
    default current_game = heart_fishing if game_type == "heart" else fishing
    $ current_game.game_type = game_type
    
    python:
        def move_bobber_up(game):
            game.bobber_y = max(game.TOP_BOUND, game.bobber_y - 47)
            
        def apply_gravity(game):
            game.bobber_y = min(game.BOTTOM_BOUND + 60 - 160, game.bobber_y + 3)
    
    # Update every frame
    timer 0.016 repeat True action Function(current_game.update, 0.016)
    
    # Background layer
    add "fishing-minigame/water.png"

    # Show intro text if game hasn't started
    showif not current_game.game_started:
        if game_type == "fish":
            add "it_text_image" align (0.5, 0.5) size (1200, 600)
        else:
            add "her_text_image" align (0.5, 0.5) size (1200, 600)
        
        key "K_SPACE" action [
            Function(current_game.start_game),
            NullAction()
        ]

    # Only show gameplay elements if game is not over and has started
    showif current_game.game_started and not current_game.game_over:
        # Bobber
        add "fishing-minigame/bobber.png":
            pos (current_game.bobber_x, current_game.bobber_y)
            size (80, 160)

        # Fish or Heart based on game type
        add "fishing-minigame/[game_type].png":
            pos (current_game.fish_x, current_game.fish_y)
            size (70, 70)

        # Vertical progress bar - moved right
        frame:
            style_prefix "fishing"
            pos (current_game.CENTER_X + 250, current_game.TOP_BOUND)
            background "#0a2438"
            padding (0, 0)
            xysize (40, current_game.PLAY_HEIGHT)
            
            bar value current_game.overlap_time range 2.0:
                style "fishing_progress"

        # UI Layer
        # Timer display
        frame:
            style_prefix "fishing"
            xalign 0.99
            ypos 20
            padding (20, 10)
            
            text "Time: [current_game.timer:.0f]" color "#fff"

        # Instructions
        frame:
            style_prefix "fishing"
            pos (20, 20)
            padding (20, 10)
            
            text "Click space to reel"
    
    # Game over overlays - centered
    showif current_game.game_over:
        if current_game.caught:
            add "fishing-minigame/catch-text.png" align (0.5, 0.5)
            
            textbutton "Continue" action Return(True):
                style "fishing_button"
                align (0.5, 0.9)
        else:
            if game_type == "fish":
                add "fishing-minigame/away-text.png" align (0.5, 0.5)
            else:
                add "fumble_text_image" align (0.5, 0.5)
            
            textbutton "Continue" action Return(False):
                style "fishing_button"
                align (0.5, 0.9)
    
    # Handle space key during gameplay
    if current_game.game_started and not current_game.game_over:
        key "K_SPACE" action [
            Function(move_bobber_up, current_game),
            NullAction()
        ]
    
    # Apply gravity only during gameplay
    if current_game.game_started and not current_game.game_over:
        timer 0.016 repeat True action Function(apply_gravity, current_game)

# Add this near the top of the file, after the imports
transform transparent:
    alpha 0.02  # 98% transparent

style fishing_frame:
    background "#164C72"  # Original solid color background
    padding (10, 5)

style fishing_text:
    color "#ffffff"
    size 24

style fishing_button:
    background "#164C72"  # Original solid color background
    padding (20, 10)
    xsize 200
    
style fishing_button_text:
    color "#ffffff"
    size 24
    xalign 0.5

style fishing_progress:
    left_bar "#164C72"
    right_bar "#0a2438"
    thumb None
    thumb_offset 0
    bar_vertical True
    xsize 40
    ysize 1.0

style fishing_rounded_frame:
    background Frame("gui/frame.png", 10, 10)  # Using the default Ren'Py rounded frame
    padding (20, 10)
    xsize None  # Allow width to adjust to content
    ysize None

# Label for regular fishing minigame
label fishing_minigame:
    window hide
    $ fishing.reset()
    $ renpy.transition(None)
    $ caught = renpy.call_screen("fishing_minigame", game_type="fish")
    window show
    return caught

# Label for heart minigame
label heart_minigame:
    window hide
    $ heart_fishing.reset()
    $ renpy.transition(None)
    $ caught = renpy.call_screen("fishing_minigame", game_type="heart")
    window show
    return caught