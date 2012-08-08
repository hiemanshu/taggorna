import sqlite3

class DBController:

	def __init__(self, filename):
		self.db = sqlite3.connect(filename)

	def putNew(self, id, repo_name, path_to_repo, latest_tag, latest_commit, dev_branch, latest_commit_dev):
		self.db.execute("insert into commits values (?, ?, ?, ?, ?, ?, ?)", (id, repo_name, path_to_repo, latest_tag, latest_commit, dev_branch, latest_commit_dev))
		self.db.commit()

	def updateTag(self, repo_name, latest_tag):
		self.db.execute("update commits set latest_tag = ? where repo_name = ?", (latest_tag, repo_name))
		self.db.commit()

	def updateCommit(self, repo_name, latest_commit):
		self.db.execute("update commits set latest_commit = ? where repo_name = ?", (latest_commit, repo_name))
		self.db.commit()

	def updateDev(self, repo_name, dev_branch):
		self.db.execute("update commits set dev_branch = ? where repo_name = ?", (dev_branch, repo_name))
		self.db.commit()

	def updateDevCommit(self, repo_name, latest_commit_dev):
		self.db.execute("update commits set latest_commit_dev = ? where repo_name = ?", (dev_branch, repo_name))
		self.db.commit()

	def get(self, id):
		return self.db.execute("select * from commits where id = ?", (id,)).fetchone()

	def getRepo(self, id):
		return self.db.execute("select * from commits where repo_name = ?", (repo_name,)).fetchone()

	def getAllRepo(self):
		cur = self.db.cursor()
		cur.execute("select repo_name from commits")
		return cur.fetchall()

	def getAll(self):
		cur = self.db.cursor()
		cur.execute("select * from commits")
		return cur.fetchall()
