-----------------------------------------------------------------------------------------------------------
PC setup
-----------------------------------------------------------------------------------------------------------
// To check python version
 > py --version

// To check pip version
 > pip --version

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

// Unable to activate? (get-executionpolicy = Restricted)
 > run powershell in administrator
 > set-executionpolicy remotesigned
 > Y
 > get-executionpolicy should be remotesinged

-----------------------------------------------------------------------------------------------------------
Django
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
> pip install virtualenv                    // To install virtual environment
> virtualenv env                            // Set environment name
> env\Scripts\activate                      // To activate virtual environment
> pip install Django==3.2.4
> pip freeze > requirements.txt
> django-admin startproject djcrm .         // Creates project named djcrm

// Run server
> python manage.py runserver
> python manage.py migrate
> python manage.py startapp leads           // Creates app named leads

// To register 'leads' app
> Navigate to djcrm folder
> settings.py
> INSTALLED_APPS
> ADD 'leads'
> Setup database models in model.py
> python manage.py makemigrations           // Creates model
> python manage.py migrations               // Apply to SQlite