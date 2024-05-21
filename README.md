# Bob_Raoul_v2

Bob_Raoul_v2 is a fun and interactive project designed to add a bit of entertainment to parties or gatherings. This project features Bob, a plastic mannequin equipped with a sensor to detect when a beer cap is tossed into a hole in its head. The project runs on a Raspberry Pi with a screen, providing visual and audio feedback whenever a cap is successfully thrown in.

## Project Overview

### Concept

The inspiration for this project comes from a tradition at UTBM (Université de Technologie de Belfort-Montbéliard) where a "Raoul" is used to collect beer caps. The goal is to make it somewhat challenging to toss the caps into the Raoul from a distance. Bob_Raoul_v2 takes this concept further by using a mannequin named Bob and incorporating technology to enhance the experience.

### Features

- **Cap Detection**: An infrared sensor placed inside Bob's head detects when a beer cap is thrown into the hole.
- **Audio Feedback**: A random sound is played from the "sounds" directory each time a cap is detected.
- **Visual Feedback**: A sequence of JPEG images from a randomly chosen directory in the "video_backgrounds" folder is displayed on the screen, creating an animation effect that loops until the next cap is detected.
- **Cap Counter**: The total number of caps successfully thrown into Bob is displayed in the corner of the screen and incremented with each new cap. The count is stored in a file named `caps.txt`.

## Hardware Requirements

- Raspberry Pi (any model with GPIO pins and a screen output)
- Infrared sensor
- Plastic mannequin (Bob)
- Screen (connected to the Raspberry Pi)
- Beer caps

## Software Requirements

- Python 3
- `pygame` library
- `RPi.GPIO` library

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/Bob_Raoul_v2.git
   cd Bob_Raoul_v2
   ```
2. **Install Dependencies**
	```sh
   pip install -r requirements.txt
   ```
3. **Setup the Hardware**
* Place the infrared sensor inside Bob's head.
* Connect the sensor to the Raspberry Pi GPIO pins.
* Connect the screen to the Raspberry Pi.

4. **Run the Program**
	```sh
   python main.py
   ```

## Usage

- Toss a beer cap into the hole in Bob's head.
- The sensor detects the cap and triggers the program.
- A random sound from the "sounds" directory plays.
- A sequence of JPEG images from a randomly chosen directory in the "video_backgrounds" folder displays on the screen, creating an animation effect.
- The cap counter increments and displays the total number of caps thrown in. The count is stored in the caps.txt file.

## Directory Structure

```Bob_Raoul_v2/
├── video_backgrounds/
│ └── [directories containing frames of animations in JPEG format]
├── sounds/
│ └── [various sound files]
├── Bob-v2.py
├── requirements.txt
├── caps.txt
└── README.md```


## Contribution

Feel free to fork this repository and contribute by submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.


## Acknowledgements

- UTBM for the inspiration of the Raoul concept.
- The Hatry-poté for the incredible colocation experience and support during the development of this project.
- Fice, Tumleu, Hackerman, DuQ, érosse, Kyrie, Nital, Marie, Lag, and all the other testers/players (apologies if anyone was missed) for their valuable feedback and contributions.
