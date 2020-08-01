# Parasite
## Description
Artwork Web-Scraper &amp; Uploader for Comission. 
## Introduction
This project intends to automate the process of scraping/downloading popular artworks from DeviantArt, or more broadly, any profitable product and re-uploading for our own commission. 
## Ethical Issues
The current implementation has some ethical issues- reselling copyrighted images is problematic to say the least. Work arounds include:
 - Automating some way of manipulating the image to ensure "Fair Use" under copyright (if this is possible)
 - Only reselling images that are on the "Public Domain" (if this is possible)
 - Restructuring the implementation to some other medium which is ethically profitable.

## Guide
 - Create a virtual environment using `virtualenv venv`.
 - Activate the environment using `./venv/bin/activate`.
 - Install requirements using `pip3 install -r requirements.txt`.

## Todo
 - [x] Setup virtualenv to avoid Lyndon's suffering.
 - [x] Learn basic Selenium concepts using Wikipedia project.
 - [ ] Setup Selenium in WSL using https://github.com/Microsoft/WSL/issues/648#issuecomment-324562271.
 - [ ] Setup Selenium browser to download a single image.
 - [ ] Automate the continuous scraping of popular images.
 - [ ] Automate the upload of a single RedBubble product.
 - [ ] Automate the continuous upload of scraped images.
 - [ ] Automate the process of creating new RedBubble accounts.

## Ideas
 - Could be re-structured to re-uploading OnlyFans content.

 ## Helpful Links
  - https://levelup.gitconnected.com/web-scraping-with-selenium-in-python-8fde2f0fd559
  - https://towardsdatascience.com/web-scraping-using-selenium-836de8677ae5