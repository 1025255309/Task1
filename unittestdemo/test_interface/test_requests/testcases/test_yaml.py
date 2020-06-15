"""
回顾使用yaml传参的用法
"""
import os

import yaml


def test_yaml():
    secret = {
        "corpsecret": "xMZ8h3PCTOGFp9TtjvWWfqtX--uwTdCPVcSmzRqRMn8",
        "agent": "xxxx"
    }
    with open("config2.yaml", "w") as f:
        yaml.dump(secret, f)


def test_read():
    print(os.path.abspath(__file__))
    with open("config2.yaml", "r") as f:
        for a in f.readlines():
            print(a)
