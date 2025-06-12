# lang-live-assignment

包含兩個功能：

1. Streamer Data Fetcher
2. QA Validation with pytest

## Streamer Data Fetcher

從 Lang Live 官網首頁爬取 pfid 介於 4000000–5000000 的主播資料

### Features

- 取得 Lang Live 官網首頁 API 資料
- 篩選 pfid 介於 4000000 ～ 5000000（含）之間的主播
- 輸出符合條件主播的 pfid 及主播暱稱

### Project Structure

```
fetch_streamers/
├── main.py                 # Main entry point
├── parser.py               # API parsing module
├── api_url.py              # API endpoint
└── filtered_streamers.csv  # Output results

```

### Requirements

- Python 3.13
- Pipenv

### Setup

1. 安裝 pipenv 與依賴套件：

```bash
pip install pipenv
pipenv install
```

2. 執行程式：

```bash
cd fetch_streamers
pipenv run python main.py
```

3. 程式會自動抓取資料並輸出到  `filtered_streamers.csv`

### Output

- 檔案格式：CSV
- 欄位：`pfid` 及 `Nickname`（主播暱稱）
