import psycopg2

db = psycopg2.connect(database='forum')
c = db.cursor()
c.execute("select * from posts")
posts = c.fetchall()
print posts
db.close()