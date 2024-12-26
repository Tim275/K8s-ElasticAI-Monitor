

Copy:
- app.py
- Dockerfile
- requirements.txt


```sh
sudo apt install python3-pip
sudo su

pip3 install Flask

mkdir -p app
cd app 


python3 app.py


curl -X POST http://20.115.71.115:5000/alert -H "Content-Type: application/json" -d '{"status": "test", "message": "This is a test alert"}'


{"status": "success", "message": "Alert received"}

#INFO:root:Received alert: {'status': 'test', 'message': 'This is a test alert'}

ERROR:app:Discord webhook error: {"content": ["Must be 2000 or fewer in length."]}

```


```sh



python3 app.py


docker build -t jonathanbaraldi/flask-log-generator:latest .


docker run -d -p 5000:5000 jonathanbaraldi/flask-log-generator:latest

docker logs -f 


docker login

jonathanbaraldi

docker push jonathanbaraldi/flask-log-generator:latest

kubectl apply -f deployment.yaml


```