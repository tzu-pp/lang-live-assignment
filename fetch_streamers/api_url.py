# parse_last_live
last_live_apis = [("last_live", "https://api.lang.live/langweb/v1/sns/last_live_list")]

#parse_hot
hot_live_list_apis = [("hot", "https://api.lang.live/langweb/v1/home/live_list?page=1&psize=15&type=hot")]

# parse_class_list
class_list_url = "https://api.lang.live/langweb/v1/home/class_list"
class_list_common = {"page": "1", "psize": "15"}
class_list_apis = [
    # 熱推主播
    ("hot_female", {"id":"1-2"}),
    ("hot_male", {"id":"1-1"}),

    # 本月新主播
    ("new_in", {"id": "2-76"}),

    # 團體主打星
    ("group_cheerleaders", {"id": "3-100005"}),
    ("group_akb48", {"id": "3-100002"}),

    # 尋找好聲音
    ("voice_album", {"id": "3-100010"}),
    ("voice_singer", {"id": "3-100009"}),
    ("voice_power", {"id": "4-1"}),
    ("voice_guitar", {"id": "4-2"}),
    ("voice_instrument", {"id": "4-5"}),

    # 表演藝術/藝人
    ("artist_model", {"id": "4-24"}),  
    ("artist_actor", {"id": "4-10"}),  
    ("artist_dancer", {"id": "4-4"}),
    ("artist_painter", {"id": "4-6"}),

    # 星座推薦 - 風象
    ("zodiac_aquarius", {"id": "5-100"}),
    ("zodiac_gemini", {"id": "5-101"}),
    ("zodiac_libra", {"id": "5-102"}),

    # 火象
    ("zodiac_aries", {"id": "5-103"}),
    ("zodiac_leo", {"id": "5-104"}),
    ("zodiac_sagittarius", {"id": "5-105"}),

    # 水象
    ("zodiac_pisces", {"id": "5-106"}),
    ("zodiac_cancer", {"id": "5-107"}),
    ("zodiac_scorpio", {"id": "5-108"}),

    # 土象
    ("zodiac_capricorn", {"id": "5-109"}),
    ("zodiac_taurus", {"id": "5-110"}),
    ("zodiac_virgo", {"id": "5-111"})
]

# parse_rank_list
rank_url = "https://api.lang.live/langweb/v1/rank/list"
rank_common = {"psize": "10"}
rank_apis = [
    ("rank_day_female", {"c_type": "1", "rank_type": "1", "sex": "2"}), 
    ("rank_month_female", {"c_type":"1", "rank_type":"3", "sex": "2"}),
    ("rank_month_male", {"c_type":"1", "rank_type":"3", "sex":"1"}),
    ("rank_day_female", {"c_type":"1", "rank_type":"1", "sex":"2"}),
    ("rank_day_male", {"c_type":"1", "rank_type":"1", "sex":"1"}),
    ("rank_week_duration", {"c_type":"2", "rank_type":"2", "sex":"0"})
]

