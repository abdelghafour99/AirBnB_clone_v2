#!/usr/bin/python3
"""
Update FileStorage: (models/engine/file_storage.py)
*** Add a public method def close(self)::
*** *** call reload() method for deserializing the JSON file to objects
"""


from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine



class DBStorage:
	"""Database storage class for interacting with MySQL using SQLAlchemy"""


	__engine = None
    	__session = None


	def __init__(self):
        	"""Initialize the DBStorage instance"""
        	self.__engine = create_engine("mysql+mysqldb://user:password@localhost/db_name")
        	Session = scoped_session(sessionmaker(bind=self.__engine))
        	self.__session = Session()


    	def reload(self):
        	"""Reloads all tables"""
        	pass

    
	def close(self):
        	"""
        	Close method to call remove() or close() on the session.
        	This will ensure that the session is properly closed 
		when the database connection is done.
        	"""
        	if self.__session:
            		self.__session.remove()  
			# Use this if you are using scoped sessions
            		# self.__session.close()
			# Uncomment this if using a standard session (not scoped)
