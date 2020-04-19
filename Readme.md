## It's my Django project

Do you want to run my project ?
Do this instruction below in your terminal.

#### 1-st step
Clone with HTTPS from GitHub
```
git clone https://github.com/AsylbekAbdyrakmanov/DjangoTask2.git
```
#### 2-nd step
Go to the bent directory. Install and activate the virtual environment

```
python3 -m venv env
```
then
```
source env/bin/activate
```

#### 3-rd step

Install all packages in  requirement.txt

```
pip install -r requirements.txt
```

#### 4-th step
Make migrations 
```
./manage.py makemigrations
```
then
```
./manage/py migrate
```
#### 5-th step
Create a super user
```
./manage.py createsuperuser
```
### Finally step
Run the project

```
./manage.py runserver
```


