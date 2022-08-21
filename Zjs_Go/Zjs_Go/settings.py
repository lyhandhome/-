# Scrapy settings for Zjs_Go project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Zjs_Go'

SPIDER_MODULES = ['Zjs_Go.spiders']
NEWSPIDER_MODULE = 'Zjs_Go.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Zjs_Go (+http://www.yourdomain.com)'
DOWNLOAD_DELAY = 0.5
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 100

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
# DEFAULT_REQUEST_HEADERS = {
# 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
# 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Connection': 'keep-alive',
# 'Cookie': '_uab_collina=165940505331078892142473; cna=NElmG7MZFHQCAf/////UhQM0; zh_choose_undefined=s; ZJZWFWSESSIONID=211a7da3-86ce-4aeb-acd1-ed44d53e2158; SERVERID=bf82ef057521af50c2c4a314a4ecd547|1659411623|1659405050; ssxmod_itna=YqIxcWDtG=oCqY5GHD8D2Y6dqlf5WKD0QYh740vPpeGzDAxn40iDtoPTpY3xgjoRxfreRDOGYa+9ECPfwii1DPNFD74i8DCqi1D0qDYzODBLPjbYxDkfx75G9DD59BD3qPGIfq7tDhxBPD04DHDB=DmqGumDeWDr+jS3j2F0QFBoozjie3ere4e2GtuDxY9nx4b0GQmiuFxD3q0iTxD=; ssxmod_itna2=YqIxcWDtG=oCqY5GHD8D2Y6dqlf5WKD0QYhDn9EpAuDDstdtDLjUWu/4nbljtcG8iCEuINqWfOG7dso1YbmLxiIrkGWdFbtBKph8IriEd4yUOohddnbUcpxd3LEziiqcFjFUMpebWu78B4G4FvCPb28whyGxoH8UYb=ulpmWtBmNS0piRgmz9OzpagAAr5QujEdaZAzFl7=C4m7ujDxUmnmC4MQ8fK=8/+Uxb8Ae5g=GUmCG3pteDxGh29Pe1TrAFWbiddreQItaOxUi5mtTugNa6ZAlGvtqDE8SevNkoerGBundx=MmukcMCRu1WgzUr19gzGb1jLrdBeD7QEDGcDG7+iDD; session=1502b265181f4c1ab2b9e48e044e5885; zwlogBaseinfo=eyJsb2dfc3RhdHVzIjoi5pyq55m75b2VIiwidXNlclR5cGUiOiJndWVzdCIsImJpel9zZXNzaW9uX2lkIjoiMTUwMmIyNjUxODFmNGMxYWIyYjllNDhlMDQ0ZTU4ODUiLCJzaXRlX2lkIjoiMSIsInBhZ2VfbW9kZSI6IuW4uOinhOaooeW8jyJ9; JKtongUNID=3097615440; acw_sc__v2=62e89a70dd48eb8730bc104e7576693a3d4714da; acw_tc=2f624a4316594114435773546e2a54b7f08ebec300577ad9ff45df6fa46235',
# }
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Zjs_Go.middlewares.ZjsGoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Zjs_Go.middlewares.ZjsGoDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Zjs_Go.pipelines.ZjsGoPipeline': 300,
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
