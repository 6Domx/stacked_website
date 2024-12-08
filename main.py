from flask import Flask, render_template, request, redirect, url_for
from Linked_list import LinkedList

app = Flask(__name__)

linked_list = LinkedList()  

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route("/works")
def works():
    return render_template("works.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route('/linked_list', methods=['GET'])  
def show_linked_list():  
    return render_template('linked_list.html', linked_list=linked_list.print_list())

@app.route('/update', methods=['POST'])
def update():
    operation = request.form['operation']
    data = request.form.get('data', None)

    if operation == "insert_beginning" and data:
        linked_list.insert_at_beginning(data)
    elif operation == "insert_end" and data:
        linked_list.insert_at_end(data)
    elif operation == "remove_beginning":
        linked_list.remove_beginning()
    elif operation == "remove_end":
        linked_list.remove_end()
    elif operation == "remove_at" and data:
        linked_list.remove_at(data)

    return redirect(url_for('show_linked_list'))  

if __name__ == "__main__":
    app.run(debug=True)
