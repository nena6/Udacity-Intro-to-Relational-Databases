# Database code for the DB Forum.
# 
# This is NOT the full solution!

import psycopg2

DBNAME = "forum"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select content, time from posts order by time desc")
  posts = c.fetchall()
  db.close()
  return posts

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("insert into posts values ('%s')" % content) # Almost but not quite. !PREVENT SQL injection attack - https://blog.sqreen.io/preventing-sql-injections-in-python/. Try post: "'); delete from posts; --"
  # Warning Never, never, NEVER use Python string concatenation (+) or string parameters interpolation (%) to pass variables to a SQL query string. Not even at gunpoint.
  # http: // bobby - tables.com / python
  db.commit()
  db.close()

