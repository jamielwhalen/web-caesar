from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form action="/" method="post">
      <lable for="rot">Rotate by:</label>
      <input id="rot"name="rot" type="text" value="0"/><br>
      <textarea name= "text">{0}</textarea><br>
      <input type="submit" value="Submit Query"/>
      
    </body>
</html>"""
@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt1():
    rotate = request.form['rot']
    text = request.form['text']
    
    return form.format(encrypt(text, rotate))



app.run()