#!/usr/bin/python
import requests
from requests.auth import HTTPBasicAuth
import json


def set_env(env):
    user = 'test'

    pwd = {
        'Devqa': "test",
        'Stage': "test",
        'Prod': "test"
    }
    urls = {
        'Devqa': 'https://url-dev',
        'Stage': 'https://url-stage',
        'Prod': 'https://url-prod'
    }

    x_apigw_api_id = {
        'Devqa': 'test',
        'Stage': 'test',
        'Prod': 'test'
    }

    x_dxc_inf_route_key = {
        'Devqa': 'testQA',
        'Stage': 'testNowQa',
        'Prod': 'test'
    }

    x_dxc_inf_user = {
        'Devqa': 'test',
        'Stage': 'test',
        'Prod': 'test'
    }

    global pwd_env, urls_env, x_apigw_api_id_env, x_dxc_inf_route_key_env, x_dxc_inf_user_env, resource, auth, headers

    pwd_env = pwd[env]
    urls_env = urls[env]
    x_apigw_api_id_env = x_apigw_api_id[env]
    x_dxc_inf_route_key_env = x_dxc_inf_route_key[env]
    x_dxc_inf_user_env = x_dxc_inf_user[env]

    ##### Values to be update

    resource = urls['Stage'] + '/incidents'

    auth = HTTPBasicAuth(user, pwd[env])

    headers = {
        'Accept': "application/json;charset=utf-8",
        'Content-Type': "application/json",
        'x-dxc-inf-route-key': x_dxc_inf_route_key_env,
        'x-dxc-inf-user': x_dxc_inf_user_env
    }

    return pwd_env, urls_env, x_apigw_api_id_env, x_dxc_inf_route_key_env, x_dxc_inf_user_env, resource, auth, headers


def make_json_create(data):

	dict_create = {}
    category = data["category"]
    subcategory = data["subcategory"]
    company = data["company"]
    description = data["description"]
    shortDescription = data["shortDescription"]

    return dict_create




def create_ticket_inc(**inc_data):
    """
	Description:
	Args:
	Return:
	
    """
    
    set_env(env)
  
    payload = make_json_create(dict)
    ## sending post request and saving response as response object
    #
    r = requests.post(url=resource, data=json.dumps(payload), headers=headers, auth=auth)
    #
    content = r.json()
    ##assert (r.status_code == 200)
    print("Response Status Code: " + str(r.status_code))
    print("Response JSON Content: " + str(content))
    #
    return content


def update_inc(**inc_ud):

    payload = (make_update_dict(dict_filter))
    r = requests.patch(url=resource + "/" + incident_number, data=json.dumps(payload), headers=headers, auth=auth)
    content = r.json()
    return content


def get_inc_number(**incident):  
    set_env(env)
    r = requests.get(url=resource + "/" + incident_number, headers=headers, auth=auth)
    content = r.json()

    return content





