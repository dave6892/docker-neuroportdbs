# docker-neuroportdbs

This is a Docker container for [NeuroportDBS](https://github.com/SachsLab/NeuroportDBS). NeuroportDBS is a collection of software [SachsLab](https://github.com/SachsLab) use for deep brain stimulation (DBS) surgery intraoperative mapping with microelectrode recording (MER) using the Blackrock Neuroport. 
This repository is currently a private repository.

A simplistic demo for starting up the docker-neuroport container.

    $ git clone https://github.com/dave6892/docker-neuroportdbs.git
    $ cd docker-neuroportdbs
    $ docker-compose pull app
    $ docker-compose up -d db
    $ IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}') xhost +
    $ docker-compose run --rm -e DISPLAY=$IP:0 app

For the first time running this application, make sure to run

    $ serf-makemigrations; serf-migrate
