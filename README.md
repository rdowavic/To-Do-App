Hi, so if you wanted to run this, you would need to set your environment variable FLASK_APP to be server.py. That's assuming you are going to run the flask command from within this directory.

You need to run

python3 -m flask run --host=0 --port=PORTNUMBER

And then you can visit

http://0.0.0.0:<PORTNUMBER>/

To see the entries that are in the Items table right now within the todo database.
