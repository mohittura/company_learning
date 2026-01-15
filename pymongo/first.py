import pymongo

connectionString = "mongodb+srv://mohitturabit:mohitturabit123@cluster0.wo9hblh.mongodb.net/?appName=Cluster0"


client = pymongo.MongoClient(connectionString)
# Creating a database for a School
db = client['mount-carmel']
# creating a collection
collection = db.class1

def insert_document():
    student_info = {
        "name" : "Drake",
        "section": 2,
        "maths_marks": 35,
        "sst_marks": 79
    }

    student_id = collection.insert_one(student_info).inserted_id
    # print(f"Student with id {student_id} has been created")


def read():
    # 2 reading a document using find() function
    myStudents = collection.find({"section": 1, "name" : "Mohit"})
    # print(myStudents)
    for student in myStudents:
        print(student)
    # using findOne() function
    myStudent = collection.find_one({"section": 1})
    print(myStudent)


def update():
    # collection.update_one({"section" : 1}, {'$inc': {'section': 100}})
    collection.update_many({}, {'$inc': {'section': 100}})

def delete():
    # collection.delete_one({"section" : 101})
    collection.delete_many({"section" : 102})



# CRUD
# 1 Create
# insert_document()

# 2 Read
# read()

# 3 Update
# update()

# 4 delete
# delete()