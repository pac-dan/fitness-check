# Fitness Diary

Fitness Diary is a full-stack web application designed to help users record their fitness goals, log workouts, and track nutritional intake. Built with Django, HTML, CSS, and Bootstrap, this application showcases comprehensive CRUD (Create, Read, Update, Delete) operations within a user-friendly interface. 

# Table of Contents
- Project Overview
- Features
- Technology Stack
- Agile Methodology
    - User Stories
    - Epics
- Installation
- Usage
- Testing
    - Manual Testing
- Deployment
- Data Schema
- Security
- Contributing
- Contact
- Screenshots
- UX Design Documentation
- Performance Optimization
- Additional Documentation

## Project Overview 
Fitness Diary aims to provide users with a centralized platform to record and achieve their fitness objectives. Whether it's increasing daily steps, logging workouts, or managing nutritional intake, Fitness Diary is a way to digitally record your fitness journey so you can see improvement and encourage yourself to continue.

### Features 
- User Registration & Authentication:
    - Secure user sign-up and login functionalities using django-allauth.
    - Profile management.

- Goals Setting:
    - Create, view, update, and delete fitness goals.
    - Track progress towards each goal.

- Workouts Logging:
    - Log details of workouts, including type, duration, and calories burned.
    - View and manage workout history.

- Nutrition Logging:
    - Track daily nutritional intake, including calories and macronutrients.
    - Manage meal logs and dietary plans. 

- Responsive Design:
    - Mobile-friendly interface using Bootstrap.
    - Accessible design adhering to UX principles.

- Real-Time Feedback:
    - Immediate reflections of CRUD operations in the user interface.

####  Technology Stack
- Backend:
    - Python 
    - Django
    - django-allauth (Authentication)
- Front-end:
    - HTML5
    - CSS3
    - Bootstrap 5
    - Javascript(ES6)
- Database:
    - SQlite
- Others:
    - WhiteNoise (Static Files Management)
    - CORS Headers
    - Crispy Forms
    - Debug Toolbar

##### Agile Methodology 
Fitness Diary was developed using the Agile methodology, ensuring iterative progress and adaptability throughout the project lifecycle.

**User Stories**

- Epic 1: User Management
    - As a user, I want to register and log in so that I can securely access my fitness data.
    - As a user, I want to update my profile information to keep my account details current.

- Epic 2: Goals Management
    - As a user, I want to create fitness goals so that I have targets to achieve.
    - As a user, I want to view my goals to track my progress.
    - As a user, I want to update or delete my goals as my objectives change.

- Epic 3: Workouts Logging
    - As a user, I want to log my workouts to monitor my exercise routines.
    - As a user, I want to view my workout history to analyze my performance over time.
    - As a user, I want to update or delete my workouts as my objectives change.

- Epic 4: Nutrition Logging
    - As a user, I want to log my meals to track my nutritional intake.
    - As a user, I want to view my nutrition history to manage my diet effectively.
    - As a user, I want to update or delete my nutrition logs as my objectives change.

###### Epics to User Stories Mapping

Each epic was broken down into specific user stories to streamline development and ensure all functionalities were covered comprehensively.

**Installation**
- Prerequisites 
    - Python 3.8+
    - pip 
    - Git

**Steps**
- Clone the Repository:
    - git clone https://github.com/yourusername/Fitness_Diary.git
      cd Fitness_Diary

- Create Virtual Environment:
    - python -m venv env
      env\Scripts\activate
    
- Install Dependencies:
    - pip install -r requirements.txt

- Apply Migrations:
    - python manage.py migrate

- Create a Superuser:
    - python manage.py createsuperuser

- Run the Development Server:
    - python manage.py runserver

- Access the Application:
    - Open http://localhost:8000 in your browser.

**Usage**
- User Registration & Authentication
    - Sign Up: Navigate to the registration page to create a new account.
    - Log In: Access your account using your credentials.
    - Profile Management: Update your profile information as needed.
- Goals Management
    - Create Goal: Set new fitness goals with specific targets.
    - View Goals: Monitor your current and past goals.
    - Update/Delete Goal: Modify or remove goals as your objectives evolve.
- Workouts Logging
    - Log Workout: Record details of your workouts, including type, duration, and calories burned.
    - View Workouts: Review your workout history to track progress.
- Nutrition Logging
    - Log Meal: Enter details about your meals, including calories and macronutrients.
    - View Nutrition History: Analyze your dietary intake over time.

**Testing**

Ensuring the reliability and robustness of Fitness Diary through comprehensive testing.

- Manual Testing
    - User Flow Testing: Verified all user flows, including registration, goal setting, workout logging, and nutrition tracking.
    - Responsive Design Testing: Ensured the application is responsive across various devices and screen sizes.
    - Accessibility Testing: Checked compliance with accessibility standards using tools like WAVE and Lighthouse.

**Deployment**

Fitness Diary is deployed on Heroku, ensuring accessibility from anywhere.

- Deployment Steps

- Set Environment Variables:
    - SECRET_KEY: Your Django secret key.
    - DEBUG: Set to False in production.
    - DATABASE_URL: Provided by Heroku.
    - ALLOWED_HOSTS: Your Heroku app domain.
    - 'heroku config:set SECRET_KEY='your-secret-key' DEBUG=False ALLOWED_HOSTS='fitness-diary.herokuapp.com' --app fitness-tracker-app'

- Collect Static files
    - python manage.py collectstatic

- Push to Heroku:
    - git push heroku main 
 
- Run Migrations
    - heroku run python manage.py migrate --app fitness-tracker-app

- Create a Superuser on Heroku:
    - heroku run python manage.py createsuperuser --app fitness-tracker-app

- Access the Application:
    - Visit https://fitness-tracker-project-b28eeb139905.herokuapp.com/ in your browser.

**Deployment Checklist**
-  Environment variables set securely.
-  DEBUG mode disabled.
-  Secret keys and sensitive information not committed to the repository.
-  Static files managed using WhiteNoise.
-  Procfile configured correctly.
-  Application tested post-deployment.

**Data Schema**

### **Goals Model**

| **Field**      | **Type**               | **Description**                                 |
|----------------|------------------------|-------------------------------------------------|
| `user`         | `ForeignKey`           | Links to the CustomUser model.                  |
| `title`        | `CharField`            | Title of the fitness goal.                      |
| `description`  | `TextField`            | Detailed description (optional).                |
| `target`       | `PositiveIntegerField` | Target value (e.g., steps, calories).           |
| `created_at`   | `DateTimeField`        | Timestamp when the goal was created.            |
| `updated_at`   | `DateTimeField`        | Timestamp when the goal was last updated.       |

### **Workouts Model**

| **Field**      | **Type**               | **Description**                                 |
|----------------|------------------------|-------------------------------------------------|
| `user`         | `ForeignKey`           | Links to the CustomUser model.                  |
| `workout_type` | `CharField`            | Type of workout (e.g., Running, Cycling).       |
| `duration`     | `PositiveIntegerField` | Duration of the workout in minutes.             |
| `calories_burned` | `PositiveIntegerField` | Estimated calories burned during the workout.|
| `date`         | `DateField`            | Date of the workout.                            |
| `created_at`   | `DateTimeField`        | Timestamp when the workout was logged.          |
| `updated_at`   | `DateTimeField`        | Timestamp when the workout was last updated.    |

### **Nutrition Logs Model**

| **Field**        | **Type**               | **Description**                                   |
|------------------|------------------------|---------------------------------------------------|
| `user`           | `ForeignKey`           | Links to the CustomUser model.                    |
| `meal_type`      | `CharField`            | Type of meal (e.g., Breakfast, Lunch).            |
| `calories`       | `PositiveIntegerField` | Total calories consumed in the meal.              |
| `carbohydrates`  | `PositiveIntegerField` | Carbohydrate intake in grams.                     |
| `proteins`       | `PositiveIntegerField` | Protein intake in grams.                          |
| `fats`           | `PositiveIntegerField` | Fat intake in grams.                              |
| `date`           | `DateField`            | Date of the meal.                                 |
| `created_at`     | `DateTimeField`        | Timestamp when the meal was logged.               |
| `updated_at`     | `DateTimeField`        | Timestamp when the meal was last updated.         |


**Security**
- Environment Variables: All sensitive information, including SECRET_KEY and database credentials, are stored in environment variables and not committed to the repository.
- Authentication: Utilizes django-allauth for robust user authentication and management.
- Authorization: Role-based access control ensures that users can only access and manipulate their own data.
- Secure Settings:
    - SECURE_SSL_REDIRECT is enabled to enforce HTTPS.
    - SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE are set to True to ensure cookies are only sent over HTTPS.
- Input Validation: All forms include validation to prevent malicious inputs.
- Error Handling: Graceful error handling ensures that users are informed of issues without exposing sensitive information.

**Contact**
For any inquiries or feedback, please contact djjohnston98@hotmail.com

**Screenshots**
- Home Page 

- Goals Pages

- Workout Pages

- Nutrition Pages 

- User Pages 

**Performance Optimization**
- Database Indexing: Indexed frequently queried fields to speed up data retrieval.
- Caching: Implemented caching strategies using Django's cache framework and WhiteNoise for static assets.
- Minification: Minified CSS and JavaScript files to reduce load times.
- Lazy Loading: Images and resources are loaded lazily to improve initial page load performance.

**Final Notes**
 
**Additional Documentation**

**Future Enhancements**
- **Data Analysis:** Implement data visualization tools to analyze user data and track progress.
- **Visual Charts:** Integrate charts to represent the progress of goals, workouts, and nutrition.
- **Notifications:** Add notifications to alert users when they complete a task or reach a milestone.
- **Mobile Application:** Develop a mobile version of Fitness Diary for on-the-go access.
- **Integration with Wearables:** Connect Fitness Diary with wearable devices to automatically log fitness data.
