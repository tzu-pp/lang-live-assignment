import requests
from requests.exceptions import RequestException, JSONDecodeError
from api_url import *


def request(streamer_type, url, params=None):
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()   # check status code, throw error while 4xx 5xx
        return response.json()

    except RequestException as e:
        print(f"ERROR: Request failed for {streamer_type}: {e}")
        return None
    except JSONDecodeError as e: 
        print(f"ERROR: Invalid JSON response for {streamer_type}: {e}")
        return None
    except Exception as e: 
        print(f"ERROR: Unexpected error for {streamer_type}: {e}")
        return None


def _parse_common(streamer_type, data, list_key, pfid_key, nickname_key):

    # assert arg format
    assert isinstance(list_key, str) and list_key, f"[Assertion] list_key must be non-empty string."
    assert isinstance(pfid_key, str) and pfid_key, f"[Assertion] pfid_key must be non-empty string."
    assert isinstance(nickname_key, str) and nickname_key, "[Assertion] nickname_key must be non-empty string."
    
    result = []

    assert isinstance(data, dict), f"[Assertion] Response data must be a dictionary"
    if data is None:
        return result

    items = data.get("data", {}).get(list_key, [])
    assert isinstance(items, list), f"[Assertion] Expected list for key '{list_key}'"

    for item in items:
        pfid = item.get(pfid_key)
        nickname = item.get(nickname_key)
        if pfid and nickname:
            result.append((streamer_type, pfid, nickname))
    return result




def parse_last_live():
    result = []
    
    for streamer_type, url in last_live_apis:
        data = request(streamer_type, url)

        # pfid: response.data.recommend[i].pfid, nickname: response.data.recommend[i].nickname
        result.extend(_parse_common(streamer_type, data, "recommend", "pfid", "nickname"))
    
    return result

def parse_hot():
    result = []
    
    for streamer_type, url in hot_live_list_apis:
        data = request(streamer_type, url)        
        result.extend(_parse_common(streamer_type, data, "list", "pfid", "nic"))
    
    return result

def parse_class_list():
    result = []
    
    for streamer_type, param in class_list_apis:
        full_params = {**class_list_common, **param}
        data = request(streamer_type, class_list_url, full_params)
        result.extend(_parse_common(streamer_type, data, "list", "pfid", "nic"))
    
    return result

def parse_rank_list():
    result = []
    
    for streamer_type, param in rank_apis:
        full_params = {**rank_common, **param}
        data = request(streamer_type, rank_url, full_params)
        result.extend(_parse_common(streamer_type, data, "list", "pfid", "nickname"))
    
    return result


