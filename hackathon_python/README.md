# Time Logger Web Application (Hackathon Project)

## Project Overview

This is a simple web application built with Python and the Flask framework for our hackathon project. The application allows users to perform basic time-tracking operations. Users can add the current timestamp, remove the most recently added timestamp, and view a list of all recorded timestamps.

The application is designed to be simple and intuitive, with a clean user interface. It serves as a great starting point for understanding the fundamentals of web development with Flask, including routing, templates, and handling user interactions.

## Features

*   **Add Current Time:** Instantly records the current date and time.
*   **Remove Last Time:** Deletes the most recently added timestamp from the record.
*   **Show All Times:** Displays a dedicated page with a complete list of all recorded timestamps.
*   **User Feedback:** Provides flash messages to confirm actions like adding or removing a time.
*   **In-Memory Storage:** Timestamps are stored in a list in memory, which means the data will reset if the server is restarted.

## Directory Structure

The project is located within the `hackathon_python` folder and is organized as follows:

```
/hackathon_python/
├── /templates/
│   ├── home.html         # The main landing page with action buttons
│   └── all_times.html    # The page to display all recorded times
├── app.py                # The main Flask application file (contains all logic)
└── README.md             # This file
```

## Technologies Used

*   **Backend:** Python
*   **Framework:** Flask
*   **Frontend:** HTML, CSS

## Prerequisites

Before you begin, ensure you have the following installed on your system:

*   **Python 3:** [Download Python](https://www.python.org/downloads/)
*   **pip** (Python's package installer, usually comes with Python)

## Setup and Installation

Follow these steps to get the project up and running on your local machine.

**1. Navigate to the Project Directory**

From your current location (`~/OneDrive - Sherwin-Williams/Desktop/Vite_Steps`), navigate into the Python project folder.

```bash
cd hackathon_python
```

**2. Create a Virtual Environment (Recommended)**

It's a best practice to create a virtual environment inside the project folder to keep dependencies isolated.

*   **On macOS/Linux/MINGW64:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

*   **On Windows (Command Prompt/PowerShell):**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

**3. Install Dependencies**

Once your virtual environment is activated, install the necessary Python packages.

```bash
pip install Flask
```

## Running the Application

Once the setup is complete, you can run the application.

**1. Start the Flask Server**

**Important:** Make sure you are inside the `hackathon_python` directory before running the next command.

```bash
python app.py
```

**2. Access the Application**

You should see output in your terminal indicating that the server is running, similar to this:

```
 * Serving Flask app 'app'
 * Running on http://127.0.0.1:5173
Press CTRL+C to quit
```

Open your web browser and navigate to the following URL:

[http://localhost:5173](http://localhost:5173)

You should now see the home page of the Time Logger application, just like in the screenshot.

## How to Use the Application

The user interface is straightforward:

*   **Add Current Time:** Click this button to save the current server time. A confirmation message will appear.
*   **Remove Last Time Page:** Click this button to delete the last time that was added. If no times are recorded, it will notify you.
*   **Show All Times Page:** Click this button to navigate to a new page that lists all the timestamps you have recorded so far.