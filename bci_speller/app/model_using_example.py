from bci_speller import datasets, models


def example_train_model():
    """
    Implements example pipeline of work with datasets and models
    :return:
    """
    data = app_record_data()
    dataset = datasets.MatlabDataset(data)
    model = models.FFNN()
    model.train(dataset)
    model.dump()


def example_use_model():
    model = models.FFNN.load_latest()
    calibration_records = app_record_data()
    calibration_dataset = datasets.MatlabDataset(calibration_records)

    model.calibrate(calibration_dataset)

    while True:
        letter_eeg = app_record_data()
        letter_dataset = datasets.MatlabDataset(letter_eeg, labeled=False)  # letter_eeg has no ground-truth letter
        predicted_letter = model.predict(letter_dataset)
        app_show_predicted(predicted_letter)


def app_record_data():
    """It's just method for examples to show that app gets data, somehow and somewhere.
    Realization of obtaining data depends on app's code"""
    pass


def app_show_predicted(letter):
    pass