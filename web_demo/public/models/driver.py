from selenium.webdriver import Remote
from selenium import webdriver

# def browser():
#     """
#     启动浏览器
#     :return: 返回浏览器驱动url
#     """
#     try:
#         host = '127.0.0.1:4444'
#         driver = Remote(command_executor='http://' + host + '/wd/hub',
#                         desired_capabilities={'paltform': 'ANY',
#                                               'browserName': 'chrome',
#                                               'version': "",
#                                               'javascriptEnabled': True})
#         return driver
#
#     except Exception as msg:
#         print('驱动异常->{0}'.format(msg))


def browser():
    a = r'D:\安装包\GoogleChrome_65.0.3325.146_x86\ChromePortable\App\Google Chrome\chromedriver.exe'
    driver = webdriver.Chrome(a)
    return driver
