from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin')

def admin_name():
    return "Hello Admin"

@app.route('/guest/<guest>')
def guest_name(guest):
    return "Hello %s" %guest

@app.route('/user/<user>')
def user_name(user):
    if user == 'admin':
        return (redirect(url_for('admin_name')))

    else:
        return (redirect(url_for('guest_name',guest=user)))


if __name__ == '__main__':
    app.run(debug=True)


# credits: www.tutorialspoint.com