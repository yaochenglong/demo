import os, sys
from config import setting

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


def insert_img(driver, file_name):
    """
    截图
    :param driver:启动浏览器
    :param file_name: 截图文件名
    :return: 返回指定路径的截图文件
    """
    file_path = setting.TEST_REPORT + '/screenshot/' + file_name
    return driver.get_screenshot_as_file(file_path)
