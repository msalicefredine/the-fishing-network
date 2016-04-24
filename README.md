# the-fishing-network
Collaborating on web client for collecting and standardizing fishing information on a global scale.


### The Fishing Network
The web version of the Fishing Network allows users visualize fishery data that has been inputted by a variety of users. Currently, the Fishing Network supports uploading csv files of fishing data to the database and even has a csv formatter to help users correctly input the data. There is also a <a rel="license" href="https://github.com/Danagregg/the-fishing-network-mobile">mobile app</a> to allow users to input data.

### Next Steps
Coming soon, the Fishing Network will have SDKs for easy API access. The user interface will also be upgraded to support more complex queries for the data and have more detailed data plots. The Fishing Network hopes to add accounts for users to save their own information.

### Dev Environment Setup
Always dreamed of adding on to the fishing network? Here's how.

####  Requirements
Requires Python 2.7.*
Server requires Mac or Linux

#### Instructions

1. ```git clone https://github.com/msalicefredine/the-fishing-network.git```
2. In the repository ```virtualenv venv```
⋅⋅* If you get an error, you may need to install virtualenv with  ```pip install virtualenv```
3. Active your virtual environment
⋅⋅1. Mac: ```source  venv/bin/activate```
4. pip install -r requirements.txt
5. If you do not have MongoDB installed locally: ```brew install mongodb```
6. In your venv directory
⋅⋅1. ```mkdir -p data/db```
⋅⋅2. mongod --dbpath data/db
7. ```Heroku local web```
⋅⋅* If Heroku is not recognized, you may need to install the heroku toolbelt

Disco @ http://localhost:5000

### License

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.


