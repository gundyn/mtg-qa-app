# Wizardly Questions

An API for discustion over Magic the Gathering rules. 

Have you ever been playing a game of Magic and been uncertian on the ruling for a specific situation? If so you are not alone! This app is a place for players to post questions and have other players weigh in on how the rules should be interpreted. Odds are someone has run into the same situation you find yourself in!

- - - 

*Wizardly client repo*
(https://github.com/gundyn/mtg-qa-react)

*Wizardly client deployed*
(https://gundyn.github.io/mtg-qa-react/)

*Wizardly django api repo*
(https://github.com/gundyn/mtg-qa-app) 

*Wizardly django api deployed*
(https://mtg-qa-app.herokuapp.com/) 

- - -
## Installation
1. Fork and clone this repository.
2. Create a new branch for your work 
3. Checkout to the branch.
4. Run ```pipenv shell``` to start up your virtual enviorment.
5. Run ```pipenv install``` to install dependencies.
6. Create a psql database for the project
    i. Type ```psql``` to get into interactive shell
    ii. Run ```CREATE DATABASE "name-of-your-database";```
    iii. exit shell ```\q```
7. Generate and run migrations with ```python3 manage.py makemigrations``` and ```python3 manage.py migrate```
8. Run the server with ```python3 manage.py runserver

- - -
## Routes 
**Questions**
| HTTP Method   | URL Path     | Result            |
|:--------------|:-------------|:------------------|
| GET           | /questions     | list of questions   |
| GET           | /questions/:id | single question  |
| POST          | /questions/       | create question       |
| PATCH         | /questions/:id | update question       |
| DELETE        | /questions/:id | delete question      |
**Answers**
| HTTP Method   | URL Path     | Result            |
|:--------------|:-------------|:------------------|
| GET           | /answers     | list of questions   |
| GET           | /answers/:id | single question  |
| POST          | /answers/       | create question       |
| PATCH         | /answers/:id | update question       |
| DELETE        | /answers/:id | delete question      |

- - - 
## Planning Story
Given the Client Specifications I was able to breakdown the overall API into a series of smaller tasks to complete. After the creation of the API the next step was to set up API communication with the React App. Following that my plan was to tackle the CRUD actions one at a time starting with CREATE. After Create was working I wanted to set up INDEX, PATCH, and DELETE, testing of each of these routes was done using postman.

Creating the question routes was planned to be first followed by creating the answer routes. Then I need to set up a many-to-one relationship between Answers and Questions

-Client Specifications-  


- Use Django to build an API.
- Create at least 4 RESTful routes for handling GET, POST, PUT/PATCH, and DELETE requests for a resource other than User.
- Have at least 1 resource that has a relationship to User
- Any actions which change data must be authenticated and the data must be "owned" by the user performing the change or a user determined by an access control list

- - -
## Technologies used
- Javascript
- Python
- CSS
- Shell

- - -
## Unsolved Problem
- veiw question/answer owner as an email and not a number
 
- - -
## Images

![Imgur Image](https://imgur.com/G572R6Z.jpg)
