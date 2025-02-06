import sqlalchemy as sa

# Create an engine that connects to the SQLite database
engine = sa.create_engine('sqlite:///books.db')

# Establish a connection to the database
with engine.connect() as conn:
    # Define the SQL query
    sql = sa.text('SELECT title FROM books ORDER BY title')
    
    # Execute the query
    rows = conn.execute(sql)
    
    # Iterate over the result and print each title
    for row in rows:
        print('title:', row[0])

# Dispose of the engine
engine.dispose()
