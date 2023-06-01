def get_release(self):
    import requests

    res = requests.head("http://su13/outbreak/significance/gr_sigs.csv.gz")
    return res.headers["Last-Modified"]
