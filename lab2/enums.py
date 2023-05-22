import random
from uuid import uuid4
import fake

def get_uuid():
    return str(uuid4())

def get_random_carplate():
    chars = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЫЭЮЯ"
    nums = "0123456789"
    rand_letter1 = [random.choice(chars) for i in range(1)]
    rand_letter2 = [random.choice(chars) for i in range(2)]
    rand_num = [random.choice(nums) for i in range(3)]
    return "".join(rand_letter1 + rand_num + rand_letter2)

def get_random_name():
    fake = fake.Faker()
    while True:
        x = fake.name()
        yield x
# ! отвал жепы
generator = get_random_name()
print(list(generator))
