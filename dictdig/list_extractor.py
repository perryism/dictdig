import re
from .name_extractor import NameExtractor

class ListExtractor:
    def __init__(self, partial_path):
        self.node_name = self.__get_node_name(partial_path)
        self.partial_path = partial_path

    def extract(self, node):
        for i, ind in  enumerate(self.__get_index(self.partial_path)):
            if i == 0:
                match = NameExtractor(self.node_name).extract(node)

            match = match[ind]

        return match

    def __get_node_name(self, partial_path):
        return partial_path.split('[')[0]

    def __get_list_index(self, partial_path):
        match = re.search('(?<=\[)\d+(?=])', partial_path)
        if match:
            return int(match.group())

    def __get_index(self, partial_path):
        matches = re.findall('(?<=\[)\d+(?=])', partial_path)
        return [ int(match) for match in matches ]
