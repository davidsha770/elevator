# Configuration file parser to load screen and building settings
import configparser

def load_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    
    # Read screen dimensions
    height_screen = config.getint('Settings', 'height_screen')
    width_screen = config.getint('Settings', 'width_screen')
    
    # Read building information
    buildings_info = []
    for key in config['Buildings']:
        floors, elevators = map(int, config['Buildings'][key].split(','))
        buildings_info.append([floors, elevators])
    
    return height_screen, width_screen, buildings_info
