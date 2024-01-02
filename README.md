# Python-Art-Generator
Written in python is an image generator based on sub-folders of layers within an image to create many different images.

Prerequisits:
Install Python
Install PyCharm
Install git

(Make sure you install the correct install for the appropriate OS: Mac, Windows, or Linux)

Downloading the project:
Step 1:
Go to command prompt or terminal and type:
git clone https://github.com/rcturner7/Python-Art-Generator.git

Step 2:
Go to PyCharm under File and click on Open and find this repository and select.

Step 3:
Once in the repository inside PyCharm go to Python Packages at the bottom of the window where it says Python Packages, select it.
You will then go to the search bar inside the Python Packages bar and search for each library the project uses and install the dependencies:
os
itertools
hashlib
Pillow

or

go to command prompt or terminal and cd to the repository:
pip install os
pip install itertools
pip install hashlib
pip install pillow

Step 4:.
In the repository I attached the folder layout of images with sample layer images for practice.
(You can change the name of the subfolders and use your own images for each layer without changing code, however, if you do change the names of the subfolders in line 18 in main.py under the def main function the categories dict "categories = ["name of subfolder", "name of subfolder", "etc.."] make sure to change the names of the subfolders within the main.py)

Now you can run the script and the script will generate a Build folder with all potential images generated of all possibilities without duplicates.
Each image file will be titled on it's hash so the script can determine that no duplicates are created.

Stay tuned for updates and add-ons to this project. Feel free to add comments or requests or issues.
For anyone who downloads the repository, I hope you enjoy.
