# agent-app

describe: Practical application scenarios of large models, including automatic crawlers, engineering of proprietary large models, engineering of proprietary deep learning models, etc. The project is under stable development and maintenance

## Automatic crawler

* Reference code：https://github.com/ScrapeGraphAI/Scrapegraph-ai
* Implementation principle：Use palywright and opanai to implement, playwright to automatically crawl web pages, and use openai to extract data content through prompt
* Preparation for operation：
  * ```pip install -r requirement.txt```
  * ```playwright install```
  * modify the configuration file ```conf/config_info.yaml ```, Enter your api_key and select model
  * Writing Test Code,eg:
```python

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


```



