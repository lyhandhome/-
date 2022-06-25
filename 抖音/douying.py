import time
from download import download, download1
import requests
import re
from selenium import webdriver
import os

def drop_down():
    # 执行页面滚动的操作  JavaScript
    for i in range(1, 100, 4):  # 1 3 5 7 9 在你不断的下拉过程中， 页面高度也会变的
        time.sleep(1)
        j = i / 9  # 1/9 3/9 5/9 7/9
        # document.documentElement.scrollTop 指定滚动条的位置
        # document.documentElement.scrollHeight 获取浏览器页面的最大高度
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


driver = webdriver.Chrome()
driver.get('https://www.douyin.com/user/MS4wLjABAAAAs9XEB1Ah5LYjd-zIIwAcUjoGRb1hyEM4pWjNJQ4K1H8')
time.sleep(10)
drop_down()
data_list = driver.find_elements_by_css_selector('div.ckqOrial > div.mwbaK9mv > div:nth-child(2) > ul li')
for d in data_list:
    a_url = d.find_element_by_css_selector('a').get_attribute('href')
    # print(a_url)

    headers = {
        'cookie': 'douyin.com; ttwid=1%7CB_IOFG0x6ORsFPRCXRXGZy1ka_dARn73oTxJou3mgYw%7C1645768914%7C363e447c3ef0a86202b7704015f67d71985bb0a906fa0ad750c0c4f7158e8363; MONITOR_WEB_ID=e80380fc-a1f4-4be2-982d-2df27bfb3fad; MONITOR_DEVICE_ID=fc795fa1-dfe6-4363-843b-c66053baaf2a; ttcid=970ab501e084484b94af0d64b105fa0636; n_mh=1F6V3qCcXYf8AEgr-VXZSdBYq49NX10l9hZNNYT6F7c; MONITOR_WEB_ID=e6564d90-a8f2-4566-b397-b54967030cae; sso_uid_tt=9b4aa9c3afe83248ffb345a0db27066c; sso_uid_tt_ss=9b4aa9c3afe83248ffb345a0db27066c; toutiao_sso_user=08d5bdefe3737f467dc674708d43597f; toutiao_sso_user_ss=08d5bdefe3737f467dc674708d43597f; sid_ucp_sso_v1=1.0.0-KDkyOGExYmRjZDUxODAxNjMwNDdjNGE2ZDZjOTc2NjU1ZTUxMjg2NTMKHwiUtNC2g4zuBRCYuNqRBhjvMSAMMPOOjogGOAZA9AcaAmxmIiAwOGQ1YmRlZmUzNzM3ZjQ2N2RjNjc0NzA4ZDQzNTk3Zg; ssid_ucp_sso_v1=1.0.0-KDkyOGExYmRjZDUxODAxNjMwNDdjNGE2ZDZjOTc2NjU1ZTUxMjg2NTMKHwiUtNC2g4zuBRCYuNqRBhjvMSAMMPOOjogGOAZA9AcaAmxmIiAwOGQ1YmRlZmUzNzM3ZjQ2N2RjNjc0NzA4ZDQzNTk3Zg; odin_tt=de35ca22f0f45317d27c9e2e7afd3f8bfa2775f47f2f2f350634a15b25652a47595dc27f16152bde759a53dbb2298dce4e6f7088d25e2c9a282c698c86bc7405; sid_guard=4e2dff63768593ae1b91e62560da1719%7C1647746073%7C5183999%7CThu%2C+19-May-2022+03%3A14%3A32+GMT; uid_tt=1bf5d1ac4a4b5f5700c7eb3409a4a44f; uid_tt_ss=1bf5d1ac4a4b5f5700c7eb3409a4a44f; sid_tt=4e2dff63768593ae1b91e62560da1719; sessionid=4e2dff63768593ae1b91e62560da1719; sessionid_ss=4e2dff63768593ae1b91e62560da1719; sid_ucp_v1=1.0.0-KDdkMGIxNDRkMTQ2YjQ5MjZiNTY3ZjBlMDhmYmNiNjMyMTAxZjM1NGQKGQiUtNC2g4zuBRCZuNqRBhjvMSAMOAZA9AcaAmxmIiA0ZTJkZmY2Mzc2ODU5M2FlMWI5MWU2MjU2MGRhMTcxOQ; ssid_ucp_v1=1.0.0-KDdkMGIxNDRkMTQ2YjQ5MjZiNTY3ZjBlMDhmYmNiNjMyMTAxZjM1NGQKGQiUtNC2g4zuBRCZuNqRBhjvMSAMOAZA9AcaAmxmIiA0ZTJkZmY2Mzc2ODU5M2FlMWI5MWU2MjU2MGRhMTcxOQ; ab.storage.userId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%22browser-1648733723087-5%22%2C%22c%22%3A1648733723598%2C%22l%22%3A1648733723603%7D; ab.storage.deviceId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%220f87e6cc-1f19-eed1-716d-44c3e939290e%22%2C%22c%22%3A1648733723605%2C%22l%22%3A1648733723605%7D; ab.storage.sessionId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%22ea2717ec-04cb-cecc-11ac-cdfe785026da%22%2C%22e%22%3A2148733723610%2C%22c%22%3A1648733723601%2C%22l%22%3A1648733723610%7D; s_v_web_id=verify_l1y822zr_rEVmFOxS_25Ht_4Gkm_AV2h_J3MZNtHCKSzC; _tea_utm_cache_6383=undefined; _tea_utm_cache_1300=undefined; THEME_STAY_TIME=299508; IS_HIDE_THEME_CHANGE=1; passport_csrf_token=253641df084c92dba017c280ea35eb7c; passport_csrf_token_default=253641df084c92dba017c280ea35eb7c; _tea_utm_cache_2285=undefined; FOLLOW_LIVE_POINT_INFO=MS4wLjABAAAAsxgeZFfxMuz2EyYpQ_wMXGQ-GxwWCwG8_S3UsgZYjxvOo-ynQr7zDiSvtV7P0SY7%2F1651248000000%2F0%2F1651191538899%2F0; douyin.com; strategyABtestKey=1651378687.444; pwa_guide_count=3; _tea_utm_cache_2018=undefined; FOLLOW_NUMBER_YELLOW_POINT_INFO=MS4wLjABAAAAsxgeZFfxMuz2EyYpQ_wMXGQ-GxwWCwG8_S3UsgZYjxvOo-ynQr7zDiSvtV7P0SY7%2F1651420800000%2F0%2F0%2F1651388493044; __ac_nonce=0626e5853009439abade0; __ac_signature=_02B4Z6wo00f016c-JWQAAIDCLHW-hBLB.7OnHiHAAIuqsPFf2L02S.YO99bOfC8v9BhKAarkXvTSCiDSDevlJi.MuyD3CjjtnMP3CxmirkdVIEWFxkQpvmIlJTL0IpEsWdBR7UDNRmPJoHOG51; msToken=PBHhN-eUe4ok5YFvuEcKBh6Nr6D0D_W9fRXavyBDQlZJdOfC_iLzqan0iJvuZikl_agFwHssUBmbsDXBWBcizgVW8zau_o-szYt6_Q21XBvE0WNkrpaONQ==; home_can_add_dy_2_desktop=1; msToken=DtolrgUnR7xbC6ddJh0Brn2vXVcTtbSaX4WpDueeR6CZyM7XMP5QizOHILO4fvQz_R6qljH9Xy2YBB5TEjoPB-Yashd265A62437JKsxHEce_tiEdYdc3lvPLiFO7VU=; tt_scid=OzKTxq5ws9dCL47lm56kUx-ZeKUnMr.hbU0yuY3qEfZXKjaLmnE8IdTI73L2WA4c24b7',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
    }
    # a_url='https://www.douyin.com/video/7088630158860520739'
    # a_url = 'https://www.douyin.com/video/7082751878999592206'
    html = requests.get(a_url, headers=headers)
# print(html.text)

    # name = re.findall('<title data-react-helmet="true">“(.*?)"#', html.text,)[0]
    # print(name)
    v = re.findall('src(.*?)a%3D6', html.text)[0]
    # print(v)


    v_url = requests.utils.unquote(v).replace('":"', 'https:')
    print(v_url)
    v_content = requests.get(v_url).content
    # download1(v_url, name)
    download(v_url)
