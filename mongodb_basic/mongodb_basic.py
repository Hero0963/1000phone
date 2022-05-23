# ref= http://rasca0027.logdown.com/posts/252512-python-mongodb-pymongo-teaching

from pymongo import MongoClient

uri = "mongodb://USERNAME:password@host?authSource=source"
client = MongoClient(uri)

db = client['news']
collect = db['papers']

for post in collect.find():
# do something

post1 = collect.find_one({'foo': 'bar'})
post2 = collect.find_one({'_id': id})

my_dog = post1['dog_name']

# create new post object


post3 = {"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"]}
# insert into collection

post_id = collect.insert_one(post3).inserted_id
print(post_id)  # if ObjectId('...') then successful!
