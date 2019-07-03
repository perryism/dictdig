from .extractor_strategy import ExtractorStrategy

class DictDig:
    def __init__(self, dict_obj):
        self.dict_obj = dict_obj

    def dig(self, path, default=None):
        current_node = self.dict_obj
        for node_name in path.split("."):
            strategy = ExtractorStrategy.strategy(node_name)
            current_node = strategy.extract(current_node)
            if current_node is None:
                return default

        if current_node is None:
            return default
        else:
            return current_node
