#!/usr/bin/env python3
"""
Simple API test script for Little Lemon API
Run this script to test basic API functionality
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_api():
    print("🧪 Testing Little Lemon API")
    print("=" * 40)
    
    # Test menu endpoint
    print("\n1. Testing Menu API (GET /restaurant/menu/)")
    try:
        response = requests.get(f"{BASE_URL}/restaurant/menu/")
        if response.status_code == 200:
            print("✅ Menu API is working")
            data = response.json()
            print(f"   Found {len(data)} menu items")
        else:
            print(f"❌ Menu API failed with status {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to the API. Make sure the server is running.")
        return
    
    # Test user registration
    print("\n2. Testing User Registration (POST /auth/users/)")
    test_user = {
        "username": "testuser123",
        "email": "test@example.com",
        "password": "testpassword123"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/auth/users/",
            json=test_user,
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 201:
            print("✅ User registration is working")
        elif response.status_code == 400:
            print("⚠️  User might already exist (this is normal)")
        else:
            print(f"❌ User registration failed with status {response.status_code}")
    except Exception as e:
        print(f"❌ User registration error: {e}")
    
    # Test token authentication
    print("\n3. Testing Token Authentication (POST /auth/token/login/)")
    login_data = {
        "username": "testuser123",
        "password": "testpassword123"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/auth/token/login/",
            json=login_data,
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            print("✅ Authentication is working")
            token = response.json().get("auth_token")
            
            # Test authenticated endpoint
            print("\n4. Testing Booking API (requires authentication)")
            headers = {
                "Authorization": f"Token {token}",
                "Content-Type": "application/json"
            }
            response = requests.get(
                f"{BASE_URL}/restaurant/booking/tables/",
                headers=headers
            )
            if response.status_code == 200:
                print("✅ Booking API is working")
                data = response.json()
                print(f"   Found {len(data)} bookings")
            else:
                print(f"❌ Booking API failed with status {response.status_code}")
        else:
            print(f"❌ Authentication failed with status {response.status_code}")
    except Exception as e:
        print(f"❌ Authentication error: {e}")
    
    print("\n" + "=" * 40)
    print("🏁 API testing completed!")
    print("💡 For more detailed testing, use the admin panel or Postman")

if __name__ == "__main__":
    test_api()