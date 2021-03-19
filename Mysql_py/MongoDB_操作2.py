import pymongo

from pymongo import ASCENDING

coll = db.students

coll.create_index([('name',ASCENDING)] , unique = True)
