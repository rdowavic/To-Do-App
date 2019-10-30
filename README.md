Hi, so if you wanted to run this, you would need to set your environment variable FLASK_APP to be server.py. That's assuming you are going to run the flask command from within this directory.

You need to run

python3 -m flask run --host=0 --port=PORTNUMBER

And then you can visit

http://0.0.0.0:<PORTNUMBER>/

To see the entries that are in the Items table right now within the todo database.


By the way, how did we get to this point with the structure of this project? Is it randomly chosen??
This is what happened:

In order to run a flask server, you need to have a python file `X.py` that sets up at least one route and then calls the constructor for a Flask object to which you pass something to do with the name of the file.

like `app = Flask(__something__)`

Then what happened was you needed to set X.py to be the value of the FLASK_APP environment variable on your computer, so do

export FLASK_APP=X.py

But again this is assuming you are going to run the `python3 -m flask run ...` command from the same directory that `X.py` is in.

Once you do this, you can add an extra feature of getting stuff from a database:
You just need to import `sqlite3`, it is a python module
You need to have a .db file to connect to, so you can make one if you have sqlite3 on your computer if you go

sqlite3 myDb.db

where myDb.db can just be the path where you want the new .db file to be created. May as well put it with the rest of your project like I did. I typed the absolute path of my project folder.

Then the next thing is that for flask to be able to render a html template and not just a string, it necessitates you having a directory called templates that is a sibling of the python file which is the server. So you make that and you can put .html files in there, then you can refer to them directly by their name (not their relative path from the python file) when you call the render_template function, using that as the return value of one of your route functions.

(Sorry that was NOT a good sentence)

Then the next thing is that you can use some templating features of flask to allow you to do a for loop, oh by the way,

If you want to retrieve things from the database and then somehow see them on the html page, you need to make a connection and then execute a query and then use the cursor object to fetch all the rows that resulted from the query. Store this in a variable `rows`. Then the render_template function can take optional keyword arguments, so if you want to refer to the rows as 'rows' inside the .html, you should do
.. render_template('blah.html', rows=rows)

Ie you are assigning the key 'rows' which you refer to in your index.html, to the value 'rows' which is a list of tuples that you retrieved from the database connection you made to your .db file.

So now your index.html or whatever .html file you have there can know about this variable "rows" when you use the (apparently builtin) flask templating feature

If your html file is like
```
<h1> Hello World </h1>
{{ rows }}
```

Then it will just raw print that whole list of tuples, it looks awful but it is a start.

Then you can use this for loop feature of the flask templating thing, which follows the for-loop syntax of python, and you can unpack the tuples as usual within the for loop statement, like

{% for id, name, thing in rows: %}

{% endfor }}

Yeah so that's gunna help you render it. These are the basics





