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
python -m pip install struct 
python -m pip install socket
(python -m pip install requests) (not sure if this is needed)

When using the dashboard you have to install the streamlit library:
pip install streamlit-autorefresh
```

To run everything you will have to: 
1. Switch the switch on the PCB to position 1 (away from the motor)
2. Press the button on the underside of the drivetrain once 
    - blue lights will be visible (battery charge indicator)
3. Connect to the wifi of fizzy, Example: FiZZy_IC69200A4F64 (numbers are different with every PCB)
4. Password is: SpinnMeRoundAndRound
5. Connect the Xbox controller via bluetooth (only needed for 'fizzy_joystick..' and 'fizzy_state_machine' files)
6. Check if the firmware on the PCB is the latest version and is compatible with the python code
7. Run directly the main.py or run the dashboard
8. For the dashboard run in a seperate terminal -> Streamlit run ..\dashboard.py (depending on where you setup your virtual environment and location of the files)