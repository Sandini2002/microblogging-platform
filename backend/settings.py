# Django settings for microblogging platform project.

# ...other settings...

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Use MySQL as the database
        'NAME': 'microblogging_platform',     # Replace with your database name
        'USER': 'root',                       # Replace with your database user
        'PASSWORD': 'password',               # Replace with your database password
        'HOST': 'localhost',                  # Replace with your database host
        'PORT': '3306',                       # Default MySQL port
    }
}

# ...other settings...