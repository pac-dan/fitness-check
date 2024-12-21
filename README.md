# Fitness Diary

Fitness Diary is a full-stack web application designed to help users record their fitness goals, log workouts, and track nutritional intake. Built with Django, HTML, CSS, and Bootstrap, this application showcases comprehensive CRUD (Create, Read, Update, Delete) operations within a user-friendly interface. 

**Table of Contents**
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
- Contact
- Screenshots
- UX Design Documentation
- Performance Optimization
- Additional Documentation

**Project Overview** 
Fitness Diary aims to provide users with a centralized platform to record and achieve their fitness objectives. Whether it's increasing daily steps, logging workouts, or managing nutritional intake, Fitness Diary is a way to digitally record your fitness journey so you can see improvement and encourage yourself to continue.

## Features 
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

## Testing

Ensuring the reliability and robustness of Fitness Diary through comprehensive testing.

### Manual Testing
- **User Flow Testing**: Verified all user flows, including registration, goal setting, workout logging, and nutrition tracking.
- **Responsive Design Testing**: Ensured the application is responsive across various devices and screen sizes.
- **Accessibility Testing**: Checked compliance with accessibility standards using tools like WAVE and Lighthouse.

## Technology Stack
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

## Agile Methodology 
Fitness Diary was developed using the Agile methodology, ensuring iterative progress and adaptability throughout the project lifecycle.

**Link to Github Projects** - https://github.com/users/pac-dan/projects/1
- You can view the comprehensive Agile board for Fitness Diary here. This board includes all project Epics, User Stories, tasks and progress tracking.
- Epics and User Stories: Clearly defined Epics broken down into actionable User Stories, each addressing specific functionalities and requirements of the application
- Task Tracking: Real-time updates on task statuses (To Do, In Progress, Done) to monitor development progress and identify any bottlenecks.

**User Stories**

### User Stories

**Epic 1: User Management**
  - As a user, I want to register and log in so that I can securely access my fitness data.
  - As a user, I want to update my profile information to keep my account details current.

**Epic 2: Goals Management**
  - As a user, I want to create fitness goals so that I have targets to achieve.
  - As a user, I want to view my goals to track my progress.
  - As a user, I want to update or delete my goals as my objectives change.

**Epic 3: Workouts Logging**
  - As a user, I want to log my workouts to monitor my exercise routines.
  - As a user, I want to view my workout history to analyze my performance over time.
  - As a user, I want to update or delete my workouts as my objectives change.

**Epic 4: Nutrition Logging**
  - As a user, I want to log my meals to track my nutritional intake.
  - As a user, I want to view my nutrition history to manage my diet effectively.
  - As a user, I want to update or delete my nutrition logs as my objectives change.

### Epics to User Stories Mapping

| **Epic**               | **User Stories**                                                                                                                                                    |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **User Management**    | - As a user, I want to register and log in so that I can securely access my fitness data.<br>- As a user, I want to update my profile information to keep my account details current. |
| **Goals Management**   | - As a user, I want to create fitness goals so that I have targets to achieve.<br>- As a user, I want to view my goals to track my progress.<br>- As a user, I want to update or delete my goals as my objectives change. |
| **Workouts Logging**   | - As a user, I want to log my workouts to monitor my exercise routines.<br>- As a user, I want to view my workout history to analyze my performance over time.<br>- As a user, I want to update or delete my workouts as my objectives change. |
| **Nutrition Logging**  | - As a user, I want to log my meals to track my nutritional intake.<br>- As a user, I want to view my nutrition history to manage my diet effectively.<br>- As a user, I want to update or delete my nutrition logs as my objectives change. |


**UX Design Documentation**

Add a section to document your UX design process, including wireframes and design decisions.

## UX Design Documentation

### Design Process
The design of Fitness Diary focused on creating a user-friendly and accessible interface without formal wireframes. Key considerations included:

- **User-Centric Layout:** Organized the application into intuitive sections: Dashboard, Goals, Workouts, Nutrition, and Profile.
- **Consistent Navigation:** Implemented a consistent header and sidebar for easy navigation across different sections.
- **Responsive Design:** Utilized Bootstrap 5 to ensure the application is fully responsive on all devices.
- **Accessibility:** Followed WCAG guidelines to make the application accessible to users with disabilities.

### Design Decisions
- **Clean and Minimalistic Design:** Chose a minimalistic approach to reduce clutter and help users focus on their fitness tracking.
- **Real-Time Feedback:** Ensured that CRUD operations provide immediate feedback to enhance user experience.
- **Mobile-First Approach:** Prioritized mobile responsiveness to cater to users who prefer accessing the application on-the-go.

### Visual Representations
I also used physical diagrams for the simple design layout and using bootstrap for layout and design it was super easy to get the website layout, i kept the design very simple not to complicate the view of the page.

While formal wireframes are not provided, the following annotated screenshots illustrate the final design and layout of the application:

- **Home Page**
  ![Home Page](static\images\home.png)(static\images\home.png)
  *Annotation: The home page features a dashboard overview with quick access to goals, workouts, and nutrition sections.*

- **Goals Page**
  ![Goals Page](static\images\goals.png)
  *Annotation: Users can create, view, update, and delete their fitness goals. Progress is tracked with visual indicators.*

- **Workout Page**
  ![Workout Page](static\images\workouts.png)
  *Annotation: The workout logging interface allows users to input workout details and view their workout history.*

- **Nutrition Page**
  ![Nutrition Page](static\images\nutrition.png)
  *Annotation: Users can log their meals, track caloric intake, and manage dietary plans.*

- **User Profile Page**
  ![User Profile Page](static\images\user_profile_page.png)
  *Annotation: Profile management section where users can update their personal information and preferences.*

### Alignment with User Stories
Each design decision aligns with specific user stories to ensure that the application meets user needs effectively. For example:

- **User-Centric Layout** aligns with the user story: *"As a user, I want to view my goals to track my progress."*
- **Real-Time Feedback** supports: *"As a user, I want to log my workouts to monitor my exercise routines."*

**Installation**
- Prerequisites 
    - Python 3.8+
    - pip 
    - Git

**Steps**
- Clone the Repository:
    - git clone https://github.com/pac-dan/fitness-check.git
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
- Thank you for reviewing my project, I really enjoyed using the class based views and learning so much in this stage of the course, I hope it was okay to use class based functions as i was told mixed things.

**Future Enhancements**
- **Data Analysis:** Implement data visualization tools to analyze user data and track progress.
- **Visual Charts:** Integrate charts to represent the progress of goals, workouts, and nutrition.
- **Notifications:** Add notifications to alert users when they complete a task or reach a milestone.
- **Mobile Application:** Develop a mobile version of Fitness Diary for on-the-go access.
- **Integration with Wearables:** Connect Fitness Diary with wearable devices to automatically log fitness data.

**Links**
- Visit https://fitness-tracker-project-b28eeb139905.herokuapp.com/ in your browser.
- Link to Github Projects https://github.com/users/pac-dan/projects/1
