import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NewMessagePage(BaseAction):

    # 接收者
    phone_edit_text = By.XPATH, "//*[@text='接收者']"
    # 键入信息
    message_edit_text = By.XPATH, "//*[@text='键入信息']"
    # 发送
    send_button = By.XPATH, "//*[@content-desc='发送']"

    @allure.step(title='新建短信 - 输入 手机号')
    def input_phone(self, content):
        allure.attach('输入手机号：', content)
        self.input(self.phone_edit_text, content)

        # 调用截图方法，输入截图文件名称
        self.screen_shot('input_phone.png')
        # 调用截图保存方法，输入截图标题与保存截图文件名称
        self.allure_pic_with_local('输入手机号截图：', 'input_phone.png')

    @allure.step(title='新建短信 - 输入 短息内容')
    def input_message(self, content):
        allure.attach('输入短信内容：', content)
        self.input(self.message_edit_text, content)

        self.screen_shot('input_message.png')
        self.allure_pic_with_local('输入短信内容截图：', 'input_message.png')

    def click_send(self):
        self.click(self.send_button)
