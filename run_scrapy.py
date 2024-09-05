
# Call the interface to run scrapy
from data_scrapy.scrapy_graph import ScrapyGraph


def run_scrapy(url, prompt, *args, **kwargs):
    """
    start scrapy
    :param url:
    :param prompt:
    :return:
    """
    result = ScrapyGraph(prompt=prompt, url=url).execute_gragh()
    print(result)

if __name__ == '__main__':
    info = {
        "url": "https://www.cdgoufangtong.com/",
        "prompt": "What is the real-time number of commercial housing units sold today?"
    }
    run_scrapy(url=info.get("url"), prompt=info.get("prompt"))

