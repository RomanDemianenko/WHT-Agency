# REPOSITORY: WHT Agency

## ABOUT
This project is a web-based API developed using Django Rest Framework (DRF). Its primary goal is to provide a systematic way to manage teams and their respective members. With a streamlined and intuitive interface, users can create, read, update, and delete both team and user entries, ensuring efficient team management for organizations or platforms that require such functionality.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and 
testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

These instructions are valid for Mac or Linux. 

You need to install following software:
* [Docker](https://docs.docker.com/install/)
* [Docker-compose](https://docs.docker.com/compose/install/)
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Installing

Clone git-repositories:
```bash
git@github.com:RomanDemianenko/WHT-Agency.git
```

Change the work directory to cloned project root dir:

```
cd why_agency
```

**Run the project**
```bash
docker-compose up
```
Run in daemon mode (in the background) 
```bash
 docker-compose up -d
``` 
If this is not your first run and you have changed the requirements, rebuild the existing images.
```bash
 docker-compose up --build
```

### Project resources
**Local uri**

- http://localhost:8000/api/ - Backed API

## API Collection

To test our API endpoints, you can use our Postman collection. Follow the steps below:

1. Download the [Postman Collection](wht_agency.postman_collection.json).
2. Import the JSON file into your Postman application.
3. Start making requests!


## Built With

* [Docker](https://docs.docker.com/install/) – used for auto-deployment and 
  management the applications and create containers.
* [Docker-compose](https://docs.docker.com/compose/install/) – used for running 
  multiple Docker containers and build and manage them local.
* [Django](https://www.djangoproject.com/) – API, ORM.
