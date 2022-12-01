# data-collection-pipeline

The prerequisites for this project are as follows: 

. To set up an environment.

. To decide which website you are going to collect data from.

. Finding each entry's particular page using a model.

. Retrieve data from details page.

. Documentation and testing.

. Containerising the scraper.

. Set up CI/CD pipeline for your Docker image.


The project was based using VS Code as a code editor, plus Git and GitHub for version control. The environment setup was done by creating a new environment, web-env, in conda. The scraper uses OOP principles and is developed in Python.

I had to create a Dockerfile and build a scraper image locally. Once the image is built, the image worked perfectly after running it, and then was pushed to the DockerHub.

Two github secrets, DOCKER HUB USERNAME and DOCKER HUB ACCESS TOKEN, had to be created in order to complete this section. Each of them have a personal access token generated on DockerHub as well as my DockerHub user ID. 

I could then use GitHub actions to put up a CI/CD pipeline. A GitHub action was created to push to the main branch of your repository.
