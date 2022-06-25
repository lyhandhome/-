import requests
from bs4 import BeautifulSoup
import re
import os
from download import *
url = 'https://www.douyin.com/user/MS4wLjABAAAAs9XEB1Ah5LYjd-zIIwAcUjoGRb1hyEM4pWjNJQ4K1H8'
headers = {
    'cookie': 'ttwid=1%7CB_IOFG0x6ORsFPRCXRXGZy1ka_dARn73oTxJou3mgYw%7C1645768914%7C363e447c3ef0a86202b7704015f67d71985bb0a906fa0ad750c0c4f7158e8363; MONITOR_WEB_ID=e80380fc-a1f4-4be2-982d-2df27bfb3fad; MONITOR_DEVICE_ID=fc795fa1-dfe6-4363-843b-c66053baaf2a; passport_csrf_token_default=2b94bf53036fd9126bc180ce7a4295b8; passport_csrf_token=2b94bf53036fd9126bc180ce7a4295b8; ttcid=970ab501e084484b94af0d64b105fa0636; n_mh=1F6V3qCcXYf8AEgr-VXZSdBYq49NX10l9hZNNYT6F7c; MONITOR_WEB_ID=e6564d90-a8f2-4566-b397-b54967030cae; sso_uid_tt=9b4aa9c3afe83248ffb345a0db27066c; sso_uid_tt_ss=9b4aa9c3afe83248ffb345a0db27066c; toutiao_sso_user=08d5bdefe3737f467dc674708d43597f; toutiao_sso_user_ss=08d5bdefe3737f467dc674708d43597f; sid_ucp_sso_v1=1.0.0-KDkyOGExYmRjZDUxODAxNjMwNDdjNGE2ZDZjOTc2NjU1ZTUxMjg2NTMKHwiUtNC2g4zuBRCYuNqRBhjvMSAMMPOOjogGOAZA9AcaAmxmIiAwOGQ1YmRlZmUzNzM3ZjQ2N2RjNjc0NzA4ZDQzNTk3Zg; ssid_ucp_sso_v1=1.0.0-KDkyOGExYmRjZDUxODAxNjMwNDdjNGE2ZDZjOTc2NjU1ZTUxMjg2NTMKHwiUtNC2g4zuBRCYuNqRBhjvMSAMMPOOjogGOAZA9AcaAmxmIiAwOGQ1YmRlZmUzNzM3ZjQ2N2RjNjc0NzA4ZDQzNTk3Zg; odin_tt=de35ca22f0f45317d27c9e2e7afd3f8bfa2775f47f2f2f350634a15b25652a47595dc27f16152bde759a53dbb2298dce4e6f7088d25e2c9a282c698c86bc7405; passport_auth_status=164fa169c6e9e0e1f2f5a45b4d761c6d%2Cc0f0de9f11781ea4feed68ff5c146195; passport_auth_status_ss=164fa169c6e9e0e1f2f5a45b4d761c6d%2Cc0f0de9f11781ea4feed68ff5c146195; sid_guard=4e2dff63768593ae1b91e62560da1719%7C1647746073%7C5183999%7CThu%2C+19-May-2022+03%3A14%3A32+GMT; uid_tt=1bf5d1ac4a4b5f5700c7eb3409a4a44f; uid_tt_ss=1bf5d1ac4a4b5f5700c7eb3409a4a44f; sid_tt=4e2dff63768593ae1b91e62560da1719; sessionid=4e2dff63768593ae1b91e62560da1719; sessionid_ss=4e2dff63768593ae1b91e62560da1719; sid_ucp_v1=1.0.0-KDdkMGIxNDRkMTQ2YjQ5MjZiNTY3ZjBlMDhmYmNiNjMyMTAxZjM1NGQKGQiUtNC2g4zuBRCZuNqRBhjvMSAMOAZA9AcaAmxmIiA0ZTJkZmY2Mzc2ODU5M2FlMWI5MWU2MjU2MGRhMTcxOQ; ssid_ucp_v1=1.0.0-KDdkMGIxNDRkMTQ2YjQ5MjZiNTY3ZjBlMDhmYmNiNjMyMTAxZjM1NGQKGQiUtNC2g4zuBRCZuNqRBhjvMSAMOAZA9AcaAmxmIiA0ZTJkZmY2Mzc2ODU5M2FlMWI5MWU2MjU2MGRhMTcxOQ; pwa_guide_count=3; _tea_utm_cache_2285=undefined; _tea_utm_cache_2018=undefined; live_can_add_dy_2_desktop=0; ab.storage.userId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%22browser-1648733723087-5%22%2C%22c%22%3A1648733723598%2C%22l%22%3A1648733723603%7D; ab.storage.deviceId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%220f87e6cc-1f19-eed1-716d-44c3e939290e%22%2C%22c%22%3A1648733723605%2C%22l%22%3A1648733723605%7D; ab.storage.sessionId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%22ea2717ec-04cb-cecc-11ac-cdfe785026da%22%2C%22e%22%3A2148733723610%2C%22c%22%3A1648733723601%2C%22l%22%3A1648733723610%7D; FOLLOW_LIVE_POINT_INFO=MS4wLjABAAAAsxgeZFfxMuz2EyYpQ_wMXGQ-GxwWCwG8_S3UsgZYjxvOo-ynQr7zDiSvtV7P0SY7%2F1648828800000%2F0%2F0%2F1648780949698; _tea_utm_cache_6383=undefined; douyin.com; strategyABtestKey=1648947083.455; s_v_web_id=verify_l1ikiozs_QOWbAcFQ_NpEV_4IsL_9itT_0dsyTcIcaNtP; _tea_utm_cache_1300=undefined; THEME_STAY_TIME=299505; IS_HIDE_THEME_CHANGE=1; FOLLOW_NUMBER_YELLOW_POINT_INFO=MS4wLjABAAAAsxgeZFfxMuz2EyYpQ_wMXGQ-GxwWCwG8_S3UsgZYjxvOo-ynQr7zDiSvtV7P0SY7%2F1649001600000%2F0%2F1648952698420%2F0; tt_scid=2jVsE3LWs.T9j0mWxeAgXbpFEsJy24Yp1.u-AVE36YMA4HqgkW1ZOzH96-c56ygDc95a; msToken=pmnL32MxSVVBF_Z7Mqjx2cYW_5fC6m6_OT9sql8sDX_AyCLB6KfPLzaVbinB_pvZsPRR1h99S9tZlWXxVZfvitq2daryqqON7kwxeBX9nJMPw8vT3hGZoho=; home_can_add_dy_2_desktop=1; msToken=yoXide6bl-OcAMZUnPG-darOW7sNpNfOya4r6K0IzbMoli-ITx-bpmplMhg15NEBC5CTsj633U9wHtFd9YvzoiBLRx30PVOiNkwzwO-vLDsckBKZyurIPGQ=; __ac_nonce=062495802001d8cd9b74f; __ac_signature=_02B4Z6wo00f01jJNYagAAIDDuQb6SGpharoybWUAAO7oIA35t41hTxRQijxI2JVyurw4QDHYo7vDnNgX4ovyOZrSr1zgtg-b3wvojH1Rye77JjNfYIKlEAI7kq3VOPOJO6RPkw5dRwKd5JpD81; __ac_referer=https://www.douyin.com/',
    'referer': 'https://www.douyin.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'

}

html=requests.get(url, headers=headers).text
# print(html)

soup = BeautifulSoup(html, 'lxml')
# print(soup)

datas = soup.select('ul.ARNw21RN li')
# print(datas)
for d in datas:
    href = d.select_one('a').attrs['href']
    # print(href)

    index_url = 'https:' + href
    # print(index_url)


# index_url = 'https://www.douyin.com/video/7108021008627469575'
    html1 = requests.get(url=index_url, headers=headers).text
    # print(html1)
    title = re.findall('<title data-react-helmet="true">(.*?)</title>', html1)[0]
    title = ''.join(title).split('#')[0]
    v = re.findall('src(.*?)%3F', html1)[0]
    v_url = requests.utils.unquote(v).replace('":"', 'https:')
    print(v_url)
    print(title)
    download1(v_url, title)
