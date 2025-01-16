from ..utils.config_loader import ConfigLoader

class StyleConfig:
    def __init__(self):
        config_loader = ConfigLoader()
        ui_config = config_loader.load_ui_config()
        
        self.colors = ui_config['colors']
        self.fonts = ui_config['fonts']
        self.dimensions = ui_config['dimensions']

    def configure_window(self, root):
        root.configure(bg=self.colors['background'])
        
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width/2 - self.dimensions['window_width']/2)
        center_y = int(screen_height/2 - self.dimensions['window_height']/2)
        
        root.geometry(f'{self.dimensions["window_width"]}x{self.dimensions["window_height"]}+{center_x}+{center_y}')

    def get_button_style(self):
        return {
            'font': self.fonts['button'],
            'bg': self.colors['primary'],
            'fg': self.colors['white'],
            'relief': 'flat',
            'padx': 20,
            'pady': 5
        }

    def get_input_style(self):
        return {
            'font': self.fonts['input'],
            'bg': self.colors['white'],
            'relief': 'flat'
        }

    def get_header_style(self):
        return {
            'font': self.fonts['header'],
            'bg': self.colors['primary'],
            'fg': self.colors['white'],
            'pady': 15
        }
