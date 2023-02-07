from selenium import webdriver
import datetime
import time

# 创建浏览器对象
driver = webdriver.Edge()
# 窗口最大化显示
driver.maximize_window()


def login(url):
    driver.get(url)
    driver.implicitly_wait(0.1)


def buy(buy_time):
    '''
    购买函数

    获取页面元素的方法有很多，获取得快速准确又是程序的关键
    在写代码的时候运行测试了很多次，css_selector的方式表现最佳
    link text测试每次轮询<0.3s
    '''

    cookies = driver.get_cookies()
    print(cookies)

    while True:
        # 现在时间大于预设时间则开售抢购
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') > buy_time:
            try:
                if driver.find_element("link text", "立即购买"):
                    driver.find_element("link text", "立即购买").click()
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), "进入下单界面")
                    break
                # time.sleep(0.1)
            except:
                print("无 立即购买 按钮")
                # time.sleep(0.3)

    while True:
        try:
            if driver.find_element("link text", "提交订单"):
                driver.find_element("link text", "提交订单").click()
                # 下单成功，跳转至支付页面
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), "下单成功")
                break
        except:
            print("下单失败")
            # time.sleep(0.5)


if __name__ == "__main__":
    url = "https://chaoshi.detail.tmall.com/item.htm?spm=a1z0d.6639537/tb.1997196601.43.3d385886c8AX5s&id=20739895092"
    mall = "TIANMAO"
    buy_time = "2023-02-07 20:00:00"

    login(url)
    buy(buy_time)
