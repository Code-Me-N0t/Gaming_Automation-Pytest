from src.modules import *
from src.main import *

host = env('host')

def get_token(index=1):
    header = {
        env('op_name'): env('op_value'),
        env('t_name'): env('t_value'),
    }

    response = requests.get(f'{host}token', headers=header)
    token = response.json()['data']['token']
    header[env('token')] = token

    key_params = {'username': data['username'],'betlimit': str(index)}
    response = requests.get(host+env('game_key'), headers=header, json=key_params)
    game_key = response.json()['data']['key']

    query_params = {'key': game_key}
    response = requests.get(host+env('site_url'), headers=header, params=query_params)
    game_url = response.json()['data']['url']
    return game_url