#unitest oferuje przydatne metody do testowania
import unittest
from selenium import webdriver
class Mojtest(unittest.TestCase):
    def test_logowanie(selfself):
        driver = webdriver.Chrome(executable_path='D:\driver do przgladarek\chromedriver.exe')
        driver.get('https://poczta.interia.pl/logowanie/#iwa_source=sg_ikona')
        title=driver.title
        print(title)
        assert title == 'Konto Interia'
        driver.quit()


