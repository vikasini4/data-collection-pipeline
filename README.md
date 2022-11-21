# data-collection-pipeline

I have chosen a website where data will be scraped. Firs of all, we have to used Selenium in order to create a webscrap class. 
This class will contain all the methods used to scrape data from the website choosen.

Milestone 4:

I have retrieved the data which is to get a list of links of the images and get images stored in a folder.

Milestone 5:

In this part, I created unit tests for my scraper using unittest, for each of methods of my webscraper() class.

Milestone 6:

I had to create a Dockerfile build a scraper image locally. Once the image is built, the image worked perfectly after running it, and then was pushed to the DockerHub.

Milestone 7:

Two github secrets, DOCKER HUB USERNAME and DOCKER HUB ACCESS TOKEN, had to be created in order to complete this section. Each of them have a personal access token generated on DockerHub as well as my DockerHub user ID. 

I could then use GitHub actions to put up a CI/CD pipeline. A GitHub action was created to push to the main branch of your repository.
