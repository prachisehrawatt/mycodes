from contextlib import contextmanager
import time
@contextmanager

def prog_timer():

    print("connecting to the database !")
    host = "localhost"
    user = "admin"
    password = "password"

    start_time = time.time()

    try:
        print("connection established !")
        yield

    finally:
        print("connection disconnected from the database !")
        process_time = time.time() - start_time
        print(f"time taken to execute : {process_time} secs.")

#main()
with prog_timer("mydb.db" , host = "localhost" , user = "admin" , password = "password") as db:
    db.execute(" CREATE TABLE IF NOT EXISTS USERS ( id integer , name varchar)")
    db.execute(" INSERT INTO USERS (name) VALUES (?)" , ("prachi"))
    db.execute( " SELECT * FROM USERS " )
    print(db.fetchall())
    
