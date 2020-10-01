# Scrapy settings for myscrapys project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'myscrapys'        # 爬虫项目名

SPIDER_MODULES = ['myscrapys.spiders']    # 爬虫位置
NEWSPIDER_MODULE = 'myscrapys.spiders'    # 新建的爬虫位置

LOG_LEVEL = "WARNING"                   # 日志等级

LOG_FILE = "douban.log"            # 生成的日志

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'     # 请求是用的用户代理

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'myscrapys (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True         # 遵守robot协议

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32          # 最大并发请求

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3       # 下载延迟 ，当请求时发出等待3秒
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16      # 最大并发请求域名数
#CONCURRENT_REQUESTS_PER_IP = 16          # 最大并发请求ip数

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False      # 在请求下一个url时，cookie可以存放上一个url 默认开启

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {         # 默认请求头
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'myscrapys.middlewares.MyscrapysSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'myscrapys.middlewares.MyscrapysDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'myscrapys.pipelines.MyscrapysPipeline': 300,     # 要使用pipelines就必须设置这个配置，300是与引擎的距离值，用来当有多个pipelines时，就看这个值哪个小就先执行哪一个
   'myscrapys.pipelines.MyscrapysPipeline1': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
