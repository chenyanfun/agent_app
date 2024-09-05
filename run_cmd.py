# The entry function selects the required application
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Please select the application you need")
    parser.add_argument("--choose_app", type=str, default="ai_scrapy")

    pass