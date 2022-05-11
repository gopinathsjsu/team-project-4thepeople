# Team Project
## Group Name - 4thepeople

## Project Repo Branches Description
1. dev-aryan : created for the development work assigned to aryan-jadon.
2. dev-harika: created for the development work assigned to harika-nalam.
3. dev-swathi: created for the development work assigned to swathi-anandram.
4. dev-shreya: created for the development work assigned to shreya-nimbhorkar.
5. main: codebase deployed to the production environment.


## Project Folder Description
1. frontend - contains the frontend apps codebase. 
2. backend - contains the backend apps codebase.
3. documentation - contains the documentation of the backend module.
4. demo_screenshots - contains the screenshots of the website and API's.
5. images - contains the images used for hotel records in database.
6. mailServer - Email and Message Sending Serverless APP

## Scrum Meeting
We have weekly meetings on Fridays and each sprint starting from  Mondays and lasting for a week.

## Weekly Scrum Task Board and Burndown Chart
[Weekly.Scrum.Task.Board.xlsx](https://github.com/gopinathsjsu/team-project-4thepeople/files/8660142/Weekly.Scrum.Task.Board.xlsx)


## Sprint Journal
[SPRINT_JOURNAL.xlsx](https://github.com/gopinathsjsu/team-project-4thepeople/files/8660236/SPRINT_JOURNAL.xlsx)


## XP Core Values

1) Communication: Everyone on a team works jointly at every stage of the project. We have clear communication between us by conducting meetings regularly on Zoom, Slack and WhatsApp. We make sure every body has a clear understanding of what is being done for every user story.


2) Simplicity: We strive to write simple code bringing more value to a product, as it saves time and effort. We brainstorm and come up with simpler solutions to make the code readable and simple to anyone. We are focused on the necessary components that are required for a successful Hotel Management System. 

3) Feedback: We constantly get feedback on the work that is being done as it provides a space for improvement by taking the positives of every feedback and improving the product accordingly.

## Functionality of Project
Customer Dashboard

1. Customer can Signup to create his profile with all the validations which checks if all the fields are entered properly, password has minimum of 8 characters, if the passwords match when confirming password, if the user already exists and if the the username and password is similar.
2. Upon successful signup, user can login where the username and password is validated.
3. User can search for hotels with location, date range and price range fields. User can search without populating location too.
4. When user searches for weekday hotels, the prices are normal, but on weekends the dynamic pricing logic makes the price higher.
5. Upon booking a room, user gets 50 reward points and an email is sent to the user with booking details.
6. User can view his rewards and his levels which are silver, gold and diamond on view rewards page.
7. User can view his bookings on view bookings tab.
8. User can edit or delete his bookings.

Employee Dashboard

1. Employee dashboard enables the employees to delete or edit a booking
2. Employee can also add rooms


## Architecture Diagram
![Architecture202-4](https://user-images.githubusercontent.com/60109870/167284899-67d00010-65d0-4f39-ad29-ea435cc2ddf3.jpg)

## Class Diagram

![visual](https://user-images.githubusercontent.com/60109870/167354665-541c016e-807a-403f-ad5d-f9f50c2a86a8.png)

## Use Case Diagram

![UseCaseDiagram202group](https://user-images.githubusercontent.com/60109870/167540517-6f6a6b1c-0f7a-47ad-82cf-9a14e8ee2a2d.jpg)


## Tech Stack used

1) frontend - Angular v12, JavaScript, HTML5, CSS3, Bootstrap
2) backend - Django Rest framework
3) database - Postgres v13
4) cloud provider - Digital Ocean

## Contributions

The work is divided in a uniform manner so that everybody gets a chance to work on all the 4 major divisions with taking up user stories of their expertise as as their major contributions.

1) Aryan Jadon - Backend and Frontend
2) Swathi Anandram - Backend and Frontend
3) Shreya Nimbhorkar - Backend and Frontend
4) Harika Nalam - Backend and Frontend


## UI Wireframes

Search Page:

![search](https://user-images.githubusercontent.com/60109870/167287966-9f9e4f0f-8f64-4e26-9de9-406a50eb9bd2.png)



Sign Up:

![signup_page](https://user-images.githubusercontent.com/60109870/167287908-81bde73c-346c-4c31-8b47-c48c25bb3a89.png)


Login:

![login_page](https://user-images.githubusercontent.com/60109870/167287934-e9d1e2d8-2489-40f9-ac23-07507da41621.png)


Reservation Form:
![hotel_booking_form](https://user-images.githubusercontent.com/60109870/167287948-17e8f074-a9fc-408c-a7e9-30fd5e2f3be3.png)

## Design Patterns Used

### Decorator
Decorator is a structural design pattern that lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.
Decorator Pattern is used during login check module, if admin tried to login, it will be redirected to a Hotel dashboard and if users tried to login- it will be redirected to a user profile page. 

### Pros and Cons of Decorator Pattern

### Pros 
1. You can extend an object’s behavior without making a new subclass.
2. You can add or remove responsibilities from an object at runtime.
3. You can combine several behaviors by wrapping an object into multiple decorators.
4. Single Responsibility Principle. You can divide a monolithic class that implements many possible variants of behavior into several smaller classes.

### Cons
1. It’s hard to remove a specific wrapper from the wrappers stack.
2. It’s hard to implement a decorator in such a way that its behavior doesn’t depend on the order in the decorators stack.
3. The initial configuration code of layers might look pretty ugly.

### Strategy
1. We have used strategy dynamic pricing. For dynamic pricing, we have designed three different strategies and these three strategies are based on the day the customer booking hotel rooms. We have considered three different types of days that a customer can book rooms, weekdays, weekends, and holidays. Depending on the day customer requested for booking pricing differs. 
2. For weekdays the price there will be no increase in the base price, coming to weekend booking the price increases by 5% and for booking on holidays the price increases by 10 % over the base price. 

### Pros: 
  The algorithm is loosely coupled and can be changed, replaced and it is easy to extended
### Cons:
  Should understand how strategies differ. Number of objects increases 
  
### Observer
1. We have used an observer design pattern to notify the hotel management when a customer books a room and also sends the customer booking confirmation. 
2. The customer receives an email upon successful booking as a confirmation which helps him while check-in. 
3. The hotels get notified through mail about room booking with customer details and prepare for customer visits.

### About Django Design  Pattern
Django App four essential components.

1. Models (models.py): POPOs (plain old python objects) classes to communicate with Database and preserve the data in OOP manner.
2. Forms (forms.py): To collect the data from the users.
3. Views (views.py): Central controller to handle the user’s request and communicate to model objects. IT is like “servlets” of JavaEE.
4. Templates(templates folder): Display response to the users in a generalized structure with customized information.

![Django Patterns](https://raw.githubusercontent.com/gopinathsjsu/team-project-4thepeople/main/images/Django_Design_Pattern.png)
