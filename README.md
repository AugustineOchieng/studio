# Prism Studio


## Built By [Augustine Ochieng](https://github.com/AugustineOchieng/personal-gallery)

## Description
This is an application that allows users to view images. Image details are stored in categories and tagged by Location. The admin is responsible for uploading, editing or deleting images.

## User Stories
These are the behaviours/features that the application implements for use by a user.

Users would like to:
* View all images submitted.
* Click on images to display more details.
* Search for images by category.
* Copy links to images to share with their friends

## Admin Abilities
These are the behaviours/features that the application implements for use by the admin.

Admin should:
* Sign in to the gallery
* Create new images for showcasing
* Delete images
* Update image post details.


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | On demand | Access Admin dashboard |
| Display all images | Home page | Clickable links to open any images in a modal |
| Display single images on click | On  click | All details should be viewed|
| To add an image  | Through Admin dashboard | Add and add categories and tag location of Image|
| To edit image  | Through Admin dashboard | Redirected to the  image form details and editing happens|
| To delete an image  | Through Admin dashboard  | click on image object and confirm by delete button|
| To search  | Enter text in search bar | Users can search by category|
| To filter by Location  | Click drop-down on navbar | Users can view images by Location|


## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv
* Requirements.txt

### Cloning
* In your terminal:

        $ git clone https://github.com/AugustineOchieng/personal-gallery
        $ cd personal-gallery

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ python3.6 manage.py runserver

## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py test images

## Technologies Used
* Python3.6
* Django and postgresql

## License
[MIT](https://choosealicense.com/licenses/mit/)

Copyright (c) 2018 AugustineOchieng