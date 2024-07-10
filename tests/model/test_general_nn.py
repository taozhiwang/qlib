
import unittest

from qlib.contrib.model.pytorch_general_nn import GeneralPTNN
from qlib.data.dataset import DatasetH, TSDatasetH
from qlib.data.dataset.handler import DataHandlerLP
from qlib.tests import TestAutoData


class TestNN(TestAutoData):

    def test_both_dataset(self):
        data_handler_config = {
            "start_time": "2008-01-01",
            "end_time": "2020-08-01",
            "instruments": "csi300",
            "data_loader": {
                "class": "QlibDataLoader",  # Assuming QlibDataLoader is a string reference to the class
                "kwargs": {
                    "config": {
                        "feature": [
                            ["$high", "$close", "$low"],
                            ["H", "C", "L"]
                        ],
                        "label": [
                            ["Ref($close, -2)/Ref($close, -1) - 1"],
                            ["LABEL0"]
                        ]
                    },
                    "freq": "day"
                }
            },
            # TODO: processors
            "learn_processors": [
                {
                "class": "DropnaLabel",
                },
                {
                    "class": "CSZScoreNorm",
                    "kwargs": {
                        "fields_group": "label"
                    }
                }
            ]
        }
        segments = {
            "train": ["2008-01-01", "2014-12-31"],
            "valid": ["2015-01-01", "2016-12-31"],
            "test": ["2017-01-01", "2020-08-01"]
        }
        data_handler = DataHandlerLP(**data_handler_config)

        # time-series dataset
        tsds = TSDatasetH(handler=data_handler, segments=segments)

        # tabular dataset
        tbds = DatasetH(handler=data_handler, segments=segments)
        
        for ds in (tsds, tbds):
            ptnn = GeneralPTNN()
            ptnn.fit(ds)  # It works
            ptnn.predict(ds)  # It works


if __name__ == "__main__":
    unittest.main()