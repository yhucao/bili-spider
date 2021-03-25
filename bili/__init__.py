import logging

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("monitor")
logger.setLevel(logging.INFO)

fh = logging.FileHandler("monitor.log")
fh.setLevel(logging.INFO)

fh.setFormatter(formatter)
logger.addHandler(fh)


connect = {
    "host": "35.185.55.51",
    "port": 3306,
    "user": "root",
    "passwd": "123456",
    "db": "bilibili",
    "charset": "utf8",
}

headers = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}

cols = [
    "v_aid",
    "v_view",
    "v_danmaku",
    "v_reply",
    "v_favorite",
    "v_coin",
    "v_share",
    "v_name",
]
