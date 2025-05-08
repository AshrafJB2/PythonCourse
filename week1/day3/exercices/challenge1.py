class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("cat1", 10)
cat2 = Cat("cat2", 12)
cat3 = Cat("cat3", 8)

def oldestcat(**kwargs):
    oldest = 0
    for key, value in kwargs.items():
        if value.age > oldest:
            oldest = value.age
            oldest_name = value.name
    return oldest_name, oldest

print(f"The oldest cat is {oldestcat(cat1=cat1, cat2=cat2, cat3=cat3)[0]} and is {oldestcat(cat1=cat1, cat2=cat2, cat3=cat3)[1]} years old.")