from flask import Flask, escape, request
app = Flask(__name__)
#
# Define the basic route / and its corresponding request handler
#
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
if __name__ == "__main__":
    app.run()
#
# Add a variable section to the url
#
#  http://127.0.0.1:5000/user/tom
#
# @app.route('/user/<username>')
# def hello(username):
#     name = request.args.get("name", username)
#     return f'Hello, {escape(name)}!'
# if __name__ == "__main__":
#     app.run()

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content
