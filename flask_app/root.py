from . import app
@app.route("/")
def main():
    return "Welcome!"