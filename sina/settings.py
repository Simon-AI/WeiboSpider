# -*- coding: utf-8 -*-

BOT_NAME = 'sina'

SPIDER_MODULES = ['sina.spiders']
NEWSPIDER_MODULE = 'sina.spiders'

ROBOTSTXT_OBEY = False

# 请将Cookie替换成你自己的Cookie
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie':'SUB=_2A25xTHt3DeRhGeBI7lcW8ijKwzWIHXVSzwU_rDV6PUJbktAKLRXjkW1NRpWgUwvozx2IUU4u3eF_Wl_myBsE-qyu; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWLXiAcM_v7SJK3N9CPrZLr5JpX5KzhUgL.FoqcSK-Neoqc1h.2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMcSo-fS0zcSon4; SUHB=0JvgHDhoQbtLSR; _T_WM=1bccc5d6fbecdabf0e601ba6c4fa85fb'
}

# 当前是单账号，所以下面的 CONCURRENT_REQUESTS 和 DOWNLOAD_DELAY 请不要修改

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 3

DOWNLOADER_MIDDLEWARES = {
    'weibo.middlewares.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None
}

ITEM_PIPELINES = {
    'sina.pipelines.MongoDBPipeline': 300,
}

# MongoDb 配置

LOCAL_MONGO_HOST = '127.0.0.1'
LOCAL_MONGO_PORT = 27017
DB_NAME = 'Sinaa'
