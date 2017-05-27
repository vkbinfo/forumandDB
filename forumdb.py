# "Database code" for the DB Forum
import psycopg2
import datetime
import bleach

POSTS = [("This is the first post.", datetime.datetime.now())]


def get_posts():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect("dbname=forum")
    cursor=db.cursor()
    cursor.execute("select time,content from posts order by time")
    data=cursor.fetchall()
    POSTS=list((str(x[1]), bleach.clean( str(x[0])) ) for x in data)
    db.close()
    return reversed(POSTS)


def add_post(content):
    """Add a post to the 'database' with the current timestamp."""
    content=bleach.clean(content)
    db = psycopg2.connect("dbname=forum")
    cursor = db.cursor()
    cursor.execute("INSERT into posts VALUES(%s)",(content,))
    db.commit()
    db.close()




