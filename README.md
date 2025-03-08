# Taxi Game

## Overview
Taxi Game is a simple arcade game built with Pygame. The player controls a taxi, picks up a passenger, and delivers them to a parking area. Upon successful delivery, the player wins.

## Requirements
- Python 3.x
- Pygame

## Installation
1. Install Python (if not already installed):
   ```sh
   sudo apt install python3
   ```
   
2. Install Pygame:
   ```sh
   pip install pygame
   ```

3. Clone or download the repository and navigate to the project folder.

## How to Play
- **Arrow keys:** Move the taxi in the corresponding direction.
- **Pick up the passenger:** Drive to the passenger's location.
- **Drop off the passenger:** Navigate to the parking area to complete the mission.
- **Win Condition:** Successfully park the taxi with the passenger.

## Game Logic
1. The taxi starts at a default position.
2. A passenger spawns at a random hotel location.
3. The player moves the taxi to pick up the passenger.
4. A parking area is assigned.
5. The player must drive to the parking area without crashing.
6. Upon reaching the parking area, the game displays a winning message and resets positions for a new round.

## Controls
- **Up Arrow:** Move up
- **Down Arrow:** Move down
- **Left Arrow:** Move left
- **Right Arrow:** Move right

## Running
Run the following command in the terminal:
```sh
python main.py
```

## License
This project is open-source and free to use.

