# Installation


Download python (Works at least with:python 3.12, but newwer versions should also work)
Download vscode (it's what I used for code editing)
In vscode download python extension


Make a seperate folder to make the virtual environment for fizzy programming stuff
follow a tutorial on making a virtual environment or following the following steps in vscode:
1. ctl+shift+p
2. type: python: create environment
3. choose venv
4. choose python version
5. done!!!

Now we need to download the packages to run the python files
```
python -m pip install pyjoystick
python -m pip install matplotlib
python -m pip install keyboard 
(python -m pip install requests) (not sure if this is needed)
```



To run everything you will have to: 
1. Switch the switch on the PCB to position 1 (away from the motor)
2. Press the button on the underside of the drivetrain once 
    - blue lights will be visible (battery charge indicator)
3. Connect to the wifi of fizzy, FiZZy-PWM-0X (X can be a number between 1-4, defining different PCB's) (OLD)
4. Password is: SpinnMeRoundAndRound
5. Connect the Xbox controller via bluetooth (only needed for 'fizzy_joystick..' and 'fizzy_state_machine' files)
6. check if the firmware is the latest version and is compatible with the python code
7. run programm