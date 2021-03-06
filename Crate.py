# Handle data storage of a given loot object. Maybe a database, maybe files, whatever we want.
import crates
class Crate:

	def __init__(self, crateType):
		#if crateType.lower() == "file":
		#	self._crate = crates.FileCrate()
		if crateType.lower() == "sql":
			self._crate = crates.SQLCrate()
		else:
			return -1
			
	def addUser(self, user):
		self._crate.addUser(user)
		return 0

	def addOrganization(self, org):
		self._crate.addOrganization(org)
		return 0

	def addRepository(self, repo):
		self._crate.addRepository(repo)
		return 0

	def addLoot(self, loot):
		self._crate.addLoot(loot)
		return 0

	def addJob(self,job):
		self._crate.addJob(job)
		return

	def finishJob(self,job):
		self._crate.finishJob(job)
		return