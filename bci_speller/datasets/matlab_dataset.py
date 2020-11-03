"""eel free to refactor/ rewrite all things that I write in this module and package,
I just want to show my view of Dataset's functionality"""
from scipy.io import loadmat


class MatlabDataset:
    # TODO: add methods for models
    def __init__(self, matobj, labeled=True):
        """
        :param src_file: path to .mat file
        :param is_labeled: if True, append labels from file to object
        """
        self.matobj = matobj
        self.labeled = labeled

        self.set_components()

    def set_components(self):
        # TODO
        return

    def load_from_file(self, path):
        # TODO
        return
