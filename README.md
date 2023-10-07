# MLOps Spam Detection

Welcome to the MLOps Spam Detection project repository. This project focuses on building an email spam classifier using machine learning techniques. By the end of this project, you'll have a trained model capable of classifying emails as either spam or not spam.

## Table of Contents

- [Installation](#installation)
- [Project Overview](#project-overview)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started, you can follow these steps to set up the project on your local machine:

### Prerequisites

- Python 3.6 or higher installed on your system.
- Git installed on your system.

### Clone the Repository

You can clone this repository using the following command:

```bash
git clone https://github.com/phanng0605/MLOps_Spam_Detections.git
```
### Create a Virtual Environment (Optional but recommended)
It's a good practice to create a virtual environment for your project to manage dependencies. You can create one using Python's built-in venv module:
```
python -m venv myenv
```

Activate the virtual environment:

On Windows:
```
myenv\Scripts\activate
```

On macOS and Linux:
```
source myenv/bin/activate
```

Install Dependencies
Navigate to the project directory and install the required packages using pip:
```
pip install -r requirements.txt
```

Project Overview
This project includes the following files and directories:

app.py: The main Python script that contains the Flask web application.
models/: Directory containing trained machine learning models.
templates/: Directory containing HTML templates for the web application.
utils.py: Utility functions for data preprocessing and model inference.
.gitignore: Git ignore file to specify files and directories to be ignored by Git.
LICENSE: MIT License file for the project.

Usage
Once you have installed the dependencies and set up the project, you can run the web application locally:
```
python app.py
```

Visit http://localhost:5000 in your web browser to access the application.

