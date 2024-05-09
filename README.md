# elevators

A brief description of what this project does and who it's for.

## Configuration Loading

`load_config` function: Reads `configuration.txt` using `configparser`. Extracts screen dimensions and buildings data (number of floors and elevators per building).

## Pygame Initialization and Main Loop

### `main` function
Initializes the pygame environment, sets up the game window, and enters the main game loop. The loop processes user inputs, updates the screen at 60 frames per second, and manages events like quitting or mouse interactions.

## Game Components

### Street class
Manages a collection of buildings. Uses the factory pattern to create buildings based on configuration data. Handles event propagation to buildings and drawing updates.

### Building class
Represents individual buildings. Manages floors and elevators, processes user clicks on floors to simulate elevator calls, and handles the drawing and updating of its components.

### Floor class
Graphical and interactive representation of a floor in a building. Responds to mouse clicks for elevator calls and renders the floor’s state visually.

### Elevator class
Controls elevator movement, queue management for floor requests, and updates its position and state based on the simulation time and queued requests.

## Factory Pattern

`factory` function: Simplifies object creation for buildings, floors, and elevators. This approach abstracts object creation and makes the system more modular.

## Utility and Drawing Functions

The script uses straightforward pygame drawing functions to render the game state, including buildings, elevators, and floors. Elevators move according to queued requests, and floors display a timer indicating the waiting time for an elevator.

## Conclusion

This setup demonstrates an application of object-oriented programming principles in Python, using Pygame for real-time simulation and interaction. The architecture promotes separation of concerns through distinct classes for managing different aspects of the simulation, such as user interaction, game state management, and rendering.

## How to Run

python3 main.py 

