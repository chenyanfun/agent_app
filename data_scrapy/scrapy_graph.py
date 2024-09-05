
# define scrapy graph
import asyncio

from data_structures.basic_graph import Graph
from data_structures.basic_node import Node
from data_structures.basic_edge import Edge
from data_scrapy.fetch_web_content import FetchContent
from data_scrapy.analysis_data import AnalysisData
from data_scrapy.output_data import output_result


class ScrapyGraph(object):

    def __init__(self, prompt, url):
        self.prompt = prompt
        self.url = url
        self.global_node_id = 0
        self.scrapy = FetchContent()
        self.analysis = AnalysisData(prompt=self.prompt)
        self.node_init()
        self.edge_init()
        self.graph_init()

    def auto_increment_id(self):
        self.global_node_id += 1
        return self.global_node_id


    def node_init(self):
        """
        define node
        :return:
        """
        self.crawl_node = Node(node_id=self.auto_increment_id(), node_type='crawl', metadata={"url": self.url},
                          node_func=self.scrapy.fetch_and_save_html, result=self.url)
        # save_node = ''
        self.analysis_node = Node(node_id=self.auto_increment_id(), node_type='analysis',
                             metadata={"prompt": self.prompt}, node_func=self.analysis.analysis_content)
        self.output_node = Node(node_id=self.auto_increment_id(), node_type='output',
                                metadata={}, node_func=output_result)

    def edge_init(self):
        """
        define edge
        :return:
        """
        self.crawl_analysis_edge = Edge(source=self.crawl_node, target=self.analysis_node, edge_type="crawl_analysis")
        self.analysis_output_edge = Edge(source=self.analysis_node, target=self.output_node, edge_type="analysis_output")

    def graph_init(self):
        self.graph = Graph()
        self.graph.add_node(self.crawl_node)
        self.graph.add_node(self.analysis_node)
        self.graph.add_node(self.output_node)
        self.graph.add_edge(self.crawl_analysis_edge)
        self.graph.add_edge(self.analysis_output_edge)
        # return graph

    def execute_gragh(self):
        asyncio.run(self.graph.execute_task())
