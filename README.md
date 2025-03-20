# Fitness Tracker Dashboard

#### Video Demo: [https://youtu.be/hiH-IOP7oF4](https://youtu.be/hiH-IOP7oF4)

#### Description:

The Fitness Tracker Dashboard is a comprehensive web application designed to help users track their workouts and water intake. This project is built using Flask, SQLAlchemy, and Chart.js, providing a user-friendly interface for logging activities and visualizing progress.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [File Structure](#file-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Design Choices](#design-choices)
- [Future Enhancements](#future-enhancements)

## Project Overview

The Fitness Tracker Dashboard allows users to:

- Register and log in to their accounts.
- Log workouts by specifying the type and duration.
- Log daily water intake.
- Visualize logged data through dynamic charts.
- View historical data for both workouts and water intake.

The application is intended to provide users with insights into their fitness habits and encourage consistent tracking for better health management.

## Features

- **User Authentication**: Secure registration and login functionality using Flask-Login and password hashing.
- **Workout Logging**: Users can log different types of workouts with their duration.
- **Water Intake Logging**: Users can record their daily water consumption.
- **Dynamic Visualization**: Interactive charts display workout types and water intake over time, with different colors representing different workout types.
- **Responsive Design**: The interface is designed to be accessible on various devices, including desktops, tablets, and smartphones.

## Technologies Used

- **Flask**: A micro web framework for Python used to build the backend of the application.
- **SQLAlchemy**: An ORM (Object Relational Mapper) used for database interactions.
- **SQLite**: A lightweight database used for storing user data, workouts, and water intake records.
- **Chart.js**: A JavaScript library used for creating interactive charts.
- **HTML/CSS**: For structuring and styling the web pages.
- **JavaScript**: For dynamic content updates and interactions on the client side.

## File Structure

```
    fitness-tracker/
    │
    ├── templates/
    │ ├── index.html # Homepage template
    │ ├── login.html # Login page template
    │ ├── register.html # Registration page template
    │ ├── dashboard.html # User dashboard template
    │
    ├── static/
    │ ├── style.css # Custom CSS for styling
    │
    ├── app.py # Main Flask application
    ├── fitness.db # SQLite database
    ├── README.md # Project documentation
    │
```

## Setup and Installation

1. **Clone the Repository**:

   ```bash
   git clone <repository_url>
   cd fitness-tracker
    ```

2. **Create a Virtual Environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**:

    ```bash
    flask run
    ```

5. **Access the Application**:

    Open your web browser and go to http://127.0.0.1:5000.

### 1. Homepage
![Homepage](static/images/home.png)
*Description*: The homepage provides an overview of the application and options to log in or register.

### 2. Register
![Register](static/images/register.png)
*Description*: New users can create an account by providing a username and password.

### 3. Login
![Login](static/images/login.png)
*Description*: Existing users can log in with their credentials to access their dashboard.

### 4. Dashboard
![Dashboard](static/images/dashboard.png)
*Description*: The user dashboard displays logged workouts and water intake. Users can also add new entries here.

1. **Log Workouts**: Enter the type and duration of your workouts.
2. **Log Water Intake**: Record your daily water intake.
3. **View Progress**: Check your logged data visualized through charts.

## Design Choices

### Database Design

- **User Table**: Contains user credentials and links to their logged activities.
- **Workout Table**: Stores details of workouts including type, duration, and date.
- **Water Intake Table**: Records daily water consumption with timestamps.

### Chart Design

- **Separate Charts**: Separate charts for workouts and water intake ensure clarity.
- **Color Coding**: Different colors represent different workout types for easy differentiation.

### Frontend and Backend Integration

- **AJAX for Logging**: Uses AJAX requests for logging workouts and water intake without page reloads.
- **Dynamic Data Fetching**: Fetches historical data on page load to display past logs.

## Future Enhancements

- **Enhanced Analytics**: Provide more detailed analytics and trends over time.
- **Social Features**: Allow users to connect with friends and share their progress.
- **Mobile App**: Develop a mobile app for easier access and logging on the go.
- **Reminders and Notifications**: Implement reminders for logging workouts and water intake.
