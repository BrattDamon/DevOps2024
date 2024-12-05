## Multi-Container Docker Application with CI/CD: Calculator App Project

#### Complete Project Instructions: [DevOps Foundations Course/Project](https://github.com/shiftkey-labs/DevOps-Foundations-Course/tree/master/Project)

#### Submission by - **Brett Jerrett**
### Project Overview

- **Brief project description:** What is the purpose of your application?

**An application that is a calculator with a frontend component and backend written in Python as a way to implement what we learned in DevOps.**


- **Which files are you implmenting? and why?:**

- **frontend/Dockerfile - the configuration for frontend container image**
- **backend/Dockerfile - the configuration for backend container image**
- **github-actions.yml - a page that defines my gitHub actions workflow for the CI/CD pipeline via Github instead of gitlab**
- **docker-compose.yaml - Configuration file from simplifying the deployment of this project's containerized frontend and backend services**


- _**Any other explanations for personal note taking.**_

<!-- Include explanation here -->
<!-- Include explanation here -->
<!-- Include explanation here -->
<!-- NOTE: It is not compulsory to include detailed explanations, writing succint concise points would also sufice. Make sure maintain readability and clarity. -->


### Docker Implementation

**Explain your Dockerfiles:**

- **Backend Dockerfile** (Python API):
    - Here please explain the `Dockerfile` created for the Python Backend API. 
    - This can be a simple explanation which serves as a reference guide, or revision to you when read back the readme in future. 

- **Base image: uses python:3.9-slim image for minimal Python runtime.**
- **Sets /app as teh working directory inside the container**
- **Copies the backend code into the /app directory.**
- **Installs required Python packages from requirements.txt using pip**
- **Opens port 5000 for the Flask application**
- **Starts the Flask app, accessible from any host, on container startup**

- **Frontend Dockerfile** (React App):
    - Similar to the above section, please explain the Dockerfile created for the React Frontend Web Application. 

- **Uses node:16-alpine for a small and efficient Node.js runtime.**
- **Sets /app as the working directory inside the container.**
- **Copies package.json and package-lock-json to install required npm packages**
- **Copies all frontend code into the /app directory**
- **Builds the React application using npm run build**
- **Opens port 3000 for accessing the application**
- **Starts the React development server**

**Use this section to document your choices and steps for building the Docker images.**


### Docker Compose YAML Configuration

**Break down your `docker-compose.yml` file:**

- **Services:** THe frontend react-based frontend application, and the backend flask-based application.
- **Networking:** - Both frontend and backend are part of the default bridge network, allowing them to directly communicate with each other. And rely on eachother via the shared network.
- **Volumes:** Mounts the local ./frontend directory to the /app directory inside the container for live code reloading, the backend did the same via the ./backend directory
- **Environment Variables:** Loads environment variables from the environment.env file.

**Use this section to explain how your services interact and are configured within `docker-compose.yml`.**

- **The frontend and backend services are designed to run together in a Dockerized environment. The frontend service serves the React application on port 3000, while the backend service provides API functionality on port 5000. Both services are connected via the default Docker network, allowing the frontend to make API calls to the backend without additional configuration. Volume mounts ensure live code changes on the host are reflected inside the containers for efficient development.**
<!-- NOTE: It is not compulsory to include detailed explanations, writing succint concise points would also sufice. Make sure maintain readability and clarity. -->


### CI/CD Pipeline (YAML Configuration)

**Explain your CI/CD pipeline:**

- What triggers the pipeline (e.g., push to main branch)? 
- **A push to the main branch, a pull request to the main branch, or a manual trigger using the workflow_dispatch event**
- What are the different stages (build, test, deploy)?
- **The Frontend stage, the backend stage and the docker stage**
- How are Docker images built and pushed to a registry (if applicable)?
**Built using the docker/build-push-action with the context set to ./Project/frontend. and ./Project/backend.**

**Use this section to document your automated build and deployment process.**

- **This pipeline automates the build, test, and image creation process for the frontend and backend applications. It ensures all code changes in the main branch are tested, built, and packaged as Docker images. These images are then uploaded to the GitHub Container Registry, ready for deployment.**
<!-- NOTE: It is not compulsory to include detailed explanations, writing succint concise points would also sufice. Make sure maintain readability and clarity. -->

### Assumptions

- List any assumptions you made while creating the Dockerfiles, `docker-compose.yml`, or CI/CD pipeline. 

- N/A


### Lessons Learned

- What challenges did you encounter while working with Docker and CI/CD?
- What did you learn about containerization and automation?

- **I experienced a lot of issues setting up my Docker Image, specifically with my frontend portion. There was a lot of trial and error with getting the correct NPM to install.**
- **I ended up spending the most time on this, as it was incredibly hard to troubleshoot with documentation online**
- **Through much pain and frustration, I understood the important of the CI/CD pipeline when it finally successfully ran - and how intuitive the errors could be with the setup**


### Future Improvements


**Use this section to brainstorm ways to enhance your project.**






<!-- BEST OF LUCK! -->
