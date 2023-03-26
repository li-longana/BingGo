import os
import time
import random
from msedge.selenium_tools import Edge, EdgeOptions

# 创建Edge浏览器的选项对象
options = EdgeOptions()
options.use_chromium = True
options.add_argument("start-maximized")

driver_path = os.path.join(os.getcwd(), 'msedgedriver.exe')
# # 创建Edge浏览器驱动程序对象
driver = Edge(options=options, executable_path=driver_path)

# 设置搜索关键字列表
search_keywords = ['apple', 'orange', 'banana', 'grape', 'kiwi', 'pear', 'watermelon', 'pineapple', 'mango', 'papaya', 'orange1', 'orange2', 'orange11']

# 执行100次随机搜索
for i in range(91):
    # 随机选择搜索关键字
    keyword = random.choice(search_keywords)+str(i)
    # 访问Bing主页
    driver.get('https://www.bing.com')
    time.sleep(1)
    # 在搜索框中输入关键字并提交搜索
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(keyword)
    search_box.submit()
    time.sleep(1)
    # 输出当前搜索的关键字
    print(f'Search #{i+1}: {keyword}')
    # 等待一段随机时间，模拟人工搜索
    time.sleep(random.randint(1, 5))

# 关闭浏览器
driver.quit()

options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 11; Redmi K30 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.09.4.5079")
#模拟移动端
driver2 = Edge(options=options, executable_path=driver_path)
# 移动端
# 执行100次随机搜索
for i in range(61):
    # 随机选择搜索关键字
    keyword = random.choice(search_keywords)+str(i)
    # 访问Bing主页
    driver2.get('https://www.bing.com')
    time.sleep(1)
    # 在搜索框中输入关键字并提交搜索
    search_box = driver2.find_element_by_name('q')
    search_box.send_keys(keyword)
    search_box.submit()
    time.sleep(1)
    # 输出当前搜索的关键字
    print(f'Search #{i+1}: {keyword}')
    # 等待一段随机时间，模拟人工搜索
    time.sleep(random.randint(1, 5))

# 关闭浏览器
driver2.quit()
