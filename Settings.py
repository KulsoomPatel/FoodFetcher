class Settings:
    def __init__(self):
        # screen height and width are variables to store details
        self.screen_width, self.screen_height = 800, 600
        # RGB color
        self.bg_color = 179, 204, 255

        self.button_width, self.button_height = 250, 50
        self.button_bg = (0, 163, 0)
        self.button_text_color = (235, 235, 235)
        self.button_font, self.button_font_size = 'Arial', 24

        # game status
        self.game_active = False
        # game over conditions
        self.min_catch_ratio = 0.9
        self.games_played = 0

        self.initialize_game_parameters()

    def initialize_game_parameters(self):
        # game play parameters
        self.food_speed = 0.1
        self.poison_ratio = 0.10

        # CHANGE THIS VALUE
        self.speed_increase_factor = 1.05
        # Number of balloons to release in a spawning:
        self.batch_size = 1
        # CHANGE THIS VALUE
        # Number of balloons that need to be popped before increasing batch_size
        #  For actual play, probably want ~10; for testing, ~3
        self.batches_needed = 3
