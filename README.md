# docker-neuroportdbs

## How to Run

To run in MacOS, see the next section.

A simplistic demo for starting up the docker-serf container.

    $ git clone https://github.com/dave6892/docker-neuroportdbs.git
    $ cd docker-neuroportdbs
    $ docker-compose pull app
    $ docker-compose up -d db
    $ IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}') xhost +
    $ docker-compose run --rm -e DISPLAY=$IP:0 app

For the first time running this application, make sure to run

    $ serf-makemigrations; serf-migrate

## To run in MacOS
1. Install [XQuartz](https://www.xquartz.org). Restart OS.
2. In XQuartz: Check the option: XQuartz -> Preferences -> Security -> "Allow connections from network clients"
3. Run the code above.

