
# use selenium to get web html
import logging
import time
import asyncio

from playwright.async_api import async_playwright


class FetchContent:

    def __init__(self):
        pass


    # def get_web_page(self, url):
    #     self.driver.get(url)
    #     web_title = self.driver.title
    #     logging.info(f"Page title is: {web_title}")
    #     time.sleep(5)
    #     web_page = self.driver.page_source
    #     # save to html
    #     temp_timestamp = int(time.time()*1000)
    #     web_file_name = f'{temp_timestamp}_web_page.html'
    #     with open(web_file_name, 'w', encoding='utf-8') as file:
    #         file.write(web_page)
    #     logging.info("The web content has been saved normally")
    #     return web_file_name

    async  def fetch_and_save_html(self, url):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await  browser.new_page()

            await page.goto(url)

            content = await page.content()
            temp_timestamp = int(time.time() * 1000)
            web_file_name = f'{temp_timestamp}_web_page.html'
            with open(web_file_name, 'w', encoding='utf-8') as file:
                file.write(content)

            logging.info("The web content has been saved normally")
            await  browser.close()
            return web_file_name







