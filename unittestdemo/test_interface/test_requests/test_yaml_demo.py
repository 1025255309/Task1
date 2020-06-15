import os

import yaml

def test_yaml():

    secrect ={

        "copid" : "xSDsd-asda-asfj-asd",
        "agent" : "xxxdd"
    }
    with open("D:/proiect/unittestdemo/test_interface/test_requests/test.yaml","w+") as f:
        yaml.dump(secrect,f)

def test_read():
    print(os.path.abspath(__file__))
    with open("test.yaml", "r") as f:
        for a in f.readlines():
            print(a)