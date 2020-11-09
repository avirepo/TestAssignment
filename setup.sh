# Installing virtualenv python env manager
python3 -m pip install --user virtualenv
# Create virtual env for project with name test_assignment
virtualenv test_assignment
# Activate virtual env
source test_assignment/bin/activate
# Install requirements in env
pip3 install -r requirement.txt
# Run test cases
python manage.py test
# Run server
python manage.py runserver 8000
