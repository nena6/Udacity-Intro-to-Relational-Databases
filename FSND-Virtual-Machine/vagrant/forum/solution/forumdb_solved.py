# Database code for the DB Forum, full solution!

import psycopg2, bleach

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
  # Past this
  # < script >
  # setTimeout(function()
  # {
  #   var
  # tt = document.getElementById('content');
  # tt.value = "<h2 style='color: #FF6699; font-family: Comic Sans MS'>Spam, spam, spam, spam,<br>Wonderful spam, glorious spam!</h2>";
  # tt.form.submit();
  # }, 2500);
  # < / script >

  # Script injection attack

  c.execute("insert into posts values (%s)", (bleach.clean(content),))  # good
  db.commit()
  db.close()

