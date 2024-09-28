# railway_reservation_django_jwt
This is a RESTful API for a Railway Reservation System built using Django REST Framework with JWT role-based authentication and authorization.

Features
User Authentication:

Users can register, log in, and log out.
JWT (JSON Web Tokens) are used for authentication.
Role-Based Permissions:

Regular Users: Can create, and view their own tickets.
Admins: Can view ,update and delete tickets created by any user.
Ticket Management:

Users: Can create, and view their own tickets.
Admins:  Can view ,update and delete any ticket.
Requirements
Python 3.x
Django 3.x+
Django REST Framework
Simple JWT (djangorestframework-simplejwt)


Here's a README.md file that includes the key aspects of your project, with explanations for setting up JWT authentication, creating views for registration, and handling permissions. This will guide others (or yourself) when revisiting the project.

Railway Reservation System API
This is a RESTful API for a Railway Reservation System built using Django REST Framework with JWT role-based authentication and authorization.

Features
User Authentication:

Users can register, log in, and log out.
JWT (JSON Web Tokens) are used for authentication.
Role-Based Permissions:

Regular Users: Can create, delete, and view their own tickets.
Admins: Can view and update tickets created by any user.
Ticket Management:

Users: Can create, view, and delete tickets.
Admins: Can view and update any ticket.
#Requirements
Python 3.x
Django 3.x+
Django REST Framework
Simple JWT (djangorestframework-simplejwt)

#Setup Instructions
Clone the repository:
git clone https://github.com/yourusername/railway_reservation_django_jwt.git
cd railway_reservation_django_jwt
Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Run migrations:
python manage.py migrate
Run the server:
python manage.py runserver

API Endpoints:
JWT-Token end points:
To get token (post method)-> api/token/
To get refresh token -> api/token/refresh/

Register-> api/register/
Login->api/login/
Logout -> api/logout/

Create Ticket (User):
Endpoint: POST /api/tickets/
Header: Authorization: Bearer <JWT token>

View Ticket(User):
Endpoint: GET /api/tickets/
Header: Authorization: Bearer <JWT token>

View All Tickets (Admin):
Endpoint: GET api/getallticket/
Header: Authorization: Bearer <JWT token>

Update Ticket (Admin):
Endpoint: PUT api/updateticket/<int:pk>/
Header: Authorization: Bearer <JWT token>

Delete Ticket (Admin):
Endpoint: DELETE api/deleteticket/<int:pk>/
Header: Authorization: Bearer <JWT token>

Authentication and Permissions
JWT Authentication
This project uses JWT (JSON Web Token) for authentication.
When a user logs in, they receive an access token (short-lived) and a refresh token (long-lived).
You need to include the access token in the Authorization header with every request that requires authentication.

Handling Authentication Credentials Issue
If you encounter "Authentication credentials were not provided", make sure you:

Include the JWT token in the Authorization header in this format:


Authorization: Bearer <your_access_token>
Confirm that JWT authentication is properly set up in settings.py:

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
Use the login endpoint to retrieve the token, and use it in subsequent requests.

Handling Registration Permissions Issue
If the UserRegistrationView is asking for authentication, ensure that:

The view uses the AllowAny permission to allow unauthenticated users to register:

permission_classes = [AllowAny]
