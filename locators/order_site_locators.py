from selenium.webdriver.common.by import By


class OrderSiteLocators:
    # поле ввода имени
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    # поле ввода фамилии
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    # поле ввода адреса
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    # поле ввода станции метро
    METRO_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    # поле ввода метро для первого кейса
    METRO_UNIVERSITY = (By.XPATH, "//*[@data-index='16']")
    # поле ввода метро для второго кейса
    METRO_DINAMO = (By.XPATH, "//*[@data-index='27']")
    # поле ввода номера телефона
    PHONE_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    # кнопка "Далее"
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    # поле выбора даты
    DATE_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    # выбор даты для первого кейса
    DATE_1 = (By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--020']")
    # выбор даты для второго кейса
    DATE_2 = (By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--025']")
    # поле ввода срока аренды
    RENT_FIELD = (By.CLASS_NAME, "Dropdown-root")
    # поле выбора срока для первого кейса
    RENT_FIELD_1 = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and (text()='сутки')]")
    # поле выбора срока для второго кейса
    RENT_FIELD_2 = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and (text()='трое суток')]")
    # выбор жемчуга
    BLACK_COLOR = (By.ID, "black")
    # выбор безысходности
    GREY_COLOR = (By.ID, "grey")
    # выбор комментария
    COMMENTS = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # кнопка заказа
    ORDER_BUTTON = (By.XPATH, '//*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]')
    # кнопка подтверждения
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    # кнопка просмотра заказа
    STATUS_VIEW = (By.XPATH, ".//*[contains(@class,'Order_ModalHeader')]")