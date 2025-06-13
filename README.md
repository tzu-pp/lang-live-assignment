# lang-live-assignment

包含兩個功能：

1. Streamer Data Fetcher
2. QA Validation with pytest

### Project Structure

```
lang-live-assignment/
├── fetch_streamers/   # Streamer Data Fetcher
├── tests/             # QA Validation with pytest
├── Pipfile
├── Pipfile.lock
└── README.md
```

### Requirements

- Python 3.13
- Pipenv

### Setup

- 安裝 pipenv 與依賴套件：

```bash
pip install pipenv
pipenv install
```

## Streamer Data Fetcher

從 Lang Live 官網首頁爬取 pfid 介於 4000000–5000000 的主播資料

### Features

- 取得 Lang Live 官網首頁 API 資料
- 篩選 pfid 介於 4000000 ～ 5000000（含）之間的主播
- 輸出符合條件主播的 pfid 及主播暱稱

### Structure

```
fetch_streamers/
├── main.py                 # Main entry point
├── parser.py               # API parsing module
├── api_url.py              # API endpoint
├── filtered_streamers.csv  # Output results
└── __init__.py
```

### Usage

- 執行程式，會自動抓取資料並輸出到  `filtered_streamers.csv`

```bash
cd fetch_streamers
pipenv run python main.py
```

### Output

- 檔案格式：CSV
- 欄位：`pfid` 及 `Nickname`（主播暱稱）

## QA Validation with pytest

使用 pytest 框架驗證 last_live_list API

### Features

- 測試 API HTTP status code
- 驗證 response 資料結構
- 驗證資料類型正確性

### Structure

```
tests/
├── test_api_last_live_list.py
└── __init__.py
```

### Usage

- 執行測試並顯示報告

```bash
pipenv run pytest tests/ -v

```

### Output (CLI)

```bash
tests/test_api_last_live_list.py::TestLastLiveListAPI::test_status_code PASSED
tests/test_api_last_live_list.py::TestLastLiveListAPI::test_response_is_dictionary PASSED
tests/test_api_last_live_list.py::TestLastLiveListAPI::test_recommend_is_list PASSED
tests/test_api_last_live_list.py::TestLastLiveListAPI::test_recommend_length_less_or_equal_20 PASSED
tests/test_api_last_live_list.py::TestLastLiveListAPI::test_pfid_is_int PASSED
tests/test_api_last_live_list.py::TestLastLiveListAPI::test_nickname_is_string PASSED

```
