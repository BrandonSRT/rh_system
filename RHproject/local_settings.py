import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'TCU_test',
       'USER': 'postgres',
       'PASSWORD':'Patricia04',
       'HOST':'localhost',
       'DATABASE_PORT':'5432',
   }
}