# Secret Santa Application

## Overview

This Secret Santa application allows users to organize gift exchanges efficiently, ensuring that each participant both gives and receives a gift while adhering to any specified blacklist constraints. It is ideal for groups, companies, or communities looking to automate their Secret Santa draws.

## Features

### Main
- Participant Management: Users can compile and manage a list of participants.
- Blacklist Configuration: Users can assign blacklist to prevent certain people from drawing certain people.
- Draw Mechanism: A draw system that allows to get the complete list of relationships ensuring that each participant receives a gift and has to offer one while taking into account their potential blacklist.
- History Access: Users can access the history of the last 5 draws.

### Optional
- User Authentication: Secure login system to manage sessions and keep the draws private.
- Email Notifications: Automated emails to participants to notify them of the draw.
- User Authorization: Some users can create a draw, some can only access it.

## Tech Stack
- Docker / Docker Compose
- Django / Django Rest Framework / Postgres
- Vue

## TODO
- [x] Setup dev environment
- [x] Design the data model
- [x] Design the API
- [x] Create the API
- [x] Write fixtures
- [x] Add tests
- [x] Implement the draw feature
- [x] Add the history feature
- [x] Create the frontend
- [x] Integrate the API and the frontend
- [ ] Deploy the application

## Run

```bash
docker compose up
```

## Create the database

```bash
docker compose exec backend python manage.py migrate
```

## Load test data

```bash
docker compose exec backend python manage.py loaddata participants blacklists
```

## Test

```bash
docker compose exec backend python manage.py test
```

## Usage

### Create a participant
```bash
curl -X POST http://localhost:8000/api/participants/ -d '{"name": "John", "email": "john@example.com"}'
```

### Get all participants
```bash
curl -X GET http://localhost:8000/api/participants/
```

### Create a blacklist
```bash
curl -X POST http://localhost:8000/api/blacklists/ -d '{"participant": 1, "cannot_receive_from": 2}'
```

### Delete a blacklist
```bash
curl -X DELETE http://localhost:8000/api/blacklists/1/
```
