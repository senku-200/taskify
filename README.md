
# Taskify

Taskify is a Django web application for managing tasks efficiently. It allows users to create, edit, delete, and prioritize tasks, and to mark them as completed or incomplete.

## Features

- **User Authentication**: Sign up, log in, and log out.
- **Dashboard**: View all tasks, categorized into completed and incomplete.
- **Task Management**:
  - Create new tasks
  - Edit existing tasks
  - Delete tasks
  - Mark tasks as complete or incomplete
  - Sort tasks by priority

 ## Prerequisites

Before you begin, make sure you have the following prerequisites installed on your system:

- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

## Getting Started

1. **Download and Install Python**:
   - Download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Follow the installation instructions for your operating system and ensure you add Python to your system's PATH during installation.

2. **Clone the Repository**:
   - Open a terminal or command prompt.
   - Run the following command to clone the STUVIBE repository:
     ```
     git clone https://github.com/senku-200/taskify.git
     ```

3. **Navigate to the Project Directory**:
   - Change your current working directory to the taskify directory:
     ```
     cd taskify
     ```

4. **Install Dependencies**:
   - Install the project's Python dependencies using `pip`. Run this command within the 'taskify' directory:
     ```
     pip install -r requirements.txt
     ```

5. **Navigate to the taskify Directory**:
   - Change your current working directory to the 'taskify' directory:
     ```
     cd taskify
     ```

6. **Apply migrations**:
   
     ```
     python manage.py migrate
     ```

7. **Run the Development Server**:
   - Start the Django development server to run the taskify project:
     ```
     python manage.py runserver
     ```

The taskify project should now be running locally on your machine. You can access it by opening a web browser and navigating to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) or [http://localhost:8000/](http://localhost:8000/).

## Contributing

If you'd like to contribute to this project or report issues, please visit the [GitHub repository](https://github.com/senku-200/taskify).





## Usage

1. Register or log in.
2. Use the dashboard to manage your tasks.
3. Create, edit, delete, and mark tasks as complete/incomplete.
