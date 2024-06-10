# AirBnB-Clone Project: Part 1 Guide

Welcome to the HBnB Evolution Project, a clone of AirBnB's API crafted using Python 3, Flask, and Docker. This application enables the creation and management of data concerning users, places, cities, countries, amenities, and reviews. The initial phase focuses on developing the API modules and business logic essential for future integrations with SQL databases and front-end technologies.

![UML Diagram](/assets/rental_clone_app2.webp)


## Implemented by Xavier J Cruz
Documentation provided by Holberton School.

# What’s Cooking in Part 1?

## Key Activities

- **Sketching with UML**: Start by designing the application architecture using UML, laying the groundwork for how components interact.
- **Testing Our Logic**: Develop tests for both the API and business logic to ensure reliability.
- **Building the API**: Use Flask to bring your UML diagrams to life, creating a functional API that interacts with a file-based persistence layer.
- **File-Based Data Storage**: Implement a simple file-based storage system to begin, planning for a seamless transition to databases in the future.
- **Packaging with Docker**: Containerize your application with Docker for easy deployment and scalability.

## Project Structure

The project is structured into three primary layers:

### Services Layer
- Manages API interactions.

### Business Logic Layer
- Handles data processing and business rules.

### Persistence Layer
- Currently a file system, to be migrated to a database.

## Key Entities

- **Places**: Core to our application, representing properties available for booking.
- **Users**: Can be hosts or reviewers, interacting with places.
- **Reviews and Amenities**: Feedback and features of places.
- **Country and City**: Geographic categorization of places.

## Business Logic

- **Unique Identifiers**: Using UUID4 for ensuring each entity is unique.
- **Creation and Update Timestamps**: For traceability.

## Technologies Used

- Python
- Flask & Flask-RESTx
- Docker
- JSON/XML for file storage

## Setup and Installation

Instructions for setting up and installing the project will be provided, ensuring users can get started with minimal setup.

```bash
# Clone the repository
git clone git@github.com:Xavier308/AirBnB-clone.git

# Navigate to the project directory
cd airbnb-clone

# Build the Docker container
docker build -t airbnb-clone .

# Run the container
docker run -p airbnb-clone

```

## Dependencies & Environment Setup

### It is recommended to use a virtual environment for this project. Set one up using:

```bash
python -m venv myenv
```

This project was built using Debian GNU/Linux 12 (bookworm). All necessary dependencies are listed in the requirements.txt file. To install these dependencies, run:

```bash
pip install -r requirements.txt
```
To know wich dependencies you have in your project use
the command and create a file with all the dependencies you have: 
```bash
pip freeze > requirements.txt
```

## Consistency Across Environments
To ensure consistency across various development environments and in preparation for production, consider:

- Locking Dependencies: Use tools like pipenv or Poetry to lock your project to specific library versions, preventing incompatible updates.

- Using Docker: For enhanced consistency, especially for production, encapsulate your application within Docker containers. This ensures that it runs identically on any system.

## UML Diagram Overview
The project began with designing a Unified Modeling Language (UML) diagram to plan and visualize the system's structure before coding.

![UML Diagram](/assets/UML_SIMPLE_DIAGRAM.png)

## Layered Architecture
This project utilizes a layered (n-tier) architecture to separate responsibilities, which simplifies management, maintenance, and scalability.

### Directory Structure Overview:

```bash
airbnb_clone/
├── app/                        # Main application codebase
│   ├── api/                    # API endpoints handling client-server interactions
│   │   ├── amenity_routes.py   # Routes for amenity-related operations
│   │   ├── location_routes.py  # Routes for location-related operations
│   │   ├── place_routes.py     # Routes for place-related operations
│   │   ├── review_routes.py    # Routes for review-related operations
│   │   └── user_routes.py      # Routes for user-related operations
│   ├── app.py                  # Entry point for initializing the Flask app
│   ├── config.py               # Configuration settings for the application
│   ├── models/                 # Data models representing database schema
│   │   ├── amenity.py          # Amenity data model
│   │   ├── city.py             # City data model
│   │   ├── country.py          # Country data model
│   │   ├── place.py            # Place data model
│   │   ├── review.py           # Review data model
│   │   └── user.py             # User data model
│   ├── persistence/            # Data access layer, interfacing with the database
│   │   ├── data_manager.py     # Manages database operations
│   │   └── interface.py        # Defines interface for database interactions
│   ├── services/               # Business logic, processes data between API and persistence layers
│   │   ├── amenity_service.py  # Business processes for amenities
│   │   ├── city_service.py     # Business processes for cities
│   │   ├── place_service.py    # Business processes for places
│   │   ├── review_service.py   # Business processes for reviews
│   │   └── user_service.py     # Business processes for users
│   └── utils/                  # Utility functions and helpers used across the application
│       └── helpers.py          # Contains utility functions
├── assets/                     # Static files like images and documents
│   ├── README.md               # Additional information for the assets directory
│   ├── rental_clone_app2.webp  # Image file example
│   └── UML_SIMPLE_DIAGRAM.png  # UML diagram of the project structure
├── Dockerfile                  # Instructions for Docker on how to build the application container
├── README.md                   # Main project documentation for developers and users
├── requirements.txt            # List of project dependencies
└── tests/                      # Contains all tests for the application components
    ├── api/                    # Tests for API routes
    ├── models/                 # Tests for data models
    ├── persistence/            # Tests for persistence layer
    ├── services/               # Tests for business logic services
    └── utils/                  # Tests for utility functions
```
### Generate this diagram using the command:

```bash
tree -I '__pycache__' /path/to/app
```

## Installation of Tree Command

For consistent directory structure visualization, install `tree` using the following commands based on your operating system:

- **Ubuntu/Debian:**
```bash
  sudo apt install tree
```

  - **CentOS/RHEL:**
```bash
  sudo yum install tree
```

  - **macOS (using Homebrew):**
```bash
  brew install tree
```

  ## Components of the Layered Architecture

### Presentation Layer (API endpoints)
- **Location:** `api/` directory
- **Functionality:** Handles all UI and browser communication logic through Flask routes.

### Business Logic Layer (Services)
- **Location:** `services/` directory
- **Functionality:** Processes the application's business logic, acting as a mediator between the presentation layer and the persistence layer, handling business rule validation, and making logical decisions and evaluations.

### Persistence Layer (Data Persistence)
- **Location:** `persistence/` directory
- **Functionality:** Responsible for storing and retrieving data from a database or any other storage system. The project currently uses a file-based system, planned to transition to a database.

### Models Layer
- **Location:** `models/` directory
- **Functionality:** These classes represent the data structures and possibly the business rules of the application. They often map directly to database tables.

### Utility Layer
- **Location:** `utils/` directory
- **Functionality:** Includes utilities and helper functions which are used across the application to support various functionalities.

### Tests Layer
- **Location:** `tests/` directory
- **Functionality:** Maintains all unit and integration tests, ensuring that your application functions as expected.

## Additional Components

### Dockerfile
- **Purpose:** Helps in containerizing the application, making it portable and consistent across any deployment environment.

### requirements.txt
- **Purpose:** Manages all project dependencies, ensuring that all necessary libraries are installed to run the application.

### README.md
- **Purpose:** Provides documentation on the project setup, configuration, and general overview, guiding new developers or users of the application.

## Integration of Flask-RESTx

In this project, we have transitioned from using Flask's Blueprint system to Flask-RESTx for defining our API routes and logic. This change enhances the structure and functionality of our application by utilizing Flask-RESTx's extended capabilities.

### Why Flask-RESTx Over Blueprints?

Flask-RESTx is an extension for Flask that adds support for quickly building REST APIs. It encourages best practices and handles much of the boilerplate code for setting up API routes, request validation, and response marshalling.

### Benefits of Using Flask-RESTx

- **Simplified Data Marshalling**: Automatically marshal and unmarshal data according to predefined schemas. This ensures that incoming and outgoing data is formatted correctly, reducing errors and simplifying data handling.
  
- **Automatic Documentation**: Flask-RESTx integrates with Swagger to provide out-of-the-box API documentation. This makes it easier for developers to understand and use the API, as all available endpoints, parameters, and expected request/response formats are well-documented.
  
- **Input Payload Validation**: Flask-RESTx allows for easy input validation, ensuring that received data meets the API’s requirements before processing. This reduces the amount of error handling code needed in the business logic.
  
- **Resourceful Routing**: Utilize the resourceful routing provided by Flask-RESTx to organize API endpoints more intuitively. This aligns API design with REST standards, making it more maintainable and scalable.
  
- **Error Handling**: Improve error handling capabilities with built-in handlers in Flask-RESTx, which can be customized for different types of exceptions. This feature standardizes API error responses, making the API more reliable and easier to debug.

### Transitioning from Blueprints to Flask-RESTx

Transitioning from Blueprints to Flask-RESTx involves defining `Namespace` objects instead of `Blueprints`, and `Resource` classes instead of route functions. Each `Resource` class encapsulates the logic for a specific part of the API, promoting clean separation of concerns and making the codebase easier to understand and maintain.

Here's a simple example of how a Flask Blueprint route might be transformed into a Flask-RESTx Resource:

```python
# Using Flask Blueprint
from flask import Blueprint
blueprint = Blueprint('example', __name__)

@blueprint.route('/example', methods=['GET'])
def get_example():
    return "Example data"

# Using Flask-RESTx
from flask_restx import Resource, Api, Namespace
api = Namespace('example')

@api.route('/example')
class ExampleResource(Resource):
    def get(self):
        return "Example data"
```