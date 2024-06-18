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
- [ ] Setup dev environment
- [ ] Design the data model
- [ ] Design the API
- [ ] Create the API
- [ ] Write fixtures
- [ ] Add tests
- [ ] Implement the draw feature
- [ ] Add the history feature
- [ ] Create the frontend
- [ ] Integrate the API and the frontend
- [ ] Deploy the application
