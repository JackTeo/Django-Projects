-----------------------------------------------------------------------------------------------------------
Installing Python and setup folder
-----------------------------------------------------------------------------------------------------------
// To check python version
 > py --version

// To check pip version
 > pip --version

// To install virtual environment
 > pip install virtualenv
 > virtualenv env

// Unable recognise path?
 > My computer
 > Properties
 > Advanced system properties
 > Environment Variables
 > System variables
 > add "C:\Users\xx\AppData\Local\Programs\Python\Python39\Scripts\;" to Path
 > restart PC

// To upgrade pip version
 > cd to Appdata\Local\Programs\Python\Python39
 > python -m pip install --upgrade pip

// To activate virtual environment
 > env\Scripts\activate

// Unable to activate? (get-executionpolicy) = Restricted)
 > run powershell in administrator
 > set-executionpolicy remotesigned
 > Y
 > get-executionpolicy should be remotesinged

-----------------------------------------------------------------------------------------------------------
Installing Django
-----------------------------------------------------------------------------------------------------------
// Get latest official version
 > pip install Django==3.2.4

// Check Django version
 > python -m django --version

// To check Django requirements
 > pip freeze > requirements.txt 
asgiref==3.3.4
Django==3.2.4
pytz==2021.1
sqlparse==0.4.1

-----------------------------------------------------------------------------------------------------------
Start Project
-----------------------------------------------------------------------------------------------------------
> pip install virtualenv
> virtualenv env
> env\Scripts\activate
> pip install Django==3.2.4
> pip freeze > requirements.txt
> django-admin startproject djcrm .

// Run server
> python manage.py runserver
> python manage.py migrate
