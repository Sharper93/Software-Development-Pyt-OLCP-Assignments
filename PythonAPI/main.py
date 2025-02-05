from flask import Flask, jsonify, request
# import necessary modules from flask and sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# setting Flask App
app = Flask(__name__)


# configure database for flask using sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///data.db'
db = SQLAlchemy(app)

# class creation with book objexts
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(80), unique=True, nullable=False)
    book_author = db.Column(db.String(50))
    book_publisher = db.Column(db.String(80))
    
    def __repr__(self): #representation with self for objects
        #string for printing the ID, title, author, and publisher of the book
        return f"{self.id} - {self.book_title} - {self.book_author} - {self.book_publisher}"

@app.route('/')
def index():
    # return welcome message when accessing the root URL http://127.0.0.1:5000
    return 'Welcome to the Flask API for BOOKS!'

@app.route('/books',)
def get_book() -> str:
    
    """
        Get: all books in database  http://127.0.0.1:5000/books
    
        Returns:  dictionary of all books in the database
            
    """
    
    # get all books from the database and return them
    books = Book.query.all()
    
    # convert each book into a dictionary for output and append to output list
    output = []
    
    for book in books:
        book_data = {
            'id': book.id, 
            'title': book.book_title, 
            'author': book.book_author, 
            'publisher': book.book_publisher
            }
        
        output.append(book_data)
        
    return {"books" : output}


@app.route('/books/<id>')
def get_singular_book(id) -> dict:
    # get book by id using get method to return 404 if book not found
    book = Book.query.get_or_404(id)
    
    # id for book one is 11111111
    # id for book two is 222222
    # id for book three is 333333
    # id for book four is 444444
    
    # added jsonify per video -- not necessary if working with a dictionary however
    return jsonify({'is': book.id, 'Title': book.book_title, 'Author': book.book_author, 'Publisher': book.book_publisher})


@app.route('/books', methods=['POST'])
def add_book() -> str:
    
    """
        POST: add a new book to database http://127.0.0.1:5000/books/
    
        Returns:  confirmation message and ID of the added book
            
    """
    
    # get book details from the request body
    book = Book()
    book.id = request.json['id']
    book.book_title = request.json['book_title']
    book.book_author = request.json['book_author']
    book.book_publisher = request.json['book_publisher']
    # add book and commit changes
    db.session.add(book)
    db.session.commit()
    # confirmation statement 
    return {'message': 'Added Successfully: ', 'id': book.id}
    

    
@app.route('/books/<id>', methods=['PUT'])

def update_book(id: int) -> str:
    """
        PUT: update book details with ID at end -->  http://127.0.0.1:5000/books/
    
        Returns:  confirmation message
            
    """
    
    # get book by id using get_or_404 method to return 404 if book not found
    book = Book.query.get(id)
    # update book details
    book.book_title = request.json['book_title']
    book.book_author = request.json['book_author']
    book.book_publisher = request.json['book_publisher']
    
    # send and commit request
    db.session.commit()
    
    # confirmation statement
    return {
            "message": "Book: updated successfully",
                "updated_fields": {
                    "book_title": book.book_title,
                    "book_author": book.book_author,
                    "book_publisher": book.book_publisher
    }
}


# delete book from database  
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id: int) -> str:
    """
        DELETE: delete a book from database with ID at end -->  http://127.0.0.1:5000/books/
    
        Returns:  confirmation message
            
    """
    
    # get book by id using get_or_404 method to return 404 if book not found
    book = Book.query.get(id)
    # if statement for if book id is not found
    if book is None: 
        return {'error': 'Book not found'}
    # send and commit request
    db.session.delete(book)
    db.session.commit()
    # confirmation statement
    return f'Book: {id} deleted successfully'
    




if __name__ == "__main__":
    app.run(debug=True)
    

