# Microblogging Platform

A simple microblogging platform where users can register, create posts, and comment on others' posts.

## Features
- User registration and login.
- Create posts with a character limit (e.g., 280 characters).
- Comment on posts.
- Admin interface for managing users, posts, and comments.

## Features
- User registration and login.
- Create posts with a character limit (e.g., 280 characters).
- Comment on posts.
- Admin interface for managing users, posts, and comments.

  ## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Sandini2002/microblogging-platform.git
   cd microblogging-platform
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   .\venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```
## Usage

- Register a new account or log in using the `/register` and `/login` endpoints.
- Create posts and comment on others' posts from the homepage.

