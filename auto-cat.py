import argparse
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Handler:
    class URL:
        MAIN = "https://popcat.click"

    class Config:
        DEBUG = False
        HEADLESS = False

    def __init__(self, driver_path: str):
        options = Options()
        if Handler.Config.HEADLESS:
            options.add_argument("headless")
        options.add_argument("window-size=540,1024")
        options.add_argument("disable-gpu")
        options.add_argument("disable-infobars")
        # options.add_argument("disable-popup-blocking")
        options.add_argument("disable-extensions")
        options.add_argument("start-maximized")
        options.add_argument("no-sandbox")
        options.add_argument("disable-dev-shm-usage")
        options.add_argument('ignore-certificate-errors')
        options.add_argument('ignore-ssl-errors')
        options.add_experimental_option('prefs', {
            'profile.default_content_setting_values': {
                # 'cookies': 2,
                # 'images': 2,
                'plugins': 2,
                'popups': 2,
                'geolocation': 2,
                'notifications': 2,
                'auto_select_certificate': 2,
                'fullscreen': 2,
                'mouselock': 2,
                'mixed_script': 2,
                'media_stream': 2,
                'media_stream_mic': 2,
                'media_stream_camera': 2,
                'protocol_handlers': 2,
                'ppapi_broker': 2,
                'automatic_downloads': 2,
                'midi_sysex': 2,
                'push_messaging': 2,
                'ssl_cert_decisions': 2,
                'metro_switch_to_desktop': 2,
                'protected_media_identifier': 2,
                'app_banner': 2,
                'site_engagement': 2,
                'durable_storage': 2
            }
        })

        self.driver = webdriver.Chrome(driver_path, options=options)

    def __call__(self, count: int = 0, delay: float = .5):
        self.driver.get(Handler.URL.MAIN)
        if not count:
            count = -1
        while count:
            element = self.driver.find_element_by_class_name('cat-img')
            element.click()

            time.sleep(delay)
            count -= 1

def main(args: argparse.Namespace):
    Handler.Config.DEBUG = args.debug
    Handler.Config.HEADLESS = args.headless

    handler = Handler(args.driver)
    handler(args.count, args.delay)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Auto Cat Click")
    parser.add_argument('--driver', type=str, default='./bin/chromedriver.exe',
                        help="driver path")

    parser.add_argument('--count', type=int, default=0,
                        help="click $count times")
    parser.add_argument('--delay', type=float, default=1.5,
                        help="click $delay")

    parser.add_argument('--debug', action='store_true', default=False,
                        help="driver path")
    parser.add_argument('--headless', action='store_true', default=False,
                        help="headless option")

    args = parser.parse_args()
    main(args)
