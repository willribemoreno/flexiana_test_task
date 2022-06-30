from selenium.webdriver.common.by import By


class PrivacyBannerMapping:
    MDL_BANNER = (By.ID, 'qc-cmp2-ui')
    BTN_AGREE = (By.XPATH, '//button[@mode="secondary"][2]')
