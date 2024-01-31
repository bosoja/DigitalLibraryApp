from flask import Flask, render_template
app = Flask(__name__)

# Dummy data for the digital library
books = [
    {"title": "Book One", "author": "Author A"},
    {"title": "Book Two", "author": "Author B"},
    {"title": "Book Three", "author": "Author C"}
]

@app.route('/')
def library():
    return render_template('library.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
