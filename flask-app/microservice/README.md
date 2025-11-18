<!-- assignments -->
to run backend
create venv
python3 -m venv env

source env/bin/activate
pip3 install -r requirement.txt

@devOps-learning/flask-app/microservice/backend$ 
python3 app.py

to run frontend
@devOps-learning/flask-app/microservice/frontend$
python3 -m http.server 3000


to submit data
http://localhost:3000/index.html


to view db data by api
http://127.0.0.1:5000/view-data