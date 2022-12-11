# PJS_EnOp

## How to: streaming-data-platform start-up
To start the streaming-data-platform make shure that docker is running with the kafka container.

### set-up Kafka
You can find the docker-compose.yml in the folder streaming-data-platform/kafka.

### Starting the python scripts
For easier handling use the platform_startup.sh in the streaming-data-platform folder.
To start it use the command:

sh platform_startup.sh

### Using the frontend
To see if everything is running fine you can use the frontend by opening localhost with a browser.

export FLASK_APP=consumer_frontend
flask run
