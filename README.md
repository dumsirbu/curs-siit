Comenzi pentru pornire proiect

```bash
python3 -m venv venv
source venv/bin/activate ( For Windows open a Powershell as administrator and run Set-ExecutionPolicy Unrestricted -Force )
cd curs-siit/siit
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Varianta Docker
```
docker build -t curs .
docker run -it curs bash
docker run -it -p 8000:8000 curs python manage.py runserver 0.0.0.0:8000
``

sau

```
docker compose up
```
