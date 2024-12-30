# 🌟 Game Tank 🌟

## 🌐 Description

**Game Tank** is an exciting arcade-style game where players control a tank and navigate through a maze filled with obstacles and enemies. The goal is to survive as long as possible, collecting ammunition and eliminating zombies that come towards the tank.

## 💡 Features

- **Tank Control**: Players can control the tank using the keyboard to navigate through the maze.
- **Ammunition**: Players can collect ammunition from the map and shoot zombies to eliminate them.
- **Zombies**: Enemies are continuously generated and move towards the tank. Zombies are capable of avoiding obstacles to reach the player.
- **Lives System**: The tank has a limited number of lives represented by hearts. If a zombie touches the tank, the player loses lives. The game ends when all lives are lost.
- **Score Saving**: At the end of each game, players can choose to save their score and enter their name. Scores are saved in a file and can be viewed from the menu.
- **Level Menu**: The game includes a level selection menu where players can choose from multiple available maps.
- **Scoreboard Menu**: Players can view the leaderboard from a dedicated menu.

## 🟢 Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/sergiu1301/TankGame.git
    ```

2. **Install dependencies**:
    Make sure you have Python and pygame installed. If not, you can install pygame using pip:
    ```sh
    pip install pygame
    ```

3. **Run the game**:
    ```sh
    python main.py
    ```

## ⚡ Controls

- **Tank Movement**: 
    - `W`: Move forward
    - `S`: Move backward
    - `A`: Rotate left
    - `D`: Rotate right
- **Shooting**:
    - `SPACE`: Shoot

## 🛡️ Project Structure

- **main.py**: Entry point of the game.
- **game.py**: Contains the main game logic.
- **menu.py**: Manages the level selection menu and scoreboard menu.
- **level.py**: Manages levels and map generation.
- **tank.py**: Defines the behavior of the tank.
- **zombie.py**: Defines the behavior of the zombies.
- **ammunition.py**: Manages the ammunition objects.
- **settings.py**: Contains game settings and maps.
- **heart.py**: Defines the behavior of the hearts.
- **tile.py**: Defines the behavior of the tiles.
- **explosion.py**: Defines the behavior of the explosions.
- **bullet.py**: Defines the behavior of the bullets.
- **debug.py**: Contains debug setup.
- **floor.py**: Defines the behavior of the floor.
  
## Screenshots

### Main Menu
![Main Menu](https://github.com/user-attachments/assets/14ca6de1-17ef-49d9-8453-abb88c426fd9)



### Scoreboard
![Main Menu](https://github.com/user-attachments/assets/703c1f0a-b124-447b-89bd-ae8bb1e00690)


### Gameplay
![Gameplay 1](https://github.com/user-attachments/assets/437a01f5-760c-4388-88de-3139f0152ce6)
![Gameplay 2](https://github.com/user-attachments/assets/d0764115-0946-47f7-b247-1d4a681aff0d)
![Gameplay 3](https://github.com/user-attachments/assets/d3843481-42c7-463d-84d9-4d5a663eef10)


### Game Over
![Scoreboard](Images/GameOver.png)
