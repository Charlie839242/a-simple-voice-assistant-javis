
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unicodecsv
def music(name):
    songname=name

    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(options=chrome_options)

    # browser.get("https://music.taihe.com/")
    # # 通过find_element_by_xpath来定位用户名和密码的输入框
    # browser.find_element_by_xpath("//input[@type='text' and @autocomplete='off' and @valuekey='value']").send_keys(u'大鱼')
    # browser.find_element_by_xpath("//i[@class='iconfont el-input__icon']").click()

    browser.get("https://www.kugou.com/")
    # 通过find_element_by_xpath来定位用户名和密码的输入框
    browser.find_element_by_xpath("//div[@class='search_input']//input").send_keys(u"%s" % songname)
    browser.find_element_by_xpath("//i[@class='search_icon']").click()
    browser.find_element_by_xpath("//ul[@class='list_header clearfix']//li[@class='width_f_li song_name_li']//span").click()
    browser.find_element_by_xpath("//a[@class='play_all']").click()

