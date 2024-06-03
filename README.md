# The Oak

## User

### First Time User

- For a first time user should be able to navigate through the website with ease. This means that they should be able
to go to each page and find information that they are looking for.

- The sign in and register process should be smooth and easy to detect if an error occurs in the registering process.

- The user should know if they are signed in to the website.

### Returning User

- A returning user should be pleased with the way the website is arranged and the booking system should be efficient.

### Frequent User

- A frequent user should find it easy to login to a previous account that has been registered to this website.

## Purpose

- The purpose of this is to create a website for a restaurant that includes a way to book a reservation. 

## Wireframes

### Desktop Device
![](assets/documentation/oak-home.png)

![](assets/documentation/oak-info-desktop.png)

![Menu Starters](assets/documentation/oak-menu-starters.png)

![Menu Mains](assets/documentation/oak-menu-mains.png)

![Menu Desserts](assets/documentation/oak-menu-desserts.png)

![Menu Drinks](assets/documentation/oak-menu-drinks.png)

![](assets/documentation/oak-make-booking-desktop.png)

![](assets/documentation/oak-view-booking-desktop.png)

![](assets/documentation/oak-login-desktop.png)

![](assets/documentation/oak-register-desktop.png)

![](assets/documentation/oak-booking-desktop.png)

### Tablet Device
![](assets/documentation/oak-home-tablet.png)

![](assets/documentation/oak-info-tablet.png)

![](assets/documentation/oak-menu-starters-tablet.png)

![](assets/documentation/oak-menu-mains-tablet.png)

![](assets/documentation/oak-menu-desserts-tablet.png)

![](assets/documentation/oak-menu-drinks-tablet.png)

![](assets/documentation/oak-make-booking-tablet.png)

![](assets/documentation/oak-view-booking-tablet.png)

![](assets/documentation/oak-login-tablet.png)

![](assets/documentation/oak-register-tablet.png)

![](assets/documentation/oak-booking-tablet.png)

### Mobile Device
![](assets/documentation/oak-home-mobile.png)

![](assets/documentation/oak-info-mobile.png)

![](assets/documentation/oak-menu-starters-mobile.png)

![](assets/documentation/oak-menu-mains-mobile.png)

![](assets/documentation/oak-menu-desserts-mobile.png)

![](assets/documentation/oak-menu-drinks-mobile.png)

![](assets/documentation/oak-make-booking-mobile.png)

![](assets/documentation/oak-view-booking-mobile.png)

![](assets/documentation/oak-login-mobile.png)

![](assets/documentation/oak-register-mobile.png)

![](assets/documentation/oak-booking-mobile.png)

## Features

- A booking system is one of the main features. This allows the user to easily make a reservation at this restaurant
from an options of days and times. This form makes sure that there are tables available at the specific
time that the user has asked for. Once succesfully booked a reservation this information will be placed in an admin page
which can be seen by users with access.
![](assets/documentation/oak-reservation-form.png)

- The admin page is a part of the project which specific people can access. They can see all the bookings that have been
made and the time and date they have booked a table for. There are filters which I have placed through the admin.py page,
this can make the user of the admin page's task much easier since they can look through data will ease.

- In the website there is a way to register an account with the website. This will allow them to log in to the account which
is crucial in order to make bookings. The form for this will make sure that the password that the user has is secure enough
so that their account is safe.

- Along with a register system there also need a log in system which will allow the user to log in to the website with just
their username and password which makes it very simple. This will allow them to log in and make a booking, since it has been
made to only show the booking page for when people are logged in. This is to ensure that we know who is making each
reservation.
![](assets/documentation/oak-login.png
)
- Since there is a login and register there also needs to be a logout system which is very simple for the user. On each page
it will show you if you are logged in and an option to logout, all the user needs to do it press the link that is available.

## Technology Used

- Python was used to make the code.
- Django
- HTML
- CSS 
- Javascript
- Bootstrap
- ElephantSql was used in order to host the database and store the data we will recieve.
- Gitpod was used to write the code.
- Git Hub was where the repository and code is stored.

## Testing

- Please visit [TESTING.md](TESTING.md).

## Bugs

### Solved Bugs

- There was a bug that I encountered which occured when I submitted the booking form. This showed an integrity
error since there needed an userid, in order to fix this I made the form require a login which needed an username.
I made it so the username was in place for the userid, this then allowed me to fix the problem I was encountering.

### Unsolved Bugs

### Mistakes

- In git commit ff582d0 I made a slight mistake in the text I used to describe the changes. It is "CMake a meta 
class for register form" this shows the mistake I made as I didnt mean to add a C at the start of the world "Make".

- Also in the git commit "984f726" I also accidentally make a mistake in the text I made to describe the git commit.
"Add fiCreate booking function", the mistake it that there is "fi on the start of the word "create".

## Deployment

- This project is deployed in heroku.