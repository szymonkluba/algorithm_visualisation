# Algorithm Visualization
#### Video Demo:  https://youtu.be/Zy01FifhavY
#### Description:
This is my CS50x Final Project, Algorithm Visualization. This is Flask app for visualizing sorting algorithms.
Build with Python and JavaScript, with some HTML and CSS. Also, some Bootstrap components were used.

app.py contains app and socketio initialization and also path for index, and some socket messages handlers.

settings.py contains dictionary of implemented sorting algorithms.

helpers.py contains helper functions such as generating random array.

algorithm.py contains base Algorithm class with methods common to every algorithm to be implemented.

algorithms.py contains classes implementing sorting algorithms (extending Algorithm class) containing algorithm method, and some helper methods if needed. Logic of algorithms is writen in such way they can be animated, so they may not resemble original algorithms in some cases.

display_update.py contain UpdateDisplay class. Its job is to send updates via socket everytime change in array is made.

index.html contains all HTML code. As it is one view app, no separate layout has been implemented.

styles.css contains styling extending styling done with Bootstrap components.

script.js contains all JavaScript code. It initializes socket on the browser side and implements some events generating and updating array display.