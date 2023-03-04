# python3 manage.py loaddata fixtures/users.json
# python3 manage.py dumpdata users --indent 4 > fixtures/users.json
import os

os.system("python3 manage.py loaddata fixtures/users.json")
