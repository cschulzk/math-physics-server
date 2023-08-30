# Math App
This app is the beginning of a longer-term project to build an app for calculating and displaying math and physics phenomenon. I'll build it out in my free time. Long term goals include temperature calculations in n-dimensional solids and the trajectory of electrons in a laser focus.

There are size limits put on the arguments that are accepted in order to make the computation times small for even small computers. These limits can be adjusted to match the infrastructure the app is running on.

# Running the server
If you're new to Flask, checkout the [official Flask tutorial](https://flask.palletsprojects.com/en/2.3.x/tutorial/). 

Set up a virtual environment in your project directory and then run `pip install Flask`. This is the only dependency required for the time. 
After installing the dependencies, you can run the server with `py flask_app.py`. This will automatically run Flask in debug mode.

The Flask website discusses a number of options for setting up a production server: https://flask.palletsprojects.com/en/2.3.x/deploying/. I've used PythonAnwhere for deploying a sample version of the app at: http://cschulzke.pythonanywhere.com/. Check it out!

# Guidelines for new functions
## Selecting branch
All functions should be listed under the route for their particular branch of mathematics or physics. For example, the functions for exponentiation live under the 'arithmetic' branch and have the route '/arithmetic/exponentiate'
## GET and POST route
Every function should have both a GET and POST route. The GET route should return instructions for how to use that route as well as any applicable precautions (let users know the limits on inputs). The POST route should accept any necessary parameters and then return the result of the calculation.
