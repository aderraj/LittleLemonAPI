#!/usr/bin/env python
"""
Create default superuser for Little Lemon API
"""
import os
import sys
import django

# Add the project directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_dir)

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'littleLemon.settings')

# Setup Django
django.setup()

from django.contrib.auth.models import User

def create_superuser():
    username = 'admin'
    email = 'admin@littlelemon.com'
    password = 'adminpass123'
    
    if User.objects.filter(username=username).exists():
        print(f'⚠️  Superuser "{username}" already exists!')
        return
    
    try:
        User.objects.create_superuser(username, email, password)
        print('✅ Superuser created successfully!')
        print(f'   Username: {username}')
        print(f'   Email: {email}')
        print(f'   Password: {password}')
        print('   Access admin at: http://127.0.0.1:8000/admin/')
    except Exception as e:
        print(f'❌ Error creating superuser: {e}')
        sys.exit(1)

if __name__ == '__main__':
    create_superuser()