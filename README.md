# CS50W Project 1 - Wiki

This project is part of the Harvard University's CS50W course on Web Programming with Python and JavaScript. It's an implementation of a simple online encyclopedia, similar to Wikipedia, using Django (without models), HTML, and CSS.

## Description

This web application serves encyclopedia entries to users, which are stored as Markdown files. When a user requests to view an entry, the markdown file is converted to HTML for display in the browser. Features of the web application include:

- Viewing individual encyclopedia entries
- Listing all encyclopedia entries
- Searching for an encyclopedia entry
- Creating a new encyclopedia entry
- Editing an existing encyclopedia entry
- Viewing a random encyclopedia entry

For detailed project requirements, refer to the project specifications on the CS50W course website [here](https://cs50.harvard.edu/web/2020/projects/1/wiki/).

## Getting Started

To run this project locally, you need Python and pip installed on your system. If you don't have Python and pip installed, visit the [official Python website](https://www.python.org/downloads/) and follow the instructions there.

```

1. **Install the dependencies**

```

pip install -r requirements.txt

```

2. **Run the application**

```

python manage.py runserver

```

Then, open your browser and visit `http://localhost:8000` to see the application in action.
```
