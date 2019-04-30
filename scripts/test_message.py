from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page

import pytest


class TestMessage:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("args", analyze_data("message_data", "test_send_message"))
    def test_send_message(self, args):
        phone = args["phone"]
        message = args["message"]

        self.page.message_list.click_new_message()
        self.page.new_message.input_phone(phone)
        self.page.new_message.input_message(message)
        self.page.new_message.click_send()
