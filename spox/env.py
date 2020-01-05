import json


def read_env():
  with open('.env.json') as json_file:
      data = json.load(json_file)

      return data

