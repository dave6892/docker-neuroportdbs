# docker-neuroportdbs

This is a Docker container for [NeuroportDBS](https://github.com/SachsLab/NeuroportDBS). NeuroportDBS is a collection of software [SachsLab](https://github.com/SachsLab) use for deep brain stimulation (DBS) surgery intraoperative mapping with microelectrode recording (MER) using the Blackrock Neuroport. 
This repository is currently a private repository.

## How to Run

In order to run PyQt GUI in Docker, X11 is required. 

#### (Optional) To run in MacOS
1. Install [XQuartz](https://www.xquartz.org). Restart OS.
2. In XQuartz: Check the option: XQuartz -> Preferences -> Security -> "Allow connections from network clients"

#### 1. Download the Repository

    $ git clone https://github.com/dave6892/docker-neuroportdbs.git
    $ cd docker-neuroportdbs
    
#### 2. Move the Data to the Repository   
Move the data (\*.ns5 and associated files) into the direcory `./data`.

#### 3. Pull the Docker Image and Compose
    $ docker-compose pull app
    $ docker-compose up -d db
    
#### 4. Configure the Environment and Run in Docker
    $ IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}') xhost +
    $ docker-compose run --rm -e DISPLAY=$IP:0 app


### Inside the Docker CLI
#### For the first time running this application, make sure to run
    $ serf-makemigrations; serf-migrate

#### Import Data into the Database
    $ python import_ns5.py
    
#### Run GUI
    $ python features_gui.py
