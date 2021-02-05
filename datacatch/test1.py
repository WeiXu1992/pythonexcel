from selenium import webdriver
from bs4 import BeautifulSoup
import self
import re
import time
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(1)
# 设置窗口大小
driver.set_window_size(800, 1000)
# 填写要爬的百度文库word的链接
url = "https://wenku.baidu.com/view/b26ca32326284b73f242336c1eb91a37f11132f5.html?fr=search-1-wk_sea-income2"#https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html
driver.get(url)
time.sleep(3)

#for i in range(1,10):
        # 滚动至元素ele可见位置（即阅读更多部分）
eles1 = driver.find_elements_by_xpath("//span[@class='moreBtn goBtn']")
        #eles1 = driver.find_elements_by_xpath("//span[@class='read-all']")
        #eles1 = driver.find_elements_by_xpath("//div[@class='fold-page-text']")
        #eles1.click()
if eles1 != []:
    print('1')
    ele1 = eles1[0]
    driver.execute_script("arguments[0].scrollIntoView();", ele1)
                # 向上滚动
    driver.execute_script('window.scrollBy(0,-200)')
                # 点击阅读更多
    ele1.click()
#time.sleep(3)
#eles2 = driver.find_elements_by_xpath("//a[@class='pageList-btn next-pageList hidden-doc-banner']")
        #eles1 = driver.find_elements_by_xpath("//span[@class='read-all']")
        #eles1 = driver.find_elements_by_xpath("//div[@class='fold-page-text']")

        #eles1.click()
#用js选择所属机构
#view_detail_tag = driver.find_elements_by_css_selector("[class='pageList-btn next-pageList hidden-doc-banner']")
#btn_div = view_detail_tag.find_element_by_css_selector("[class='ic ic-pageList-icon']")

#driver.execute_script("arguments[0].click();", btn_div)
eles2 = driver.find_elements_by_xpath("//a[@class='pageList-btn next-pageList hidden-doc-banner']") #先点击下拉按钮
#ele2 = else2[0]
#driver.execute_script("arguments[0].click();", ele2)
if eles2 != []:
    print('2')
    ele2 = eles2[0]
    driver.execute_script("arguments[0].scrollIntoView();", ele2)
                # 向上滚动
    driver.execute_script('window.scrollBy(0,-200)')
                # 点击阅读更多
    ele2.click()

#time.sleep(3)
eles3 = driver.find_elements_by_xpath("//div[@class='fold-page-text']") #先点击下拉按钮
#ele2 = else2[0]
#driver.execute_script("arguments[0].click();", ele2)
if eles3 != []:
    print('3')
    ele3 = eles3[0]
    driver.execute_script("arguments[0].scrollIntoView();", ele3)
                # 向上滚动
    driver.execute_script('window.scrollBy(0,-200)')
                # 点击阅读更多
    ele3.click()
eles4 = driver.find_elements_by_xpath("//span[@class='moreBtn goBtn']")
        #eles1 = driver.find_elements_by_xpath("//span[@class='read-all']")
        #eles1 = driver.find_elements_by_xpath("//div[@class='fold-page-text']")
        #eles1.click()
if eles4 != []:
    print('4')
    ele4 = eles4[0]
    driver.execute_script("arguments[0].scrollIntoView();", ele4)
                # 向上滚动
    driver.execute_script('window.scrollBy(0,-200)')
                # 点击阅读更多
    ele4.click()
#time.sleep(3)
"""
eles5 = driver.find_elements_by_xpath("//div[@class='fold-page-text']") #先点击下拉按钮
#ele2 = else2[0]
#driver.execute_script("arguments[0].click();", ele2)
if eles5 != []:
    print('5')
    ele5 = eles5[0]
    driver.execute_script("arguments[0].scrollIntoView();", ele5)
                # 向上滚动
    driver.execute_script('window.scrollBy(0,-200)')
                # 点击阅读更多
    ele5.click()
#time.sleep(3)

eles6 = driver.find_elements_by_xpath("//div[@class='fold-page-text']") #先点击下拉按钮
#ele2 = else2[0]
#driver.execute_script("arguments[0].click();", ele2)
if eles6 != []:
    print('6')
    ele6 = eles6[0]
    driver.execute_script("arguments[0].scrollIntoView();", ele6)
                # 向上滚动
    driver.execute_script('window.scrollBy(0,-200)')
                # 点击阅读更多
    ele6.click()
time.sleep(30)
eles7 = driver.find_elements_by_xpath("//div[@class='fold-page-text']") #先点击下拉按钮
#ele2 = else2[0]
#driver.execute_script("arguments[0].click();", ele2)
if eles7 != []:
    print('7')
    ele7 = eles7[0]
    driver.execute_script("arguments[0].scrollIntoView();", ele7)
    time.sleep(20)
                # 向上滚动
    driver.execute_script('window.scrollBy(0,-200)')
                # 点击阅读更多
    ele7.click()
#org = driver.find_element_by_xpath("//i[@class='ic ic-pageList-icon']")  #定位要选择的元素，注意这里用的是find_element
#scrollIntoView()是DOM API的一部分，需要运行它WebElement但不能在列表的WebElement（S），所以不能用find_elements
#driver.execute_script("arguments[0].scrollIntoView();", org)  #执行js，使滚动条下滑至要定位的元素位置
#time.sleep(3)   #等待几秒查看滚动条是否下滑
#org.click()     #点击操作
#element = driver.find_element_by_id(id:'next-pageList-1')
#webdriver.ActionChains(driver).move_to_element(element ).click(element ).perform()
"""



"""
# 模拟鼠标点击“点击加载更多“
pos2 = driver.find_elements_by_xpath("//span[@class='moreBtn goBtn']")#driver.find_elements_by_xpath("//a[@class='pageList-btn next-pageList hidden-doc-banner']"),driver.find_elements_by_xpath("//span[@class='moreBtn goBtn']")
pos3 = driver.find_element_by_xpath("//span[@class='read-all']")
if pos2 != []:
    print('1')
    ele2 = pos2[0]
    driver.execute_script("arguments[0].scrollIntoView();", ele2)
                # 向上滚动
    driver.execute_script('window.scrollBy(0,-200)')
                # 点击阅读更多
    ele2.click()


loop = 1
while loop <= 5:
    time.sleep(1)
    ActionChains(driver).move_to_element(pos2).perform()
    ActionChains(driver).click(pos3).perform()
    loop = loop + 1


attempts = 0
success = True
while attempts < 10 and success:
    try:
        # 向下滑动，到有“点击加载更多”的位置停止
        pagerwg = driver.find_elements_by_xpath("//a[@class='pageList-btn next-pageList hidden-doc-banner']")
        # 拖动到可见的元素
        driver.execute_script('arguments[0].scrollIntoView();', pagerwg[-1])
        driver.execute_script('window.scrollBy(0,-200)')
        # 模拟点击，加载更多页面
        more_text = driver.find_elements_by_xpath("//a[@class='pageList-btn next-pageList hidden-doc-banner']")
        more_text.click()

    except:
        success = False
        attempts += 1
        print('到底啦~~！请开始你的爬虫表演>.<')

    # 等待网页加载每次点击间隔2s
    time.sleep(3)"""
#eles2 = driver.find_elements_by_xpath("//a[@class='pageList-btn next-pageList hidden-doc-banner']")
#print('2')

#driver.execute_script("arguments[0].scrollIntoView();", eles2[-1])
                # 向上滚动
#driver.execute_script('window.scrollBy(0,-200)')
                # 点击阅读更多
#more_text = driver.find_element_by_xpath("//a[@class='pageList-btn next-pageList hidden-doc-banner']")
#more_text.click()




"""
attempts = 0
success = True
while attempts < 10 and success:
    try:
        # 向下滑动，到有“点击加载更多”的位置停止
        pagerwg = driver.find_elements_by_xpath("//div[@class='pagerwg-root']")
        # 拖动到可见的元素
        driver.execute_script('arguments[0].scrollIntoView();', pagerwg[-1])

        # 模拟点击，加载更多页面
        more_text = driver.find_element_by_xpath("//span[@class='pagerwg-arrow-lower']")
        more_text.click()

    except:
        success = False
        attempts += 1
        print('到底啦~~！请开始你的爬虫表演>.<')

    # 等待网页加载每次点击间隔2s
    time.sleep(3)
"""
#time.sleep(60)
# 获取此时页面资源
html = driver.page_source
print('step 191')
bdwk1 = BeautifulSoup(html, 'html5lib')##html5lib是一个html解析库，使用BeautifulSoup进行解析html会用到。当然也可以使用python自带的库html.parser不过兼容性没有html5lib好。 html5lib不是自带，使用的时候需要安装一下。
# 定义一个列表，用于之后文本的处理
print('step 193')
textlist = []
# 找到存放文本的标签
print('step 196')
#bdwk5 = bdwk1.findAll()
#html = driver.page_source
#bf = BeautifulSoup(html, 'lxml')
"""
get_docx_name = bdwk1.find(class_='doc-title').get_text()
docx_name = re.sub('\s', '', get_docx_name) + '.docx'
pages = bdwk1.find_all(class_='reader-page')
import docx
file = docx.Document()
with open('wenku.txt', 'w', encoding='utf-8') as f:
    for page in pages:
        para = page.find_all(class_='txt')
        for p in para:
            text = p.get_text()
            f.write(text + '\n')
            file.add_paragraph(text)
file.save(docx_name)
"""
bdwk5 = bdwk1.findAll('div', {'id': re.compile('^pageNo.*')})
#bdwk5 = bdwk1.findAll('div', {'class': re.compile('^reader-page.*')})#reader-txt-layer
#bdwk5 = bdwk1.findAll(class_='reader-txt-layer')
#bdwk5 = bdwk1.findAll('div', {'class': re.compile('^mod reader-page complex.*')})#reader-txt-layer
# 对每个存放文本的标签进行遍历处理
print('step 197')
print(bdwk5)
#time.sleep(40)
i = 0
for bdwk6 in bdwk5:
    # 获取该bdwk6下class的属性，得到的是字典
    #i=i+1
    #print(i)
    a = bdwk6.attrs['id']
    print(a)
    # 将a中的元素使用空格连接，得到字符串
    b = ' '.join(a)
    print(b)
    # 组合成xpath的标签形式，并使页面滚动至该页面处
    c = "//div[@id='" + b + "']"
    print(c)
    eles9 = driver.find_elements_by_xpath(c)
    ele9 = eles9[0]
    driver.execute_script("arguments[0].scrollIntoView();", ele9)
    time.sleep(0.5)  # 注意，此处不要删，可根据情况自行设置
    # 取得该页面涉及到的文本资源
    html = driver.page_source
    bdwk1 = BeautifulSoup(html, 'html5lib')
    bdwk2 = bdwk1.find_all('div', {'class': 'ie-fix'})
    # 对是否取得重复文字进行判断，若不重复，则写入wenku.txt
    for bdwk4 in bdwk2:
        d = bdwk4.get_text()
        if d not in textlist:
            textlist.append(d)
            with open('wenku.txt', 'w', encoding='utf-8') as f:
                #print("is writing")
                f.write(str(d))  # 将字符串写入文件中
            print(d, end='')
#driver.close()
