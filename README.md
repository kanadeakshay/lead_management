# Lead Management

A lead management tool for **CorpsComp** competition organised by IIT BOMBAY.

## Table of Contents :

- [Introduction](#introduction)
- [Design](/docs/images/)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Local Setup](#local-setup)
- [Authors](#authors)

### Introduction

Lead Management is a software solution for **Problem Statement 1** of **CorpsComp** competition organised by IIT BOMBAY in September 2020.
You can read the whole problem statement here 👉 [CorpsComp-PS](/docs/problem_statement)

### Features

- **Authentication** : We have added authentication so that the user/employee first need to register on our side using his/her employee/user id and setup a password and then he can login in the website.

- **Dashboard** : We have a dashboard on which you can see all the activities that happened on the website. i.e., all the leads assigned to and submitted by other users.

- **Profile Page** : Each user has their profile page, where he can see his info and leads assigned to him and previous leads submitted by him.

- **New Lead Form** : Each user can add a new lead in the system and assign it to other users. The default(initial) status of every lead is OPEN.

- **Edit(Validate) Lead Form** : The user can change the status of the lead after it is assigned to him. He can either validate the lead or reject and then the lead will be closed.

- **Filter Leads** : We have a filter on both leads assigned and leads submitted page through which users can filter all the leads based on their status.

- **Downloadable Data** : The user can download all this data by simply clicking on a button. And all the data will be downloaded as a CSV file.

### Tech Stack

- Fronend :
  - HTML
  - CSS
  - Javascript
- Backend :
  - Django

### Local Setup

- Read [CODE OF CONDUCT] check [CONTRIBUTING.md] for contributions.

```bash
git clone https://github.com/akshay782/lead_management.git
git checkout -b <branch-name>
```

```python
python manage.py migrate
python manage.py makemigrations
python manage.py runserver
```

- Go to `http://127.0.0.1:8000/`

```bash
git add .
git commit -m "message"
git push origin <branch-name>
```

### Authors

Team members :

- Akshay Kanade
  - [LinkedIn](https://www.linkedin.com/in/akshaykanade/) | [Github](https://github.com/kanadeakshay)
- Vivek Namaye
  - [LinkedIn](https://www.linkedin.com/in/viveknamaye/) | [Github](https://github.com/viveknamaye)
- Prajyot Pawar
  - [LinkedIn](https://www.linkedin.com/in/prajyot-pawar-579a5834b/) | [Github](https://github.com/prajyotpdev)
