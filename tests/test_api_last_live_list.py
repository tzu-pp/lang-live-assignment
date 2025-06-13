import pytest
import requests

class TestLastLiveListAPI:
    """Test cases for 'last_live_list' API endpoint in Lang live official site"""

    def setup_method(self):
        self.url = "https://api.lang.live/langweb/v1/sns/last_live_list"
        self.payload = {
            "page": 1,
            "psize": 20
        }
        self.response = requests.post(self.url, json=self.payload)
        self.data = self.response.json()
        self.recommend_list = self.data["data"]["recommend"]


    def teardown_method(self):
        pass

    
    def test_status_code(self):
        assert self.response.status_code == 200, f"Expected 200, got {self.response.status_code}"

    def test_response_is_dictionary(self):
        assert isinstance(self.data, dict)

    def test_recommend_is_list(self):
        assert isinstance(self.recommend_list, list)

    def test_recommend_length_less_or_equal_20(self):
        assert len(self.recommend_list) <= 20, f"Got {len(self.recommend_list)} items"

    def test_pfid_is_int(self):
        for item in self.recommend_list:
            assert isinstance(item.get("pfid"), int), f"pfid should be int:{item.get('pfid')}"

    def test_nickname_is_string(self):
        for item in self.recommend_list:
            assert isinstance(item.get("nickname"), str), f"nickname should be string:{item.get('nickname')}"
