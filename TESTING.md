# Testing

## Manual Testing

| Feature | Action | Expected Result | Tested | Passed | Comments |
| --- | --- | --- | --- | --- | --- |
| Next Button | Click next button | Change image | Yes | Yes | --- |
| Logout/Login | Click on login/logout | User should logout or should get sent to login page | Yes | Yes | Changes whether user is authenticated or not |
| Link to info page | Click a link | Move to info page | Yes | Yes | --- |
| Link to starters page | Click a link | Move to starters page | Yes | Yes | --- |
| Link to mains page | Click a link | Move to mains page | Yes | Yes | --- |
| Link to desserts page | Click a link | Move to desserts page | Yes | Yes | --- |
| Link to drinks page | Click a link | Move to drinks page | Yes | Yes | --- |
| Link to booking page | Click a link | Move to booking page | Yes | Yes | --- |
| Link to sign up page | Click a link | Move to login page | Yes | Yes | --- |
| Link to register page | Click a link | Move to register page | Yes | Yes | --- |
| Make booking form | create reservation | Make a booking which relays to admin | Yes | Yes | --- |
| Delete booking | delete booking | remove a booking that previously been made | Yes | Yes | --- |
| View booking | view reservations | Once booked a reservation user is able to view it | Yes | Yes | --- |
| Register | Fill in a register form | Fill a form and create a user in the website | Yes | Yes | --- |
| Register check | Automatically checks from | If fields arent correct it will not accept the form | Yes | Yes | --- |
| Login | Fill in log in | Fill in log in form with info which user registered with | Yes | Yes | --- |
| Table amount | An amount of table available | If theres too many people booked for a specific time the system will not allow it. | Yes | Yes | --- |
| Instagram icon in the footer | Click on the Instagram icon | The user is redirected to the Instagram page | Yes | Yes | It should open the link in another tab or page |
| Facebook icon in the footer | Click on the Facebook icon | The user is redirected to the Facebook page | Yes | Yes | It should open the link in another tab or page |
| Twitter icon in the footer | Click on the Twitter icon | The user is redirected to the Twitter page | Yes | Yes | It should open the link in another tab or page |
| YouTube icon in the footer | Click on the YouTube icon | The user is redirected to the YouTube page | Yes | Yes | It should open the link in another tab or page |
| Edit Function | Edits reservation | Succesfully change the reservation | Yes | Yes | --- |
| Create Review | Create a text review | A review should be submitted | Yes | Yes | --- |
| Edit Review | Review should be edited | Review is edited | Yes | Yes | --- |
| Delete Review | Review should be deleted | Review is deleted | Yes | Yes | --- |
| Staff Link | Directed to admin page | The admin page should appear only for staff | Yes | Yes | --- |
| --- | --- | --- | --- | --- | --- |
## Validation

### Home Page

![](documentation/index-val.png)

### Information Page

![](documentation/info-val.png)

### Starters Menu

![](documentation/menu-starters-val.png)

### Main Menus

![](documentation/menu-main-val.png)

### Dessert Menu

![](documentation/menu-desserts-val.png)

### Drinks Menu

![](documentation/menu-drink-val.png)

### Booking

![](documentation/booking-val.png)

### Make Booking

![](documentation/make-booking-val.png)

### View Booking

![](documentation/view-booking-val.png)

## CSS

![](documentation/oak-css-val.png)

## Javascript
![Js](documentation)
## Python

### Booking

#### Admin
![](documentation/admin-val.png)
#### Apps
![](documentation/val-app.png)
#### Constants
![](documentation/constants-validation.png)
#### Forms
![](documentation/forms-val.png)
#### Models
![](documentation/val-models.png)
#### Urls
![](documentation/val-urls.png)
#### Views
![](documentation/val-views.png)
### Restaurant

#### Urls
![](documentation/val-urls-two.png)
#### Asgi
![](documentation/val-asgi.png)
#### Wsgi
![](documentation/val-wsgi.png)
## Responsiveness

![Responsiveness](documentation/responsive-one.png)

![Responsiveness](documentation/responsive-two.png)

## Lighthouse

![Booking](documentation/lighthouse-booking.png)

![Delete Review](documentation/lighthouse-delete.png)

![Desserts](documentation/lighthouse-desserts.png)

![Drinks](documentation/lighthouse-drinks.png)

![Edit Review](documentation/lighthouse-edit.png)

![Home](documentation/lighthouse-index.png)

![Information](documentation/lighthouse-info.png)

![Main Meals](documentation/lighthouse-mains.png)

## Compatibility

These images show that the website is compatible with numerous web engines.

![Chrome](documentation/chrome.png)

![Edge](documentation/microsoft-edge.png)

![OperaGx](documentation/operagx.png)

## User Stories

| User Story | Requirement met | Image |
| --- | --- | --- |
| Customer Reservation| The user is easilty able to make a reservation for the restaurant | ![Reservation](documentation/max-reservations.png) |
| Availability Of Tables | If there is too many bookings and not enough tables the user should be told so | ![MaxReservations](documentation/max-reservations.png) |
| View Details Of Reservation | The user should be able to view their bookings and see the details of their reservation|
| Device Compatibility | The website should be able to be used on difference devices| ![Responsiveness](documentation/responsive-one.png) | 
| View Menu | The user should be able to see the different menus with ease|  |
| Delete Reservation | The user should be able to delete the reservation with ease | ![Delete](documentation/view-booking.png) |
| Logout | The user should be able to logout easily| ![Logout](documentation/logout.png) |
| Login | The user should be able to login with ease| ![Login](documentation/login.png) |
| No Backdated Bookings| When the user is entering the form an validation error should appear saying that they can't book a date before the present day | ![Backdate](documentation/backdate-img.png) |
|||