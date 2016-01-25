# Example Bottle Application from Docker

This is a simple bottle application which uses the devries/bottle base image.
The application serves a single page which uses the bottle template engine to
provide a simple hello world message with the container's IP address. 

## Building the Docker Container

You can build this container using the command

~~~~~
docker build -t devries/hellobottle .
~~~~~

or you can pull the image from the [docker hub](http://hub.docker.com/) using
the command

~~~~~
docker pull devries/hellobottle
~~~~~

## Running the Docker Container

To run the container use the command:

~~~~~
docker run -d -p 8080:8080 devries/hellobottle
~~~~~

The Dockerfile runs the [gunicorn](http://gunicorn.org) WSGI server.
