# Little Lemon API 🍋

A Django REST API for the Little Lemon restaurant, providing endpoints for menu management, table bookings, and user authentication.

## ⚡ Quick Start (Recommended)

**Want to get up and running fast? Use our automation scripts!**

1. **Setup MySQL database** (see detailed instructions below)
2. **Run the setup script:**
   ```bash
   cd littleLemon
   pipenv install
   ./setup.sh
   ```
3. **Test your API:**
   ```bash
   python manage.py runserver  # Start server
   python test_api.py          # Test in another terminal
   ```

**That's it! Your API is ready.** 🍋✨

### 🔧 Troubleshooting

**If admin login doesn't work:**
1. Try the manual superuser creation:
   ```bash
   pipenv shell
   python manage.py createsuperuser
   ```
2. Or run the standalone script:
   ```bash
   pipenv run python create_superuser.py
   ```

**Default credentials:**
- Username: `admin`
- Password: `adminpass123`
- Email: `admin@littlelemon.com`

---

## 🚀 Features

- **Menu Management**: Create, read, update, and delete menu items
- **Table Booking System**: Manage restaurant reservations (authenticated users only)
- **User Authentication**: Registration, login/logout with token-based authentication
- **Admin Panel**: Django admin interface for easy management
- **RESTful API**: Clean and intuitive API endpoints

## 📋 Prerequisites

- Python 3.12+
- MySQL Server
- pipenv (for dependency management)

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/aderraj/LittleLemonAPI.git
cd LittleLemonAPI/littleLemon
```

### 2. MySQL Database Configuration

You need to set up a local MySQL database with the exact credentials specified in `settings.py`:

**Create Database and User:**
```sql
-- Connect to MySQL as root
mysql -u root -p

-- Run these commands:
CREATE DATABASE littleLemon;
CREATE USER 'littleAdmin'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON littleLemon.* TO 'littleAdmin'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

**Required credentials** (must match `settings.py`):
- **Database**: `littleLemon`
- **User**: `littleAdmin` 
- **Password**: `password`
- **Host**: `127.0.0.1`
- **Port**: `3306`

### 3. Automated Setup

**Use the setup script for everything else:**

```bash
pipenv install
./setup.sh
```

The setup script automatically handles:
- ✅ Dependencies installation
- ✅ Database migrations
- ✅ Superuser creation (admin/adminpass123)
- ✅ Sample data loading
- ✅ Environment verification

**If the automatic superuser creation fails, you can create one manually:**
```bash
pipenv shell
python manage.py createsuperuser
# Use: admin / admin@littlelemon.com / adminpass123
```

### 🧪 Test Your API

After setup, verify everything works with the included test script:

```bash
# Make sure your server is running first
python manage.py runserver

# In another terminal, run the API tests
python test_api.py
```

The test script will automatically:
- ✅ Test all API endpoints
- ✅ Create a test user account
- ✅ Test authentication
- ✅ Verify booking functionality
- ✅ Show you what's working

## 📚 API Documentation

### Base URL
```
http://127.0.0.1:8000
```

### Authentication
The API uses token-based authentication. Include the token in your headers:
```
Authorization: Token <your-token-here>
```

### Endpoints

#### 🍽️ Menu Management
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/restaurant/menu/` | List all menu items | No |
| POST | `/restaurant/menu/` | Create a new menu item | No |
| GET | `/restaurant/menu/{id}/` | Retrieve a specific menu item | No |
| PUT | `/restaurant/menu/{id}/` | Update a menu item | No |
| DELETE | `/restaurant/menu/{id}/` | Delete a menu item | No |

#### 📅 Booking Management
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/restaurant/booking/tables/` | List all bookings | Yes |
| POST | `/restaurant/booking/tables/` | Create a new booking | Yes |
| GET | `/restaurant/booking/tables/{id}/` | Retrieve a specific booking | Yes |
| PUT | `/restaurant/booking/tables/{id}/` | Update a booking | Yes |
| DELETE | `/restaurant/booking/tables/{id}/` | Delete a booking | Yes |

#### 🔐 Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/users/` | User registration |
| POST | `/auth/token/login/` | User login |
| POST | `/auth/token/logout/` | User logout |
| POST | `/restaurant/api-token-auth/` | Obtain auth token |

## 💡 Usage Examples

### Register a New User
```bash
curl -X POST http://127.0.0.1:8000/auth/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newuser",
    "email": "user@example.com",
    "password": "securepassword123"
  }'
```

### Login and Get Token
```bash
curl -X POST http://127.0.0.1:8000/auth/token/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newuser",
    "password": "securepassword123"
  }'
```

### Create a Menu Item
```bash
curl -X POST http://127.0.0.1:8000/restaurant/menu/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Grilled Salmon",
    "description": "Fresh Atlantic salmon grilled to perfection",
    "price": "24.99",
    "inventory": 15
  }'
```

### Create a Booking (Authenticated)
```bash
curl -X POST http://127.0.0.1:8000/restaurant/booking/tables/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -d '{
    "name": "John Doe",
    "number_of_guests": 4,
    "booking_date": "2025-10-15T19:30:00Z"
  }'
```

## 🏗️ Project Structure

```
littleLemon/
├── manage.py
├── Pipfile                     # pipenv dependencies
├── requirements.txt            # pip dependencies (generated from Pipfile)
├── setup.sh                   # 🚀 AUTOMATED SETUP SCRIPT - Run this!
├── test_api.py                # 🧪 API TESTING SCRIPT - Test your API!
├── db.sqlite3                 # SQLite database (backup)
├── fixtures/
│   └── sample_menu.json       # sample menu data
├── littleLemon/
│   ├── __init__.py
│   ├── settings.py            # Django settings (contains MySQL config)
│   ├── urls.py
│   └── wsgi.py
├── restaurant/
│   ├── models.py              # Menu and Booking models
│   ├── views.py               # API views
│   ├── serializers.py         # DRF serializers
│   ├── urls.py               # restaurant app URLs
│   ├── migrations/
│   └── management/
│       └── commands/
│           └── create_default_superuser.py
└── templates/
    └── index.html
```

## 🔧 Configuration

### Database Settings
The application is configured to use MySQL with these exact settings (as specified in `littleLemon/settings.py`):
- **Database**: `littleLemon`
- **User**: `littleAdmin`
- **Password**: `password`
- **Host**: `127.0.0.1`
- **Port**: `3306`

**Important**: You must create a MySQL database and user with these exact credentials for the application to work properly.

### MySQL Setup Commands
```sql
CREATE DATABASE littleLemon;
CREATE USER 'littleAdmin'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON littleLemon.* TO 'littleAdmin'@'localhost';
FLUSH PRIVILEGES;
```

## 🧪 Testing

### Automated API Testing
Use the included test script to verify all endpoints:

```bash
# Start the development server
python manage.py runserver

# In another terminal, run the automated tests
python test_api.py
```

**What the test script does:**
- ✅ Tests menu API (GET /restaurant/menu/)
- ✅ Tests user registration (POST /auth/users/)
- ✅ Tests authentication (POST /auth/token/login/)
- ✅ Tests booking API with authentication
- ✅ Provides detailed success/error feedback

### Manual Testing
```bash
# Run Django unit tests
python manage.py test

# Test with curl commands (see examples below)
curl http://127.0.0.1:8000/restaurant/menu/
```

### Test Credentials
Use these for manual testing:
- **Superuser**: admin / adminpass123
- **Test User**: Created automatically by test_api.py

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG = False` in settings.py
- [ ] Configure production MySQL database with proper credentials
- [ ] Update `SECRET_KEY` for production
- [ ] Configure static file serving (use `python manage.py collectstatic`)
- [ ] Set up HTTPS
- [ ] Update `ALLOWED_HOSTS` in settings.py
- [ ] Use environment variables for sensitive data

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support and questions, please open an issue in the GitHub repository or contact the development team.

---

**Happy Coding! 🍋✨**