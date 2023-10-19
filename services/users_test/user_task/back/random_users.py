from user_task.schemas.users import User
import random
import string


def generate(n):
    user_list = []
    for i in range(n):
        user = User(
            sex=bool(random.getrandbits(1)),
            age=random.randint(0, 120),
            name=''.join(random.choices(string.ascii_letters, k=5)),
            surname=''.join(random.choices(string.ascii_letters, k=5)),
            father_name=''.join(random.choices(string.ascii_letters, k=5)),
            address=''.join(random.choices(string.ascii_letters, k=5)),
            e_mail=''.join(random.choices(string.ascii_letters, k=5)),
            login=''.join(random.choices(string.ascii_letters, k=5)),
        )
        user_list.append(user)
    return user_list
