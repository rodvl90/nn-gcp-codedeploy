from dotenv import load_dotenv
load_dotenv()
from pprint import pprint
import os

test = os.getenv("TEST")
test2 = [{"name": "test", "value": "test"}, {"name": "test2", "value": "test2"}]
print(test)