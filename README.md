# Algorithm Visualization
#### Video Demo:  https://youtu.be/Zy01FifhavY
#### Description:
This is my CS50x Final Project, Algorithm Visualization. This is Flask app for visualizing sorting algorithms.
Build with Python and JavaScript, with some HTML and CSS. Also, some Bootstrap components were used.

App uses runs sorting algorithms on backend and sends updates to be displayed on browser side via sockets using Flask-SocketIO. Socket messages are received and processed In JavaScript.

app.py contains app and socketio initialization and also path for index, and some socket messages handlers.

settings.py contains dictionary of implemented sorting algorithms. To extend app with new algorithms it is only needed to implement new class for algorithm (extending Algorithm base class) and include class name in this dictionary. App is updated from here, names are included in <select> tag and instance of class is created after algorithm is selected (information is sent back via socket).

helpers.py contains helper functions such as generating random array. Values in array are generated in range od 10 to 99 as they are also used as percentage height of bars (% of div height containing display of array as bars).

algorithm.py contains base Algorithm class with methods common to every algorithm to be implemented.

algorithms.py contains classes implementing sorting algorithms (extending Algorithm class) containing algorithm method, and some helper methods if needed. Logic of algorithms is writen in such way they can be animated, so they may not resemble original algorithms in some cases. To extend application with new algorithms it is required to implement new class here with method algorithm() containing logic of sorting, and include the new class in available_algorithms dict in settings.py

display_update.py contain UpdateDisplay class. Its job is to send updates via socket everytime change in array is made. Instance of class is initialized in Algorithm object.

index.html contains all HTML code. As it is one view app, no separate layout has been implemented. Styling is done mostly using Bootstrap components, with some addition of custom CSS for array display and customization of Bootstrap components.

styles.css contains styling extending styling done with Bootstrap components and custom styling for array display (ex. bars highlights), and also slight customization of Bootstrap components (mostly change of colors and highlights on hover).

script.js contains all JavaScript code. It initializes socket on the browser side and implements some events generating and updating array display. It also dynamically generates array display as set of divs with height dependent on percentage value from the array.

Array size is also dependent on window size, event listener is set to check if any resize of window happened and reducing of size of array is needed.

Flask and web sockets may not be the best tools for this particular application, but the idea was to check if it will even work:D Also I didn't found anybody trying to do this that way (maybe because it's a bad idea... but still).