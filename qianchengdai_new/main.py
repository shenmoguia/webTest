# -*- coding:utf-8 -*-
import pytest

if __name__ == '__main__':
    pytest.main(['-s', '--reruns', '3', r'--html=Result\report\web.html', r'--alluredir=Result\report\allure'])
    #  r'--alluredir=Result\report\allure'
