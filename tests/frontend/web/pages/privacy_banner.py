from ..mapping.privacy_banner import PrivacyBannerMapping as mapping
from core.web_actions import WebActions


class PrivacyBannerPage:

    @staticmethod
    def is_on_focus(driver):
        web_actions = WebActions(driver)
        return all([web_actions.wait_until_element_visible(mapping.MDL_BANNER),
                    web_actions.wait_until_element_visible(mapping.BTN_AGREE)])

    @staticmethod
    def exit_page(driver):
        web_actions = WebActions(driver)
        web_actions.wait_until_element_clickable(mapping.BTN_AGREE).click()
