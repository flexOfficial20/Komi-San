import pymongo
import os

MONGO_URL = os.environ.get('MONGO_URL', 'mongodb+srv://Mongo1:586637515hshhwfftqu@cluster0.tvy79ai.mongodb.net/?retryWrites=true&w=majority')

database = pymongo.MongoClient(MONGO_URL)['notes']['notes']
