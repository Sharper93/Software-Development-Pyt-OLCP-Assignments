from flask import Flask
# setting Flask App
app = Flask(__name__)

# import necessary modules from flask and sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# configure database for flask using sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///data.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(80), unique=True, nullable=False)
    book_author = db.Column(db.String(50))
    book_publisher = db.Column(db.String(80))
    
    def __repr__(self): #representation with self for objects
        #string for printing the name and description
        return f"{self.id} - {self.book_title} - {self.book_author} - {self.book_publisher}"


@app.route('/books')

def get_books() -> str:
    
    """
    Get all books in database 
    
    Returns:
        str dictionary of all books in the database
    """
    
    books = Book.query.all()
    
    output = []
    for book in books:
        book_data = {
            'id': book.id,
            'book_title': book.book_title,
            'book_author': book.book_author,
            'book_publisher': book.book_publisher
        }
        output.append(book_data)
        
    return {'books': output}


@app.route('books', methods=['POST'])
def create_book() -> str:
    
    """
    Create a new book for database

    Returns:
        string : Addes sucessfully and book ID 
        
    """
    book = Book()
    book.id = request.json['book_id']
    book.book_title = request.json['book_title']
    book.book_author = request.json['book_author']
    book.book_publisher = request.json['book_publisher']
    
    db.session.add(book)
    db.session.commit()
    
    return {'message': 'Added Successfully: ', 'id': book.book_id}
    
    
# create link for local book from DB
# http://localhost:5000/books/1 
@app.route('/books/<id>', methods=['PUT'])
def update_book(id: int) -> str:
    pass #TODO: CREATE!!!
    

# create link for local book from DB
# http://localhost:5000/books/1   
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id: int) -> str:
    
    """
    Gets book ID and delete the book, if it exists
    
    Returns: Error if book id is not found
    Returns: Book ID and deleted successfully if book exists
    
    """
    
    book = Book.query.get(id)
    ret_val: dict = []
    
    book_id = id  # Assuming 'id' is the correct variable name for 'book_id'
    ret_val = {'error': f'Book: {book_id} not found'}
    db.session.delete(book)
    db.session.commit()
    ret_val['complete'] = f'Book: {book_id} deleted successfully'
    db.session.commit()
    ret_val['complete'] = f'Book: {book_id} deleted successfully'

if __name__ == "__main__":
    app.run(debug=True)
    
