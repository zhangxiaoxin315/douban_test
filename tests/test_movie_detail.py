#coding = UTF-8

import requests
import pytest
import sys,os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_path)

from utils.commlib import get_test_data

cases,list_params = get_test_data(r"E:\douban_test\data\test_movie_detail.yaml")

class TestMovieDetail(object):
    @pytest.mark.parametrize("case,http,expected",list(list_params),ids=cases)
    def test_movie_detail(self,env,case,http,expected):
        url = env['host']['douban'] + http["url"]
        params =http["params"]
        headers = http["headers"]

        r = requests.get(url,params=params,headers=headers)
#        print(r.json())
        response = r.json()
#        print(response['originalName'])

        assert response['originalName'] == expected["response"]["originalName"]


# if __name__ == '__main__':
#     pytest.main(['test_movie_detail.py','-v'])