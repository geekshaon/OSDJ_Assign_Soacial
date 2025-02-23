# RexSocial - Social Media Platform

## User Credentials for Testing

### Superuser Account:
- **Username:** admin
- **Password:** admin

### Regular User Accounts:
1. **Username:** rex2
   - **Password:** 123
2. **Username:** rex2
   - **Password:** 123

## Setup and Installation Instructions

### Prerequisites
- Python 3.8+
- Django 4+
- SQLite (default) or PostgreSQL (if preferred)

### Installation Steps

1. **Clone the repository:**
   ```bash
   https://github.com/geekshaon/OSDJ_Assign_Soacial.git
   cd rexsocial
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set up an admin account.

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   - Open a web browser and visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Admin Panel: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## Summary of Implemented Features

- **User Authentication:** Sign up, login, logout.
- **User Profiles:** Update bio, upload profile pictures, set location and date of birth.
- **Post Creation:** Users can create posts with text and images.
- **Post Management:** Users can edit and delete their posts.
- **Post Feed:** View all posts in a modern card-style format.
- **My Posts:** View all posts created by the logged-in user.
- **Bootstrap-based UI:** Responsive and clean design.

## Entity Relationship Diagram (ERD)

![ERD](https://github.com/geekshaon/OSDJ_Assign_Soacial/blob/main/erd.png)




## Additional Notes
- Make sure you have media file handling set up properly in Django settings.
- If using PostgreSQL, update the `DATABASES` setting in `settings.py` accordingly.
- For testing, use the provided credentials or create new users through the sign-up page.

