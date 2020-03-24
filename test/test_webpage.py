from bs4 import BeautifulSoup
import pytest
import pickle
import requests

class TestWebpage:
    @pytest.fixture(autouse=True)
    def get_soup(self):
        index_page = requests.get("http://localhost:8000/index.html")
        soup_index = BeautifulSoup(index_page.content, 'html.parser')
        self._index = soup_index
        
    # testing index.html
    def test_indexpage(self):
        site = self._index.find_all('audio')
        count = 0
        for audio in site:
            count +=1
        assert count==3
         
        site1 = self._index.find('source',{'src':'SampleAudio.mp3'})
        count = 0
        for site1 in self._index.find_all('source',{'src':'SampleAudio.mp3'}):
            count +=1
        assert count==3
        assert self._index.find('audio', {'controls': '', 'preload': 'none'})
        assert self._index.find('audio', {'controls': '', 'loop': ''})