from selenium.webdriver.common.by import By


class MainSiteLocators:
    # лого "Яндекс"
    YANDEX_LOGO = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    # лого "самокат"
    SCOOTER_LOGO = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    # кнопка заказа сверху
    TOP_ORDER_BUTTON = [By.XPATH, "(.//button[text()='Заказать'])[1]"]
    # кнопка заказа снизу
    DOWN_ORDER_BUTTON = [By.XPATH, "(.//button[text()='Заказать'])[2]"]
    # кнопка куков
    COOKIE_BUTTON = [By.ID, 'rcc-confirm-button']

    # перый вопрос
    FIRST_QUESTION = [By.ID, 'accordion__heading-0']
    # второй вопрос
    SECOND_QUESTION = [By.ID, 'accordion__heading-1']
    # третий вопрос
    THIRD_QUESTION = [By.ID, 'accordion__heading-2']
    # четвертый вопрос
    FOURTH_QUESTION = [By.ID, 'accordion__heading-3']
    # пятый вопрос
    FIFTH_QUESTION = [By.ID, 'accordion__heading-4']
    # шестой вопрос
    SIXTH_QUESTION = [By.ID, 'accordion__heading-5']
    # седьмой вопрос
    SEVENTH_QUESTION = [By.ID, 'accordion__heading-6']
    # восьмой вопрос
    EIGHTH_QUESTION = [By.ID, 'accordion__heading-7']

    # перый ответ
    FIRST_ANSWER = [By.ID, 'accordion__panel-0']
    # второй ответ
    SECOND_ANSWER = [By.ID, 'accordion__panel-1']
    # третий ответ
    THIRD_ANSWER = [By.ID, 'accordion__panel-2']
    # четвертый ответ
    FOURTH_ANSWER = [By.ID, 'accordion__panel-3']
    # пятый ответ
    FIFTH_ANSWER = [By.ID, 'accordion__panel-4']
    # шестой ответ
    SIXTH_ANSWER = [By.ID, 'accordion__panel-5']
    # седбмой ответ
    SEVENTH_ANSWER = [By.ID, 'accordion__panel-6']
    # восьмой ответ
    EIGHTH_ANSWER = [By.ID, 'accordion__panel-7']