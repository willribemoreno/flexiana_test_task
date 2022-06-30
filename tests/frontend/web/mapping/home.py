from selenium.webdriver.common.by import By


class HomeMapping:
    TBL_BOARD = (By.ID, 'board')
    TxT_HEADER = (By.XPATH, '//h1[text()="Checkers"]')
    BTN_RESTART = (By.XPATH, '//a[text()[normalize-space() = "Restart..."]]')
    IMG_BLUE_PIECES = (By.CSS_SELECTOR, 'img[name*="space"][src*="me1"]')
    IMG_ORANGE_PIECES = (By.CSS_SELECTOR, 'img[name*="space"][src*="you1"]')
    # PIECE_62 = (By.CSS_SELECTOR, 'img[name*="space"][src*="you1"][onclick="didClick(6, 2)"]')
    IMG_AVAILABLE_GRAY_POSITIONS = (By.CSS_SELECTOR, 'img[name*="space"][src*="gray"]')
    IMG_AVAILABLE_BLACK_POSITIONS = (By.CSS_SELECTOR, 'img[name*="space"][src*="black"]')
