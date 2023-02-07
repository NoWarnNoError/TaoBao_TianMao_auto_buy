from selenium import webdriver
import datetime
import time

# 创建浏览器对象
driver = webdriver.Edge()
# 窗口最大化显示
driver.maximize_window()


def login(url):
    driver.get(url)
    driver.implicitly_wait(1)

    # time.sleep(2)
    # # 淘宝和天猫的登陆链接文字不同
    # if mall == '1':
    #     # 找到并点击淘宝的登陆按钮
    #     driver.find_element("link text", "亲，请登录").click()
    # else:
    #     # 找到并点击天猫的登陆按钮
    #     driver.find_element("class name", "请登录").click()
    # print("请在30秒内完成登录")
    # # 用户扫码登陆
    # time.sleep(30)


def buy(buy_time):
    '''
    购买函数

    buy_time:购买时间
    mall:商城类别

    获取页面元素的方法有很多，获取得快速准确又是程序的关键
    在写代码的时候运行测试了很多次，css_selector的方式表现最佳
    '''
    # if mall == '1':
    #     # "立即购买"的css_selector
    #     button_buy = '#J_juValid > div.tb-btn-buy > a'
    #     # "立即下单"的css_selector
    #     btn_order = '#submitOrder_1 > div.wrapper > a'
    # else:
    #     button_buy = '#J_LinkBuy'
    #     btn_order = '#submitOrder_1 > div > a'

    while True:
        # 现在时间大于预设时间则开售抢购
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') > buy_time:
            try:
                # 找到“立即购买”，点击
                if driver.find_element("link text", "立即购买"):
                    driver.find_element("link text", "立即购买").click()
                    # driver.find_element("id", button_buy).click()
                    break
                # time.sleep(0.1)
            except:
                print("无 立即购买 按钮")
                # time.sleep(0.3)

    while True:
        try:
            # 找到“立即下单”，点击，
            if driver.find_element("link text", "提交订单"):
                driver.find_element("link text", "提交订单").click()
                # 下单成功，跳转至支付页面
                print("购买成功")
                break
        except:
            time.sleep(0.5)


if __name__ == "__main__":
    url = "https://chaoshi.detail.tmall.com/item.htm?spm=a1z0d.6639537/tb.1997196601.43.3d385886c8AX5s&id=20739895092"
    mall = "TIANMAO"
    buy_time = "2023-02-07 20:00:00"

    login(url)
    buy(buy_time)
