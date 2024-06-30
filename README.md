# PM-Django

!Django
!Python
!PostgreSQL

## Project Overview

**PM-Django** is a project management application built with Django. It allows users to manage projects, tasks, and teams efficiently.

## Features

- **User Authentication**: Secure login and registration.
- **Project Management**: Create, update, and delete projects.
- **Task Management**: Assign tasks to each project and track progress.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/omarmosharawi/PM-Django.git
    cd PM-Django
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    1. go to ```project_management/settings.py``` and open file.
   2. go down and find database settings and access your db information.
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## Usage

1. **Access the application**:
    Open your browser and go to `http://127.0.0.1:8000`.

2. **Log in**:
    Use the superuser credentials to log in.

3. **Start managing projects**:
    Create new projects, assign tasks, and collaborate with your team.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any inquiries or feedback, please contact:
- **omarmosharawi** - GitHub
- **omarmosharawi** - LinkedIn
- **omarmosharawi@gmail.com** - Email

---
