import os
import traceback
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend101.settings')
django.setup()

from django.db import connection


def initiate_database():
    try:
        with connection.cursor() as cursor:
            cursor.execute('set foreign_key_checks=0')
            cursor.execute('truncate social_signup_types')
            cursor.execute('truncate account_types')
            cursor.execute('truncate users')
            
    except Exception as e:
        print(str(e))
        traceback.print_exc()

initiate_database()
