Comenzi pentru pornire proiect

```bash
python3 -m venv venv
source venv/bin/activate ( For Windows open a Powershell as administrator and run Set-ExecutionPolicy Unrestricted -Force )
cd curs-siit/siit
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
