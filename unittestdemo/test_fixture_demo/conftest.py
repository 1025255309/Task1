import pytest
@pytest.fixture()
def login():
    print("这是一个登录方法")

def pytest_configure(config):
    marker_list=["search", "login"]  #标签名集合
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )