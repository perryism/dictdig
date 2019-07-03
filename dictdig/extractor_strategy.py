from .name_extractor import NameExtractor
from .list_extractor import ListExtractor

import re

class ExtractorStrategy:
    @staticmethod
    def strategy(partial_path):
        if re.search('(?<=\[)\d+(?=])', partial_path):
            return ListExtractor(partial_path)
        else:
            return NameExtractor(partial_path)
