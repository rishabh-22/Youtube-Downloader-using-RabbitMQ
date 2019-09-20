# Youtube-Downloader-using-RabbitMQ
This repository includes a script to install youtube videos with the help of workers deployed by RabbitMQ.

The script is run by main.py file.
Provide the urls of the videos that you want to download as the system arguments.
Deploy as many workers as required and feasible using the worker.py file.
The main file then sends the urls to download the videos to the workers in roundrobin manner.
