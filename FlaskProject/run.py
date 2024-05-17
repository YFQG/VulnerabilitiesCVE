from application import app

# This block of code checks if the script is being run directly or imported as a module
if __name__ == "__main__":
    # If the script is being run directly, the Flask application is started in debug mode
    app.run(debug=True)
