import os

from biothings.utils.dataload import tabfile_feeder


def load_data(data_folder):
    json_path = os.path.join(data_folder, "gr_sigs.csv")
    records = tabfile_feeder(json_path, sep=",")
    doc_keys = ["loc", "lin", "leaf", "snr", "growing", "sig"]
    for record in records:
        doc = {}
        for i, key in enumerate(doc_keys):
            if key in ["growing", "leaf"]:
                doc[key] = record[i].lower()
            else:
                doc[key] = record[i]
        doc["_id"] = doc["loc"] + "_" + doc["lin"]
        yield doc


def custom_data_mapping(cls):
    return {
        "growing": {"type": "boolean"},
        "leaf": {"type": "boolean"},
        "lin": {"type": "keyword"},
        "loc": {"type": "keyword"},
        "sig": {"type": "double"},
        "snr": {"type": "double"},
    }
