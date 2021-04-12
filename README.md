# docker-neuroportdbs

A simplistic demo for starting up the docker-serf container.

    $ git clone https://github.com/dave6892/docker-neuroportdbs.git
    $ cd docker-neuroportdbs
    $ docker-compose pull app
    $ docker-compose up -d db
    $ IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}') xhost +
    $ docker-compose run --rm -e DISPLAY=$IP:0 app

For the first time running this application, make sure to run

    $ serf-makemigrations; serf-migrate