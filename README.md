# This is a clone version of AirBnB's API using Python 3, flask, Docker

This App make it posible to create and manage their data of user, places, cities, countries, ammenities and reviews. The first part was creating the API modules and business logic to manage all the data necesary for future integration like database in SQL and front-end.

![UML Diagram](/assets/rental_clone_app2.webp)



## App implemented by Xavier J Cruz using documetantion provide by Holberton School


## Dependencies & enviroment

It is recommendend to use a virtual enviroment to work with this project. You can create it with the following command:
'python -m venv myenv'

The OS used to build this project was Debian GNU/Linux 12 (bookworm).

Check the 'requirements.txt' file to see all the dependencies necessary for this project

To know wich dependencies you have in your project use
the command: 'pip freeze > requirements.txt'
It will create a file with all the dependencies you have.

To install the dependecies necessary for the project
you can use the command: 'pip install -r requirements.txt'

## Consistency Across Environments

To ensure consistency across different development environments and potentially in production, consider the following:

- Locking Dependencies: 
Tools like pipenv or Poetry can lock your project to specific versions of libraries to ensure that your project doesn’t accidentally get incompatible updates.

- Docker: For even greater consistency, especially when preparing for production, consider using Docker, which containers can replicate the exact software environment across different machines.

## UML SIMPLE Diagram

The first step was to create  a Unified Modeling Language (UML) design. This task is all about planning and visualizing the structure of our system models before diving into coding.

This UML diagram include all the entities discussed (Places, Users, Reviews, Amenities, Country, City) and their relationships. 

![UML Diagram](/assets/UML_SIMPLE_DIAGRAM.png)



## Layered Architecture / n-tier Architecture of the APP

This architectural style organizes the application into logical layers that separate responsibilities, which makes the application easier to manage, maintain, and scale.

This is an example of the distribution of files/dir in the app to make it more visual and less abstract but it doesn't show all the actual files.

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
* To make this diagram you can use the command 'tree -I '__pycache__|node_modules' /path/to/app', make sure that you have installed tree in your terminal.

To install it you can use:

On Ubuntu/Debian: sudo apt install tree
On CentOS/RHEL: sudo yum install tree
On macOS: brew install tree (using Homebrew)


This layered architecture helps in separating concerns, making the application easier to extend and maintain. It allows developers to work on one layer without the need to know every detail of other layers, provided the interfaces between layers are well-defined. This structure is widely used in complex applications that require scalability, maintainability, and flexibility.

### Components of Layered Architecture

- Presentation Layer (API endpoints): This is where the application handles all the user interface and browser communication logic. In a web application like the AirBnB-Clone, this layer is represented by the api/ directory, which contains the Flask routes that serve as the interface to the outside world.

- Business Logic Layer (Services): This layer processes the application's business logic. It acts as a mediator between the presentation layer and the persistence layer, handling business rule validation, and makes logical decisions and evaluations. It's found in your services/ directory.

__init__.py: Typically initializes a Flask Blueprint or a Flask-RESTx API, which is used to organize and group the endpoints.

Route files (user_routes.py, place_routes.py, etc.): Define the routes (or endpoints) that handle requests and responses to the client. Each route invokes logic from the service layer and interacts with models to serve data required by the client.

- Persistence Layer (Data Persistence): This layer is responsible for storing and retrieving data from a database or any other storage system. Your project uses the persistence/ directory to manage data interactions, abstracting the details of data access away from the business logic layer.

- Models: These are classes that represent the data structures and possibly the business rules of the application. They often map directly to database tables. In your project, this is managed under the models/ directory.

- Utility Layer: This includes utilities and helper functions which are used across the application. In your project, these are stored in the utils/ directory.

- Tests: This is where you maintain all unit and integration tests, ensuring that your application functions as expected. The tests/ directory in your structure plays this role.


### Additional Components
- Dockerfile: Helps in containerizing the application, making it portable and consistent across any deployment environment.

- requirements.txt: Manages all project dependencies, ensuring that all necessary libraries are installed to run the application.

- README.md: Documentation on the project setup, configuration, and general overview, guiding new developers or users of the application.

## Integration of Flask-RESTx

By integrating Flask-RESTx, you're reorganizing how routes and endpoints are handled, moving from Flask's Blueprint system to a more structured approach using namespaces and resources provided by Flask-RESTx. This setup provides benefits such as automatic API documentation and better organization for your API endpoints.

Remember, each of your resource files (like user_routes.py, place_routes.py) will need to be adjusted to define Resource classes and add them to the respective Namespace. This approach modularizes your API and takes full advantage of Flask-RESTx’s features.

### Pending for more information and resources
