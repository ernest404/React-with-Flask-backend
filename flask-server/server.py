from flask import Flask

app = Flask(__name__)

# Members API Route
@app.route('/members')
def members():
    return {'members': ['Member1', 'Member2','Member3', 'Member4']}

if __name__ == '__main__': #is used to execute this code only if the file was run directly, and not imported in other files.
    app.run(debug = True, host="0.0.0.0")

# Reason: If the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value “__main__”. If this file is being imported from another module, __name__ will be set to the module’s name.