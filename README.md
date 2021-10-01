ZipAPI
======

The API is written using Python3 (Django Framework). You need to install Python 3.x and Django Framework.

You can install Django by using the command,

Python3 -m pip install -r requirement.txt

Interaction
-----

I have included everything in this repo. Clone it and follow the steps below,

1. In root folder of zipAPI (where you can see manage.py). Enter the command 'python3 manage.py runserver'
2. Once the server starts running without any issue at http://127.0.0.1:8000
3. (Interaction) In you use local CLI (Windows powershell on windows or Terminal on macOS) enter the following commands as you wish,

Command: curl http://127.0.0.1:8000/insert/33613 Function: 'Inserts the zip code 33613' <br/>
Command: curl http://127.0.0.1:8000/delete/33613 Function: 'Deletes the zip code 33613' <br/>
Command: curl http://127.0.0.1:8000/display Function: 'Displays all the zip codes inserted till now' <br/>
Command: curl http://127.0.0.1:8000/has/33613 Function: 'Checks if 33613 exists in the zip code'<br/>

Tests
-----

I included the tests screenshots under TestScreenshots folder. Check those to see wheather everything is running as it should. If any kind of error occurs please reach out to pantamrohit@gmail.com. I will help you out to fix the error. 

Note
-----

**I did my best to take care of the edge cases**
