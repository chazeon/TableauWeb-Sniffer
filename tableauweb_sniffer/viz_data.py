import munch
import json
from typing import List


class VizDataDictionary:

    def __init__(self):
        self._segments = {}

    def update(self, segments):
        self._segments.update(segments)
        self.rebuild_values()
    
    def rebuild_values(self):
        self.values = dict()
        for _, segment in sorted((int(key), val) for key, val in self._segments.items()):
            if segment is None: continue
            for dataColumn in segment.dataColumns:
                dataType = dataColumn.dataType
                if dataType not in self.values.keys():
                    self.values[dataType] = []

                self.values[dataType].extend(dataColumn.dataValues)

    def __getitem__(self, key):

        dataType, index = key

        if index < 0:
            dataType = "cstring"
            index = -index - 1
 
        return self.values[dataType][index]