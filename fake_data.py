# first install library pip3 install faker
# then import faker
from faker import Faker
# then initialize Faker()
faker=Faker()
# keep generating data like name,address,job
# date of birth, city etc
name=faker.name()
address=faker.address()
dob=faker.date_of_birth()
city=faker.city()
job=faker.job()
# then print all thing which you were creating 
print("Name: \t\t",name)
print("Address: \t",address)
print("Date Of Birth:  ",dob)
print("Address: \t",city)
print("Job: \t\t",job)
