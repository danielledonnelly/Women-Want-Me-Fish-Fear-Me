# Simple Fishing Minigame for Ren'Py

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
            self.PLAY_HEIGHT = self.BOTTOM_BOUND - self.TOP_BOUND + 60  # Add this back for progress bar
            
            # Center position
            self.CENTER_X = self.WIDTH // 2 + 100
            
            # Bobber starts at bottom
            self.bobber_x = self.CENTER_X
            self.bobber_y = self.BOTTOM_BOUND - 160
            
            # Super simple fish properties
            self.fish_x = self.CENTER_X + 5
            self.fish_y = 300  # Start in middle
            self.fish_going_up = True
            
            # Basic game state
            self.timer = 15.0
            self.overlap_time = 0.0
            self.caught = False
            self.game_over = False
        
        def update(self, dt):
            if self.game_over:
                return
            
            # Update timer
            self.timer -= dt
            if self.timer <= 0:
                self.timer = 0
                self.game_over = True
                return
            
            # SUPER SIMPLE fish movement - just up and down
            if self.fish_going_up:
                self.fish_y -= 2
                if self.fish_y < self.TOP_BOUND + 100:
                    self.fish_going_up = False
            else:
                self.fish_y += 2
                if self.fish_y > self.BOTTOM_BOUND - 100:
                    self.fish_going_up = True
            
            # Simple overlap check
            if abs(self.bobber_y + 80 - self.fish_y) < 50:
                self.overlap_time += dt * 0.3
                if self.overlap_time >= 2.0:
                    self.caught = True
                    self.game_over = True
            else:
                self.overlap_time = max(0, self.overlap_time - dt * 0.2)

# Create global instance
default fishing = FishingGame()

# Main minigame screen
screen fishing_minigame():
    modal True
    
    # Update every frame
    timer 0.016 repeat True action Function(fishing.update, 0.016)
    
    # Background layer
    add "fishing-minigame/water.png"

    # Bobber
    add "fishing-minigame/bobber.png":
        pos (fishing.bobber_x, fishing.bobber_y)
        size (80, 160)

    # THE FISH - JUST A SIMPLE IMAGE ON SCREEN
    add "fishing-minigame/fish.png":
        pos (fishing.fish_x, fishing.fish_y)
        size (70, 70)

    # Vertical progress bar - moved right
    frame:
        style_prefix "fishing"
        pos (fishing.CENTER_X + 250, fishing.TOP_BOUND)
        background "#0a2438"
        padding (0, 0)
        xysize (40, fishing.PLAY_HEIGHT)
        
        bar value fishing.overlap_time range 2.0:
            style "fishing_progress"

    # UI Layer
    # Timer display
    frame:
        style_prefix "fishing"
        xalign 1.0
        ypos 20
        padding (20, 10)
        
        text "Time: [fishing.timer:.0f]" color "#fff"

    # Instructions
    frame:
        style_prefix "fishing"
        pos (20, 20)
        
        text "HOLD SPACE TO REEL UP"
    
    # Replay button (always visible)
    frame:
        style_prefix "fishing"
        pos (20, 80)
        
        textbutton "Replay" action Function(fishing.reset):
            style "fishing_button"
            text_size 20
    
    # Game over overlays - centered
    if fishing.game_over:
        if fishing.caught:
            add "fishing-minigame/catch-text.png" align (0.5, 0.5)
            
            textbutton "Continue" action Return(True):
                style "fishing_button"
                align (0.5, 0.9)
        else:
            add "fishing-minigame/away-text.png" align (0.5, 0.5)
            
            textbutton "Continue" action Return(False):
                style "fishing_button"
                align (0.5, 0.9)
    
    # Handle space key - move bobber up when space is pressed, constrained to progress bar bounds
    key "K_SPACE" action [
        Function(lambda: setattr(fishing, 'bobber_y', max(fishing.TOP_BOUND, fishing.bobber_y - 45))),
        NullAction()
    ]
    
    # Apply gravity but stop at bottom of progress bar
    timer 0.016 repeat True action Function(lambda: setattr(fishing, 'bobber_y', min(fishing.BOTTOM_BOUND + 60 - 160, fishing.bobber_y + 2)))

style fishing_frame:
    background "#164C72"
    padding (10, 5)

style fishing_text:
    color "#ffffff"
    size 24

style fishing_button:
    background "#164C72"
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

# Label that runs the minigame
label fishing_minigame:
    window hide
    $ fishing.reset()
    $ renpy.transition(None)
    $ caught = renpy.call_screen("fishing_minigame")
    window show
    return caught