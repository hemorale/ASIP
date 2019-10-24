# ASIP
Academic Stress Identification Platform Files

User’s guide – Academic Stress Identification Platform v0.0.1
Hector Morales

1.	Firefox is the default browser. Highly recommended to use it instead of chrome or any other.
2.	Download python 3 latest stable version (currently is 3.8.0) for the desired platform. Currently we have tested Mac OSX High Sierra 10.13.6 with python 3.7.2 and Windows 10 Pro version 10.0.17134/10.0.18362
3.	Python 3 for windows does not have virtualenv as part of the package, compared to Mac OSX version:
 
4.	It is highly recommended to install virtualenv
 
5.	Create virtualenv
    Virtualenv C:\Users\[USER]\[VIRTUALENV_DIR]
6.	Activate virtualenv. 
    C:\Users\[USER]\[VIRTUALENV_DIR]\Scripts\activate.bat 	#or activate.ps1
If using Powershell, the activate script is subject to the execution policies on the system
7.	Make sure you have Microsoft C++ Build Tools if you are using a windows 10 machine. Download from https://visualstudio.microsoft.com/es/downloads/ if necessary
8.	Install python packages using the requirements.txt file
9.	Pip install requests
10.	Pip install numpy
11.	Pip install scipy in case this install fails try using https://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy download scipy-1.3.1-cp38-cp38-win32.whl (or amd64 depending your hardware architecture on your windows machine) try pip install from local file
12.	Pip install matplotlib from https://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib

