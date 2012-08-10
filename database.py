import sqlite3

class DBController:

	def __init__(self, filename):
		self.db = sqlite3.connect(filename)

	def initDB(self):
		self.db.execute("DROP TABLE IF EXISTS commits")
		self.db.execute("CREATE TABLE commits (id PRIMARY KEY, repo_name, latest_tag, latest_commit, latest_commit_dev)")
		self.db.commit()

	def putNew(self, repo_name, latest_tag, latest_commit, latest_commit_dev):
		self.db.execute("INSERT INTO commits VALUES (NULL, ?, ?, ?, ?)", (repo_name, latest_tag, latest_commit, latest_commit_dev))
		self.db.commit()

	def updateTag(self, repo_name, latest_tag):
		self.db.execute("UPDATE commits SET latest_tag = ? WHERE repo_name = ?", (latest_tag, repo_name))
		self.db.commit()

	def updateCommit(self, repo_name, latest_commit):
		self.db.execute("UPDATE commits SET latest_commit = ? WHERE repo_name = ?", (latest_commit, repo_name))
		self.db.commit()

	def updateDevCommit(self, repo_name, latest_commit_dev):
		self.db.execute("UPDATE commits SET latest_commit_dev = ? WHERE repo_name = ?", (latest_commit_dev, repo_name))
		self.db.commit()


	def getRepo(self, repo_name):
		cur = self.db.cursor()
		cur.execute("select * from commits where repo_name = ?", (repo_name,)).fetchone()
		return cur.fetchall()

	def getAllRepo(self):
		cur = self.db.cursor()
		cur.execute("select repo_name from commits")
		return cur.fetchall()

	def getAll(self):
		cur = self.db.cursor()
		cur.execute("select * from commits")
		return cur.fetchall()
