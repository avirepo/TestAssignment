
## Installation steps

#### Its a Django application system should pre install the python to run this application

##### There is a setup shell script is available in the project directory, I have make it according to mac, in case it is not working please follow the steps below. 
###### Run following command to run setup
    sh setup.sh
     
###### Install virtual env
    python3 -m pip install --user virtualenv

###### Install virtual env
    virtualenv assignment
###### Activate virtual env
    source assignment/bin/activate

###### Install project dependencies
    pip3 install -r requirement.txt

###### Running unittest cases
    python manage.py test

###### Running the application
    python manage.py runserver
    
## Run Application    

##### Api supports 2 API
###### 1. Get price API(Will return today's bitcoin price)
    
    http://localhost:8000/price/ 
    
###### 2. Get price History(Will return bitcoin price for provided start and end date use)
    
    http://localhost:8000/history/?start_date=2020-11-05 (Return history of btc price from 5th Nov till today) 
    
    http://localhost:8000/history/?end_date=2020-11-05 (Return history of btc price till 5th Nov till with past 9 days) 
    
    http://localhost:8000/history/?start_date=2020-11-01&end_date=2020-11-05 (Return history of btc price between 1st-5th Nov) 
    
    http://localhost:8000/history/ (Return history of btc price between with last 10 days) 
