## website

This is repo for folders: Basics, Dates and Filters, Files, Internet Data:

https://github.com/LinkedInLearning/learning-python-2896241

This is the repo for other stuff:

https://github.com/LinkedInLearning/hands-on-python-3084712

# Python virtual enviornment set up

Python 3 comes with a virtual enviornment module built-in called 'venv'. There's no need to download anything. Just jump in and create a vm

1- In terminal navigate to the project folder

2 - To create a virtual enviornment. In this example calling it 'pyautomation_venv' :

    python3 -m venv pyautomation_venv

3 - Activate the virtual enviornment by sourcing the activate script in its bin directory

    source pyautomation_venv/bin/activate

4 - To deactivate the virtual enviornment, just type 'deactivate':

    deactivate

5 - In .gitignore file, you may want to add the virtual enviornment folder as 'venv/' is not picking the folder up.

6 - To delete, just delete the virtual enviornment folder from the project directory
