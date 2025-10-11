#!/bin/bash

echo "🍋 Little Lemon API Setup Script"
echo "================================"

# Navigate to project directory
cd "$(dirname "$0")"

# Check if Python 3.12+ is available
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "📍 Using Python version: $python_version"

# Check if pipenv is installed
if ! command -v pipenv &> /dev/null; then
    echo "❌ pipenv is not installed. Please install it first:"
    echo "   pip install pipenv"
    exit 1
fi

# Install dependencies with pipenv
echo "📦 Installing dependencies with pipenv..."
pipenv install

# Database check
echo ""
echo "🗄️  Database Setup Required:"
echo "   Make sure MySQL is running and execute these commands:"
echo "   CREATE DATABASE littleLemon;"
echo "   CREATE USER 'littleAdmin'@'localhost' IDENTIFIED BY 'password';"
echo "   GRANT ALL PRIVILEGES ON littleLemon.* TO 'littleAdmin'@'localhost';"
echo "   FLUSH PRIVILEGES;"
echo ""

read -p "Press Enter after setting up the MySQL database..."

# Activate pipenv shell and run setup commands
echo "🔄 Running database migrations..."
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate

# Create superuser
echo "👤 Creating default superuser..."
pipenv run python manage.py create_default_superuser

# Load sample data
echo "� Loading sample menu data..."
pipenv run python manage.py loaddata fixtures/sample_menu.json

echo ""
echo "✅ Setup completed successfully!"
echo ""
echo "🚀 To start the development server:"
echo "   pipenv shell"
echo "   python manage.py runserver"
echo ""
echo "   Or directly:"
echo "   pipenv run python manage.py runserver"
echo ""
echo "🌐 Then visit:"
echo "   • API: http://127.0.0.1:8000/"
echo "   • Admin: http://127.0.0.1:8000/admin/"
echo ""
echo "🔑 Default admin credentials:"
echo "   Username: admin"
echo "   Password: adminpass123"
echo ""