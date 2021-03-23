# The Health App

The Health App allows users to create an account and keep track of their weight. The app will calculater their BMI indicator based on profile information. 

# Technical Details

This is an app where users can keep track of thier weight. 

Users can create an account/profile and upload a profile picture, update their name, email address, and change their password. 

Users can enter their weight. All weights entered by any given user are listed in the home page. Users can choose to only see the weights entered by themselves. 

# Author
[Chuck Li Villalobos](https://github.com/ticochuck)


## GETTING STARTED:

On you terminal:
- `poetry shell` to start your virtual environment
- `poetry install` to install dependencies
- create .env file with listed <a href="#env">below</a> variables and save it into 'penny_pincher' directory
- `python manage.py makemigrations` - to generate DB schema
- `python manage.py migrate` - to create DB schema
- `python manage.py createsuperuser` - to create user with admin access
- `python manage.py collectstatic` - to collect apps static files
- `python manage.py runserver` - to run server

\* You will need to have an web email server for the reset password functionallity. Email account and password will need to be entered in the .env file

### <a name="env"></a> ENV variables:

SECRET_KEY=secret key for the app (typically 50-characters long string)  
DEBUG=should be set to True in development  
ALLOWED_HOSTS=localhost,127.0.0.1 (for testing)

## API:

`/` - landing page;  
`user/register/` - register page, handles users registration;  
`login/` - login page, allows users to log in;  
`profile/` - profile page, allows users to view and edit their profile information and upload a profile picture(login required);  
`password-reset/` - allow users to request a new password  
`password-reset/done/` - email confirmation page with link to change password;   
`password-reset-confirm/<uidb64>/<token>/`- confirmation that password has been changed. Routes back to login page;  
`password-reset-complete/` - password change process completed successfully;  
`user/logout/` - logout page, is shown when users are logged out (login required);    
`user/<str:username>`  
`post/<int:pk>/` - displays selected post;  
`post/new/` - allows a user to create a new post (login required);  
`post/<int:pk>/update/` - allows a user to update existing post (login required, authorization required);  
`post/<int:pk>/delete/` - allows a user to delete existing post (login required, authorization required);  
`about/` - about us page;  
`admin/` - site admin page;


