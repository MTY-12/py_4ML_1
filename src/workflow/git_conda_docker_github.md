# Project Setup with Docker, Conda, Git, and GitHub

## Setup Version Control

### Step 1: Create a New Project Folder in VS Code

1. **Open VS Code.**
2. **Create a new folder for your project.**

    **Reason:** Starting by creating a new project folder ensures that all your project files are organized in one place. This makes it easier to manage and maintain your project.

### Step 2: Initialize a Git Repository

1. **Open the terminal in VS Code (`Ctrl + `).**
2. **Navigate to your project folder and initialize a Git repository.**

    ```bash
    cd /path/to/your/project
    git init
    ```

    **Reason:** Initializing a Git repository early in the process allows you to track changes to your files from the beginning. This helps in maintaining version control and facilitates collaboration with others.

    **Why Before Next Step:** Setting up version control first ensures that all subsequent changes are tracked, which is crucial for maintaining a history of changes and collaborating effectively.

## Setup Environment Management

### Step 3: Create a Conda Environment

1. **Open the terminal in VS Code.**
2. **Create a new Conda environment.**

    ```bash
    conda create --name myenv python=3.10

    ```

3. **Activate the Conda environment.**

    ```bash
    conda activate myenv
    ```

   **if the env not activated.**
     conda env list
    conda init
    conda --version
    conda update conda

    **Reason:** Creating and activating a Conda environment early ensures that you are working in a clean and isolated environment. This prevents conflicts with other Python packages and dependencies on your system.

    **Why Before Next Step:** Ensuring an isolated environment prevents potential conflicts and issues when setting up the project structure and dependencies.

### Step 4: Create Project Structure

1. **Create the necessary files and folders for your project.**

    ```bash
    mkdir -p src
    touch Dockerfile environment.yml src/app.py .dockerignore
    ```

    **Reason:** Creating the project structure early helps you organize your files logically. This makes it easier to manage the project as it grows and ensures you have all necessary placeholders for subsequent steps.

    **Why Before Next Step:** Having the project structure in place provides a clear organization for setting up dependencies and creating the application code.

### Step 5: Create an `environment.yml`

1. **In your project folder, create a file named `environment.yml`.**

    ```yaml
    name: myenv
    channels:
      - defaults
    dependencies:
      - python=3.8
      - numpy
      - pandas
      - flask
      - pip
      - pip:
          - requests
    ```

    **Reason:** Defining the `environment.yml` file allows you to specify all dependencies for your project in one place. This ensures consistency across different environments and simplifies the process of setting up the environment in the Docker container.

    **Why Before Next Step:** Having dependencies defined ensures that the environment setup is reproducible, which is crucial for consistent development and deployment.

### Step 6: Create a Simple Python Application

1. **In your `src` folder, create a file named `app.py`.**

    ```python
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    if __name__ == '__main__':
        app.run(host='0.0.0.0')
    ```

    **Reason:** Creating a simple Python application early allows you to have a working base that you can build upon. This also provides a simple way to verify that your environment setup and dependencies are working correctly.

    **Why Before Next Step:** Having a basic application ensures that there is a working project to containerize and test with Docker.

## Setup Containerization

### Step 7: Create a Dockerfile

1. **In your project folder, create a file named `Dockerfile`.**

    ```Dockerfile
    # Use an official Python runtime as a parent image
    FROM continuumio/miniconda3

    # Set the working directory in the container
    WORKDIR /usr/src/app

    # Copy the current directory contents into the container at /usr/src/app
    COPY . .

    # Install any needed packages specified in environment.yml
    RUN conda env create -f environment.yml

    # Make RUN commands use the new environment
    SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

    # Ensure the conda environment is activated when the container starts
    ENV PATH /opt/conda/envs/myenv/bin:$PATH

    # Run app.py when the container launches
    CMD ["python", "src/app.py"]
    ```

    **Reason:** Creating the Dockerfile early allows you to define the environment and dependencies that your application needs. This ensures that the application can run consistently across different machines and environments.

    **Why Before Next Step:** Defining the Dockerfile first ensures that you have a blueprint for the container that can be built and tested.

### Step 8: Create a `.dockerignore` File

1. **In your project folder, create a file named `.dockerignore`.**

    ```dockerignore
    __pycache__
    *.pyc
    *.pyo
    *.pyd
    .Python
    env
    build
    dist
    *.tgz
    *.egg-info
    ```

    **Reason:** The `.dockerignore` file helps you avoid including unnecessary files in your Docker image, making the image smaller and the build process faster.

    **Why Before Next Step:** Ensuring unnecessary files are ignored makes the Docker build process more efficient and helps keep the image clean and lightweight.

## Track Project with Version Control

### Step 9: Track Your Project with Git

1. **Add your files to the Git repository.**

    ```bash
    git add .
    ```

2. **Commit your changes.**

    ```bash
    git commit -m "Initial commit"
    ```

    **Reason:** Committing your files to the Git repository ensures that you have a snapshot of your project at this point. This is crucial for tracking changes and facilitating collaboration.

    **Why Before Next Step:** Committing changes before pushing ensures that all local changes are recorded and can be reviewed before being shared with others.

### Step 10: Push Your Project to GitHub

1. **Create a new repository on GitHub.**
2. **Add the remote repository URL to your local Git repository.**

    ```bash
    git remote add origin https://github.com/yourusername/yourrepository.git
    ```

3. **Check the current branch.**

    ```bash
    git branch
    ```

4. **Create and switch to the `main` branch if it doesn't already exist.**

    ```bash
    git checkout -b main
    ```

5. **Stage your changes.**

    ```bash
    git add .
    ```

6. **Commit your changes.**

    ```bash
    git commit -m "Initial commit"
    ```

7. **Push the `main` branch to the remote repository.**

    ```bash
    git push -u origin main
    ```

    **Reason:** Pushing your project to GitHub before building and running the Docker container allows you to:
    - Ensure your code is backed up and safe.
    - Facilitate collaboration and review by team members.
    - Maintain a clear change history.
    - Utilize CI/CD pipelines for automated testing and deployment.
    - Confirm that the code is in a deployable state before proceeding to build and deployment.

    **Why Before Next Step:** Ensuring the code is backed up and in a shareable state before deployment provides a safety net and facilitates collaboration.

    8. **Fetch and merge changes from the remote repository.**

    ```bash
    git fetch origin
    git pull origin main
    ```

    **Reason:** Fetching and merging changes ensures that your local repository is up-to-date with the remote repository. This prevents conflicts and ensures that your local changes are compatible with the remote repository.

    **Why Before Next Step:** Ensuring the local repository is up-to-date prevents conflicts when pushing changes to the remote repository.

8. **Push the `main` branch to the remote repository.**

## Deployment

### Step 11: Build and Run the Docker Container

1. **Navigate to the project directory.**

    ```bash
    cd /path/to/your/project
    ```

2. **Build the Docker image.**

    ```bash
    docker build -t my-python-app .
    ```

3. **Run the Docker container.**

    ```bash
    docker run -p 5000:5000 my-python-app
    ```

    **Reason:** Building and running the Docker container allows you to test your application in an isolated environment. This ensures that the application works as expected and is ready for deployment.

    **Why Before Next Step:** This step should be done last to verify that everything is set up correctly and the application is ready for deployment.

## Troubleshooting Docker Issues

### Restart Docker Daemon

```bash
Restart-Service docker
