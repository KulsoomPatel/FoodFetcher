class Settings:
    def __init__(self):
        # screen height and width are variables to store details
        self.screen_width, self.screen_height = 800, 600
        # RGB color
        self.bg_color = 179, 204, 255

        self.initialize_game_parameters()

    def initialize_game_parameters(self):
        # game play parameters
        self.food_speed = 0.1

        # CHANGE THIS VALUE
        self.speed_increase_factor = 1.05
        # Number of balloons to release in a spawning:
        self.batch_size = 1
        # CHANGE THIS VALUE
        # Number of balloons that need to be popped before increasing batch_size
        #  For actual play, probably want ~10; for testing, ~3
        self.catch_needed = 3
