# basic graph data structures

# define node
class Node:
    def __init__(self, node_id, node_type, metadata, node_func, result=None):
        self.node_id = node_id
        self.node_type = node_type
        self.metadata = metadata
        self.edges = []
        self.node_func = node_func
        self.result = result

# define edge
class Edge:
    def __init__(self, source, target, edge_type, weight=1):
        self.source = source
        self.target = target
        self.edge_type = edge_type
        self.weight = weight

# define graph
class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node):
        self.nodes[node.node_id] = node

    def add_edge(self, edge):
        self.edges.append(edge)
        edge.source.edges.append(edge)

    def _topological_sort_util(self, node, visited, stack):
        visited.add(node.node_id)
        for edge in node.edges:
            if edge.target.node_id not in visited:
                self._topological_sort_util(edge.target, visited, stack)
        stack.append(node)

    async def execute_task(self):
        visited = set()
        stack = []

        # 从每个节点开始进行拓扑排序
        for node in self.nodes.values():
            if node.node_id not in visited:
                self._topological_sort_util(node, visited, stack)

        # 反转栈以获得正确的执行顺序
        result = ""
        while stack:
            node = stack.pop()
            self._execute_node(node)
            # if node.result is None:
            #     node_result = node.node_func(0)
            # else:
            #     node_result = node.node_func(node.result)
            node_result = await node.node_func(node.result)
            for edge in node.edges:
                edge.target.result = node_result
            result = node_result
        return result


    def _execute_node(self, node):
        print(f"Executing task: {node.node_type} with metadata: {node.metadata}")


def global_auto_increment():
    global global_node_id
    global_node_id += 1
    return global_node_id


async def node_func_example(auto_number, *args, **kwargs):
    """
    node func example
    :param auto_number:
    :return:
    """
    auto_number = auto_number + 1
    print(f"The increment number is {auto_number}")
    return auto_number

# def node_func_example(auto_number, *args, **kwargs):
#     """
#     node func example
#     :param auto_number:
#     :return:
#     """
#     auto_number = auto_number + 1
#     print(f"The increment number is {auto_number}")
#     return auto_number


if __name__ == '__main__':
    global_node_id = 0
    # 多节点示例用法
    graph = Graph()
    node1 = Node(node_id=global_auto_increment(), node_type='Split', metadata={'content': 'task splitting'},
                 node_func=node_func_example, result=0)
    node2 = Node(node_id=global_auto_increment(), node_type='Crawl', metadata={'content': 'content web crawling'},
                 node_func=node_func_example)
    node3 = Node(node_id=global_auto_increment(), node_type='Analysis', metadata={'content': 'content analysis'},
                 node_func=node_func_example)
    node4 = Node(node_id=global_auto_increment(), node_type='Merge', metadata={'content': 'merge output'},
                 node_func=node_func_example)

    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)
    graph.add_node(node4)

    edge1 = Edge(source=node1, target=node2, edge_type='split_crawl')
    edge2 = Edge(source=node2, target=node3, edge_type='crawl_analysis')
    edge3 = Edge(source=node3, target=node4, edge_type='analysis_merge')

    graph.add_edge(edge1)
    graph.add_edge(edge2)
    graph.add_edge(edge3)
    print(f"see new graph is: {graph}")

    import asyncio
    # 执行任务
    asyncio.run(graph.execute_task())
