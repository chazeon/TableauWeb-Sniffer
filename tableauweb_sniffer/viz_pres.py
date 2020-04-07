import munch, json
from collections import OrderedDict
from .viz_data import VizDataDictionary

class VizDataPresentation:

    def __init__(self, store, data):
        self._data = data
        self._store = store
        self._paneColumnsData = self._data.paneColumnsData
        self._vizDataColumns = self._paneColumnsData.vizDataColumns
        self._paneColumnsList = self._paneColumnsData.paneColumnsList
    
    @property
    def tupleIds(self):
        return [
            self._paneColumnsList[paneIndex].vizPaneColumns[columnIndex].tupleIds
            for paneIndex, columnIndex in zip(
                self._vizDataColumns[0].paneIndices,
                self._vizDataColumns[0].columnIndices
            )
        ]

    def retrieveTuples(self):
        for i, tupleIds in enumerate(self.tupleIds):
            for j, _ in enumerate(tupleIds):

                tup = OrderedDict()

                for dataColumn in self._vizDataColumns[1:]:

                    dataType = dataColumn.dataType
                    try:
                        paneIndex = dataColumn.paneIndices[i]
                        columnIndex = dataColumn.columnIndices[i]
                    except Exception:
                        continue

                    aliasIndex = self._paneColumnsList[paneIndex].vizPaneColumns[columnIndex].aliasIndices[j]

                    tup[dataColumn.fn] = {
                        "type": dataType,
                        "value": self._store[dataType, aliasIndex]
                    }

                yield tup
