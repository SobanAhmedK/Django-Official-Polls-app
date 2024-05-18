# Polls Web Application

Welcome to the Polls web application! This project allows users to create, view, and vote on polls. It's built using Django, a high-level Python web framework, and leverages Django templating engine with Bootstrap for the frontend.

## Features

- **Poll Creation:** Users can create new polls with multiple-choice questions.
- **Poll Viewing:** Users can view existing polls along with their choices and vote on them.
- **Poll Results:** Results of the polls are displayed after users have voted.
- **Contact Form:** Provides a contact form for users to send messages, including their name, email, contact number, age, and message.

## Technologies Used

- **Django:** A powerful Python web framework used for building web applications.
- **Bootstrap:** A popular CSS framework for building responsive and visually appealing web interfaces.
- **Templating Engine:** Django's templating engine is used to generate HTML content dynamically.
- **Python:** The backend logic and business logic are implemented in Python.

## Project Structure

polls/<br>
├── migrations/<br>
├── templates/<br>
│ └── polls/<br>
├── static/<br>
├── models.py<br>
├── views.py<br>
├── urls.py<br>
└── tests.py<br>


## Running the Application

1. Install Python and Django if you haven't already.
2. Clone this repository to your local machine.
3. Navigate to the project directory in your terminal.
4. Run `python manage.py migrate` to apply migrations and set up the database.
5. Run `python manage.py runserver` to start the development server.
6. Open your web browser and go to `http://localhost:8000/` to access the application.

## Testing

To run the unit tests:

```bash
python manage.py test

Feel free to adjust any details or formatting to suit your preferences! Let me know if you need further modifications.
