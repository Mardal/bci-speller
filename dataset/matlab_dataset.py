# Feel free to refactor/ rewrite all things that I write in this module and package,
# I just want to show my view of Dataset's functionality
from scipy.io import loadmat


class MatlabDataset:
    # TODO: add methods that'll be used by models later
    def __init__(self, src_path, labeled=True):
        # TODO: I'm not quite sure how matlab data will lock like, maybe better approach
        # to load MatlabDataset only from object in code, and provide method like
        # load_matlab(), that'll load matlab from file.
        """
        Creates instance loading data from .mat file
        :param src_file: path to .mat file
        :param is_labeled: if True, append labels from file to object
        """
        self.matobj = self.load_from_file(src_path)
        self.labeled = labeled

        self.set_components()

    def set_components(self):
        self.signals = self.get_signals()
        self.stimuluses = self.get_stimuluses()
        
        if self.labeled:
            self.targets = self.get_targets()

    def load_from_file(self, path):
        # TODO
        return

    def get_signals(self):
        # TODO
        return

    def get_stimuluses(self,):
        # TODO
        return

    def get_targets(self):
        # TODO
        return
