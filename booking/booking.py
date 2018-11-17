from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Booking_com:
    def __init__(self, driver_path):
        # http://chromedriver.chromium.org/downloads
        self.driver = webdriver.Chrome(driver_path)
        # Начало парсинга с уже выбранных некоторых параметров,
        # таких как: город вылета, количество людей, даты
        self.driver.get("https://www.booking.com/searchresults.ru.html?aid=397607&label=gog235jc-index-ru-XX-XX-unspec-ru-com-L%3Aru-O%3AosSx-B%3Achrome-N%3AXX-S%3Abo-U%3Ac-H%3As&sid=f48be79d410adde80065c5e0d337018e&sb=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.ru.html%3Faid%3D397607%3Blabel%3Dgog235jc-index-ru-XX-XX-unspec-ru-com-L%253Aru-O%253AosSx-B%253Achrome-N%253AXX-S%253Abo-U%253Ac-H%253As%3Bsid%3Df48be79d410adde80065c5e0d337018e%3Bsb_price_type%3Dtotal%26%3B&ss=%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&checkin_monthday=1&checkin_month=12&checkin_year=2018&checkout_monthday=8&checkout_month=12&checkout_year=2018&no_rooms=1&group_adults=2&group_children=0&b_h4u_keep_filters=&from_sf=1&ss_raw=vjc&dest_id=&dest_type=&search_pageview_id=016e96b9f2ba006e&search_selected=false")

    def find_hotels(self, city):
        # элемент для ввода места назначения
        to_input = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.ID, 'ss')))
        to_input.clear()
        # Ввести название города
        to_input.send_keys(city)

        submit_button = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '#frm > div.xp__fieldset.accommodation > div.xp__button > div.sb-searchbox-submit-col.-submit-button > button')))
        ActionChains(self.driver).click(submit_button).perform()

        # # Если не получилось точно определить город, то выбрать первый из предложенных booking
        # results = self.driver.find_elements_by_class_name('disam-single-result')
        # ActionChains(self.driver).click(results[0]).perform()

    def get_prices(self):
        """ Сбор цен на жилье со страницы """
        prices = []
        elements = self.driver.find_elements_by_class_name('price')
        for element in elements:
            # Преобразование цены '123 456 руб.' к виду 123456
            try:
                price_str = element.find_element_by_tag_name('b').text
                if price_str:
                    prices.append(int(price_str[:-5].replace(' ', '')))
            except Exception as e:
                pass
        return prices

    def pagination(self, num_pages):
        """ Функция переходит по страницам и собирает цены """
        prices = []
        for _ in range(num_pages):
            print(f"Страница {_}")
            try:
                prices += self.get_prices()
                link = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "#search_results_table > div.bui-pagination.results-paging > div.bui-pagination__nav > ul > li.bui-pagination__item.bui-pagination__next-arrow > a")))
                if not link:
                    break
                ActionChains(self.driver).click(link).perform()
                print("Start waiting")
                self.driver.implicitly_wait(20)
            except Exception as e:
                print(e)
                break
        return prices

    @staticmethod
    def avg_price(self, prices):
        if prices:
            return round(sum(prices)/len(prices), 2)

    @staticmethod
    def put_price_to_table(self, price, city, country):
        """ Добавить среднюю цену проживания в городе """
        return f"Страна: {country} \n Город: {city} \n Цена: {price}"

    def main(self):
        pass


if __name__ == "__main__":
    booking = Booking("/Users/aleksandrmusorin/Desktop/курс/3. Основы сбора данных/chromedriver")
    booking.find_hotels("Милан")
    prices = booking.pagination(5)
    print(prices)
