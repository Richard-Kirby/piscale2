# piscale2

Connecting a Pi to a kitchen Scale - this allows tracking of your calorie intake based on weight and a database of calorie content for different foods.

Need to first install the C++ library that the HX711 library relies upon. Repo is here: https://github.com/endail/hx711

Clone this repo and change to the directory $cd piscale2

Set up a virtual Python environment. Using "python3 -m venv venv" - this puts a new Virtual environment directory, which you then need to activate by 'source venv/bin/activate'. You then need to install the rest of the requirements in the virtual environment.   

Once it is clear you are running in the venv - command line should be showing (venv) at the start, the you need to run this install dependencies via 'pip3 install -r requirements.txt'

For some reason the hx711 shared object file wasn't found. 'ImportError: libhx711.so: cannot open shared object file: No such file or directory'. Running 'sudo ldconfig' solved this problem. 

Set up an alias in the .bashrc file by adding 

alias piscale_venv='source /home/kirbypi/piscale2/venv/bin/activate'

piscale service enables running piscale as a service via systemd. It will need to be modified to use your own username and loaded as per other services. Install it as a user systemnd service by follwing the instructions here https://scruss.com/blog/2017/10/22/creating-a-systemd-user-service-on-your-raspberry-pi/ 

Piscale makes use of 'Onboard' onscreen keyboard as it is intended to be used on a touchscreen. This no longer works with the latest Raspberry Pi OS. Need to fix this. 

** 
