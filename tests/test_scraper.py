import sys
sys.path.insert(1, './scraper')


import scraper

def test_getTemp():
    assert type(scraper.getTemp()) is str
