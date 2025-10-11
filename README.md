# Little Lemon API 🍋

A Django REST API for the Little Lemon restaurant, providing endpoints for menu management, table bookings, and user authentication.

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

### 2. Install Dependencies with Pipenv
```bash
pipenv install
pipenv shell
```

### 3. MySQL Database Configuration

You need to manually set up a local MySQL database with the exact credentials specified in `settings.py`:

#### Install MySQL Server
Make sure MySQL Server is installed and running on your system.

#### Create Database and User
Connect to MySQL as root and run the following commands:
```sql
CREATE DATABASE littleLemon;
CREATE USER 'littleAdmin'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON littleLemon.* TO 'littleAdmin'@'localhost';
FLUSH PRIVILEGES;
```

**Important**: These credentials must match exactly what's in `littleLemon/settings.py`:
- **Database Name**: `littleLemon`
- **Username**: `littleAdmin`
- **Password**: `password`
- **Host**: `127.0.0.1` (localhost)
- **Port**: `3306`

### 4. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser
You can either create a superuser manually or use the automated command:

**Option A: Manual Creation**
```bash
python manage.py createsuperuser
```

**Option B: Use Default Credentials**
```bash
python manage.py create_default_superuser
```
This creates an admin user with:
- Username: `admin`
- Email: `admin@littlelemon.com`
- Password: `adminpass123`

### 6. Load Sample Menu Data (Optional)
```bash
python manage.py loaddata fixtures/sample_menu.json
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

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
├── setup.sh                   # automated setup script
├── test_api.py                # API testing script
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

### Run Tests
```bash
python manage.py test
```

### Test API Endpoints
Use the provided test credentials or create your own user account to test authenticated endpoints.

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