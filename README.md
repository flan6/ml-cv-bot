# ML-CV-BOT
> This project aims to apply computer vision in games to automate repetitive tasks. My main goal is to study the fields of computer vision and machine learning while gaming. It uses YoloV4 and OpenCV to identify "crops" in the game "Albion Online¨.


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- Provide general information about your project here.
	We are using a custom trained detection model to detect 'crops' on AlbionOnline, this can later be used to automate the farming labor of the game.
	We locate the game window based on its name (Linux only), then capture screenshots and send them to the dectetion model to detect and classify the objetcs (crops), after that we are planning to automate the task of collecting grown crops.
- What problem does it (intend to) solve?
	This project aims to apply computer vision in games to automate repetitive tasks.
- What is the purpose of your project?
	The purpose of this project is to apply computer vision and machine learning to automate certain games' tasks. Like colecting resources, crafting or even combat. 



## Technologies Used
- OpenCV
- YoloV4
- PyAutoGUI
- Fastgrab API
- Xdo API
- Numpy

## Features
List the ready features here:
- Object Detection in Real Time

## Screenshots
<!-- ![Example screenshot](./img/screenshot.png) -->
<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
<!-- What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located? -->

<!-- Proceed to describe how to install / setup one's local environment / get started with the project. -->


## Usage
<!-- How does one go about using it? -->
<!-- Provide various use cases and code examples here. -->

<!-- `write-your-code-here` -->


## Project Status
Project is: _in progress_ / _very early development stage_


## Room for Improvement
<!-- Include areas you believe need improvement / could be improved. Also add TODOs for future development. -->

Room for improvement:
- Threads are out of sync, we could sync them and fix it schelude.
- It's taking screenshots way faster than the detection model can handle.

To do:
- Fix threads timing
- Add the automation to colect grown crops
- Add the automation to plant new chosen crops
- Add herbs to the system.


## Acknowledgements
Give credit here.
- This project was inspired by the youtube channel Learn Code By Gaming.
- This project was based on [this tutorial](https://www.youtube.com/watch?v=KecMlLUuiE4&list=PL1m2M8LQlzfKtkKq2lK5xko4X-8EZzFPI).
- Many thanks to Ben from channel Learn Code By Gaming, for inspiring me to start this new project and learn a new language and this incredible field of computer vision and machine learning.


## Contact
Created by [@flan6](https://github.com/flan6) - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
