# jango-tutorial

## Step 1: Create a proj
- `django-admin startproject [project name here]`
- `python -m django startproject [project name]`
  
## Step 2: create app
- `django-admin startapp [app name here]`
- `python manage.py startapp [app name here]`
  
## Step 3: run web server
-> cd into the project folder where manage.py is located

-> run `python manage.py runserver`

## Step 4: build database
-> cd into folder with manage.py

-> `python manage.py migrate`

## Step 5: create super user
-> cd into folder w manage.py

-> `python manage.py createsuperuser`
## Step 6: add app to setting Installed apps Dictionary
-> `INSTALLED APPS = [`

->`...

->`'app_name',`

## Step 7: add template folder
-> `'DIRS': [BASE_DIR /  'templates']`,

-> Add template folder inside app folder

## View Fuction
```python
def base(request):
    context ={

    }

    return render(request, 'base.html', context)
```
