#!/usr/bin/python3
# -*- coding: utf8 -*-
"""
说明: 环境变量`KJWJ_UP`账号密码`-`分割
cron: 20 */6 * * *
new Env('科技玩家-签到');
"""
import requests
import os
# from sendNotify import send
import time



def login():
    os.environ['NO_PROXY'] = 'kejiwanjia.com'
    session = requests.Session()

    login_url = 'https://www.kejiwanjia.com/wp-json/jwt-auth/v1/token'

    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; PBEM00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.52 Mobile Safari/537.36'
    }
    data = {
        'nickname': '',
        'username': '@qq.com',
        'password': '',
        'code': '',
        'img_code': '',
        'invitation_code': '',
        'token': '',
        'smsToken': '',
        'luoToken': '',
        'confirmPassword': '',
        'loginType': ''
    }
    res = session.post(login_url, headers=headers, data=data)

    if res.status_code == 200:
        status = res.json()
        print(f"账号`{status.get('name')}`登陆成功")
        print(f"ID：{status.get('id')}")
        print(f"金币：{status.get('credit')}")
        print(f"等级：{status.get('lv').get('lv').get('name')}")
        token = status.get('token')
        get_head = {
            'authorization': f'Bearer {token}',
            'origin': 'https://www.kejiwanjia.com',
            'referer': 'https://www.kejiwanjia.com/newsflashes',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; PBEM00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.52 Mobile Safari/537.36'
        }
        respg = session.post('https://www.kejiwanjia.com/wp-json/b2/v1/getUserMission', headers=get_head)
        if respg.status_code == 200:
            check_url = 'https://www.kejiwanjia.com/wp-json/b2/v1/userMission'
            check_head = {
                'authorization': f'Bearer {token}',
                'origin': 'https://www.kejiwanjia.com',
                'referer': 'https://www.kejiwanjia.com/task',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; PBEM00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.52 Mobile Safari/537.36'

            }
            resp = session.post(check_url, headers=check_head)
            if resp.status_code == 200:
                info = resp.json()
                if type(info) == str:
                    print(f"已经签到：{info}金币")
                else:
                    print(f"签到成功：{info.get('credit')}金币")
    else:
        print('账号登陆失败: 账号或密码错误')


if __name__ == '__main__':
    login()
