#!/usr/bin/python

import json
import requests
from ansible.module_utils.basic import AnsibleModule

url = "https://api.github.com/user/repos"

def create_repo(data):
  api_key = data['api_key']
  headers = {"Authorization":"Token {}".format(api_key)}
  result = requests.post(url,json.dumps(data),headers=headers)
  meta = {"status":result.status_code,"response":result.json()}
  return True,False,meta


def del_repo(data=None):
  url1 = "https://api.github.com/repos" 
  print("nothing to do")
  api_key = data['api_key']
  headers = {"Authorization":"Token {}".format(api_key)}
  api_url = "{}/{}/{}" . format(url1,"Shweta217",data['name'])
  result = requests.delete(api_url,headers=headers)
  meta = {"status":result.status_code}
  return True,False,meta


def main():
  fields = {
    "api_key": {"required":True,"type":"str"},
	"name": {"required":True,"type":"str"},
	"private": {"default":False,"type":"bool"},
	"Description": {"required":False,"type":"str"},
	"state": {
	  "default":"absent",
	  "type":"str",
	  "choices": ['present','absent']
	}
  }  
  choice_map ={
    'present': create_repo,
	'absent': del_repo
  }
  obj = AnsibleModule(argument_spec = fields)
  has_changed,*result = choice_map.get(obj.params['state'])(obj.params)
  obj.exit_json(changed=has_changed,meta=result)

if __name__ == '__main__':
  main()  
