import requests
import json

from requests import models
headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

url = "https://www.hackerrank.com/rest/contests/selftest-py/judge_submissions"
headers["Cookie"] = "_utma=74197771.287559364.1638620886.1638621056.1638621056.1;utmb=74197771.190.9.1638623808169;utmc=74197771;utmt=1;_utmz=74197771.1638621056.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none);_biz_flagsA=%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D;_biz_nA=97;_biz_pendingA=%5B%5D;_biz_sid=5a0ebd;_biz_uid=23f7860e06484993bd17d650e1bede88;_clck=1gno3bo|1|ewz|0;_clsk=1dbobho|1638620979526|3|1|e.clarity.ms/collect;_ga=GA1.2.287559364.1638620886;_gat_UA-45092266-26=1;_gat_UA-45092266-28=1;_gid=GA1.2.62864430.1638620886;_mkto_trk=id:487-WAY-049&token:_mch-hackerrank.com-1638620922503-60658;_uetsid=b560091054fd11ecae7b67cbf7651e7d;_uetvid=b5605c4054fd11ecaacdd934ad525e31;hackerrank_mixpanel_token=68a022fb-acf3-4501-9225-bfc2ceb15396;mp_bcb75af88bccc92724ac5fd79271e1ff_mixpanel=%7B%22distinct_id%22%3A%20%226e2da817-cd6c-4810-93fc-eb26c690ac4c%22%2C%22%24device_id%22%3A%20%2217d856af3486b6-0ebcc9dcee642-978183a-e1000-17d856af34978c%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22%24user_id%22%3A%20%226e2da817-cd6c-4810-93fc-eb26c690ac4c%22%7D;optimizelyBuckets=%7B%7D;optimizelyEndUserId=oeu1638622953481r0.9831572223250027;optimizelySegments=%7B%221709580323%22%3A%22false%22%2C%221717251348%22%3A%22gc%22%2C%221719390155%22%3A%22direct%22%2C%222308790558%22%3A%22none%22%7D;user_type=hacker;_an_uid=-1;_gd_session=22932a75-35dc-4d49-8028-229b3e3be737;_gd_svisitor=0720b07b040e0000f55eab61e801000095f78e00;_gd_visitor=4a94ed61-5481-4436-8576-6a208564ed23;_hrank_session=28aee78b644b722d3566684fc3654d730e779641dc40db1b75ef985b51666c07874570a4c63937db7a235904629eb1e8e7ab7cdc8d045afd7fbe789dae428ac5;enableIntellisenseUserPref=true;fileDownload=true;h_r=logo;hacker_editor_theme=light;hrc_l_i=T;metrics_user_identifier=5a6e9a-7bf8ff6551a5dc6bfad64a56e855beba1ba14ca3;react_var=false__cnt6;react_var2=false__cnt6;remember_hacker_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaGJDRnNHYVFPYWJsb2lJaVF5WVNReE1DUlhhemxxV25aT1NtNVRaMkpSY21WNGExQlNhMDB1U1NJWE1UWXpPRFl5TVRBME5TNDNOalE0TWpFNEJqb0dSVVk9IiwiZXhwIjoiMjAyMS0xMi0xOFQxMjozMDo0NS43NjRaIiwicHVyIjpudWxsfX0%3D--2979c8457bfaac9712cd414a06deb6739dc20c69;selftest-py_crp=*nil*;session_id=61svla3z-1638621054854;show_cookie_banner=false;web_browser_id=a047e7b1415dbaa4445ff5411b70687c;"


resp = requests.get(url, headers=headers)
models = json.loads(resp.content)['models']
submission_ids = [model['id'] for model in models]

subs = {}
for id in submission_ids:
    url2 = f'https://www.hackerrank.com/rest/contests/selftest-py/submissions/{id}'
    resp = requests.get(url2, headers=headers)
    model = json.loads(resp.content)['model']

    key = model['hacker_username'] if 'hacker_username' in model.keys() else model['hacker_id']
    if key not in subs:
        subs[key] = []
    subs[key].append(model['code'])

print(subs)