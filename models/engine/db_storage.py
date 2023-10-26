#!/usr/bin/python3
"""Creating a new engine 'DBStorage'"""
import os
class DBStorage:
    """Represents a database storage engine"""
    --engine = None
    --session = None

    def __init__(self):
        """Initializing new instance in db"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                                        .format(os.environ.get('HBNB_MYSQL_USER'),
                                            os.environ.get('HBNB_MYSQL_PWD'),
                                            os.eniron.get('HBNB_MYSQL_HOST'),
                                            os.environ.get('HBNB_MYSQL_DB'))
                                        pool_pre_ping=True)
