# pause-app
## README

### Name

Pause - The Study Break Timer App.

### Description

Our website application will allow students to divide up their study time into small timed sessions, selecting the duration of their study time, break time and total study duration. We have suggested starting with 25 minutes study and then when the timer runs out, a study break of 5 minutes begins. This repeats throughout the total study session and will help students manage time and stay focussed. During the study break timer, an activity of approximately 5 minutes will be suggested - this may be a Brain Gym type activity with a YouTube video link to follow or a wellbeing activity with instructions.

### Technologies Used

- Programming Language(s): Python, JavaScript.

- Backend Framework(s): Flask 

- Database: MySQL

- External API: Pixela - register for a general user account. Use the `POST` command to send the `USER_TOKEN` and `USERNAME` for each request. A new user graph is created using the `GET` command to get an empty graph and then the data is added from the timer duration and date using the `PUT` command, sending the data to Pixela. The result is a Pixela chart showing the study time in minutes for that date and the user progress with their studies.  

### Installation Guide

Run the `schema.sql` and `pixela_account.py` files located in the `setup_scripts` directory 
Copy the contents from `config.template.py` into a new python folder called `config.py` and update the database user and password to your own

You will need to install the following python packages:

- `pip install flask`

- `Pip install flask-login`

- `pip install mysql.connector`

- `pip install requests`

Once you have followed these steps, run the main program in `app.py` from your Python IDE. Click the link that appears in the terminal, or navigate on your browser to `http://localhost:{port}`

This will display the sign in screen or a link to sign up for the web app.

### How To Navigate the App

*Sign Up Page*

Enter your details here to register - username, email and password. Once you have successfully registered, it will display “new account created”, and will redirect you to the sign in page. Type in your account details and hit 'Sign in'.

*Sign In Page*

If you already have a registered account, sign in using your username and password and it will take you onto the home page.

*Home Page*

You will see a welcome dashboard. From here, click on any of the buttons to select a Pause app option. Here, you can navigate to your account, start a study session, choose study sounds, see your study progress tracker, find out how Pause works, or sign out and return to the sign in page by clicking on the home icon in the top right corner.

<img width="1272" alt="Screenshot 2022-11-01 at 14 14 56" src="https://user-images.githubusercontent.com/112558282/200183173-d3d1ca0b-6949-4a50-824b-c9cae5c6bd68.png">

*My Account*

Click on this icon to display your username and email address. 

*Start Study Session*

Click on this icon to display a selection bar for you to choose the duration of your study session in minutes; duration of your study break in minutes; and the total duration of expected study in hours. It also shows an image of the study timer with start buttons, a pause button and reset button. By clicking on the start button, your timer will start counting down and your study session has begun. The study timer can be paused or reset at any time during the session. Once the study timer has hit zero, the break timer will begin to count down and a suggested activity will appear for you to try. This might be a Youtube video link to watch or simple instructions to follow on screen. This break timer can be paused or reset at any time during the session. Once this timer hits zero, the study session will begin again.

<img width="1366" alt="Screenshot 2022-11-02 at 15 50 33" src="https://user-images.githubusercontent.com/112558282/200183153-a3c6d122-209a-4524-8038-5a7fdc4bc449.png">

*My Study Progress*

Click on this icon to see a tracked chart showing your total study time to date. 

*How Pause Works*

Click on this icon to read about how Pause can help with your studies.

*Choose Study Sounds*

(Under development)

*Sign Out*

Selecting sign out returns you to the dashboard and from here, sign out returns you to the log in screen.

### Authors and acknowledgment

Ivy Kalegi, Joanna Waller & Nifesimi Komolafe
