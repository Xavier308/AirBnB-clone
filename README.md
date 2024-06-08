# This is a clone version of AirBnB using Python 3, flask, Docker

This App create user and manage their data, also it manage: places, cities, countries, ammenities and reviews.

![UML Diagram](/assets/rental_clone_app2.webp)



### App implemented by Xavier J Cruz using documetantion provide by Holberton School


## Dependencies & enviroment

It is recommendend to use a virtual enviroment to work with this project. You can create it with the following command:
'python -m venv myenv'


Check the 'requirements.txt' file to see all the dependencies necessary for this project

To know wich dependencies you have in your project use
the command: 'pip freeze > requirements.txt'
It will create a file with all the dependencies you have.

To install the dependecies necessary for the project
you can use the command: 'pip install -r requirements.txt'

## Consistency Across Environments

To ensure consistency across different development environments and potentially in production, consider the following:

Locking Dependencies: 
Tools like pipenv or Poetry can lock your project to specific versions of libraries to ensure that your project doesn’t accidentally get incompatible updates.

Docker: For even greater consistency, especially when preparing for production, consider using Docker, which containers can replicate the exact software environment across different machines.

## UML SIMPLE Diagram

The first path was to create  a Unified Modeling Language (UML) design. This task is all about planning and visualizing the structure of our system before diving into coding.

This UML diagram should include all the entities discussed (Places, Users, Reviews, Amenities, Country, City) and their relationships. 

![UML Diagram](/assets/UML_SIMPLE_DIAGRAM.png)



## Layered Architecture / n-tier Architecture of the APP

This architectural style organizes the application into logical layers that separate responsibilities, which makes the application easier to manage, maintain, and scale.

```bash
AirBnB Clone/
│
├── app/                       # Application package
│   ├── __init__.py            # Initializes your application as a package
│   ├── config.py              # Configuration settings and environment variables
│   │
│   ├── models/                # Data models
│   │   ├── __init__.py        # Makes models a package and imports all models
│   │   ├── user.py            # User model
│   │   ├── place.py           # Place model
│   │   ├── review.py          # Review model
│   │   ├── amenity.py         # Amenity model
│   │   ├── city.py            # City model
│   │   └── country.py         # Country model
│   │
│   ├── services/              # Business logic and service layer
│   │   ├── __init__.py        # Makes services a package
│   │   ├── user_service.py    # Service functions for user management
│   │   └── place_service.py   # Service functions for place management
│   │
│   ├── api/                   # API endpoints
│   │   ├── __init__.py        # Initializes the API blueprint
│   │   ├── user_routes.py     # Routes for user management
│   │   └── place_routes.py    # Routes for place management
│   │
│   ├── persistence/           # Data persistence layer
│   │   ├── __init__.py        # Initializes persistence package
│   │   ├── interface.py       # Persistence interface
│   │   └── data_manager.py    # DataManager implementation
│   │
│   └── utils/                 # Utility functions and classes
│       ├── __init__.py        # Makes utils a package
│       └── helpers.py         # Helper functions and utilities
│
├── tests/                     # Test suite
│   ├── __init__.py            # Initializes tests as a package
│   ├── test_config.py         # Tests for configuration settings
│   ├── models/                # Tests for models
│   │   ├── __init__.py        # Initializes model tests
│   │   ├── test_user.py       # Tests for the User model
│   │   └── test_place.py      # Tests for the Place model
│   └── services/              # Tests for services
│       ├── __init__.py        # Initializes service tests
│       ├── test_user_service.py # Tests for user services
│       └── test_place_service.py # Tests for place services
│
├── Dockerfile                 # Dockerfile for containerizing the application
├── requirements.txt           # Project dependencies
└── README.md                  # Project overview and setup instructions
```

### Components of Layered Architecture

- Presentation Layer (API endpoints): This is where the application handles all the user interface and browser communication logic. In a web application like yours, this layer is represented by the api/ directory, which contains the Flask routes that serve as the interface to the outside world.

- Business Logic Layer (Services): This layer processes the application's business logic. It acts as a mediator between the presentation layer and the persistence layer, handling business rule validation, and makes logical decisions and evaluations. It's found in your services/ directory.

- Persistence Layer (Data Persistence): This layer is responsible for storing and retrieving data from a database or any other storage system. Your project uses the persistence/ directory to manage data interactions, abstracting the details of data access away from the business logic layer.

- Models: These are classes that represent the data structures and possibly the business rules of the application. They often map directly to database tables. In your project, this is managed under the models/ directory.

- Utility Layer: This includes utilities and helper functions which are used across the application. In your project, these are stored in the utils/ directory.

- Tests: This is where you maintain all unit and integration tests, ensuring that your application functions as expected. The tests/ directory in your structure plays this role.


### Additional Components
Dockerfile: Helps in containerizing the application, making it portable and consistent across any deployment environment.

requirements.txt: Manages all project dependencies, ensuring that all necessary libraries are installed to run the application.

### Pending more information and resources



README.md: Documentation on the project setup, configuration, and general overview, guiding new developers or users of the application.

This layered architecture helps in separating concerns, making the application easier to extend and maintain. It allows developers to work on one layer without the need to know every detail of other layers, provided the interfaces between layers are well-defined. This structure is widely used in complex applications that require scalability, maintainability, and flexibility.
