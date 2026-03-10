# Installation


Download python (Works at least with:python 3.12, but newwer versions should also work)
Download vscode (it's what I used for code editing)


make a seperate folder to make virtual environment for fizzy stuff
follow a tutorial on making a virtual environment or following the following steps in vscode:
1. ctl+shift+p
2. type: python: create environment
3. choose venv
4. choose python version
5. done!!!

Now we need to download the packages to run the python files

python -m pip install pyjoystick
python -m pip install matplotlib
python -m pip install keyboard 
(python -m pip install requests) (not sure if this is needed)



To run everything you will have to: 
1. connect the powersupply of the ball (insert the cable of the battery holder into the pcb)
2. connect to the wifi of fizzy, FiZZy-PWM-0X (X can be a number between 1-4, defining different PCB's)
3. password is: SpinnMeRoundAndRound
4. connect the Xbox controller via bluetooth (only needed for 'fizzy_joystick..' and 'fizzy_state_machine' files)
5. check if the firmware is the latest version and is compatible with the python code
6. run programm









1. Open the Anaconda Prompt.
2. Clone this repository and cd inside it.
3. Create a new Conda environment:

```
conda env create --prefix ./envs --file environment.yml
```

4. Activate the environment:

```
conda activate ./envs
```

Document the rest of the installation!!