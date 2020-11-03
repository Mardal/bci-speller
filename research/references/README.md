# content
This directory contains links to projects/ code that can be useful in research or reused directly
You can find list of saved sources below, also we add lonk to source for every added file

# links

## Recording and processing EEG
1. [The Lab Streaming Layer (LSL)](https://github.com/sccn/labstreaminglayer)

    Probably useful tool for data acquisition
    *from docs*: "system for the unified collection of measurement time series in research experiments that handles both the
    networking, time-synchronization, (near-) real-time access as well as optionally the centralized collection,
    viewing and disk recording of the data."

2. [BCI2000](https://www.bci2000.org/)

    Widely used tool for data acquisition, visualisations etc.

3. [EEGLab](https://sccn.ucsd.edu/eeglab/index.php)

    MATLAB-based toolbox for processing of EEG etc.

4. [BCILab](https://sccn.ucsd.edu/eeglab/index.php)

    IDK where's difference with previous toolbox, but they were developed in same place.
    Just check it out, maybe it'll be useful.

## Models and data
1. [BCI challenge 2015](https://www.kaggle.com/c/inria-bci-challenge/)

    Kaggle competition with code to train binary classifier and discussions with code

    Simple baselines:
    * [Random Forest](https://www.kaggle.com/c/inria-bci-challenge/discussion/11009)
    * [Gradient Boosting](https://www.kaggle.com/c/inria-bci-challenge/discussion/11056)

2. [BCI competition III](http://www.bbci.de/competition/iii/)

    Competition from 2004 with plenty interesting datasets

3. [Manucar's repo p300 speller](https://github.com/Manucar/p300-speller)

    Contains notebook with complete pipeline from loading .mat data from 2nd dataset of BCI competition III to writing
    file with test predictions

4. [EEGNet architecture](https://github.com/aliasvishnu/EEGNet)

    Repo with EEGNet notebook and architecture schema

5. [ARL EEGModel project](https://github.com/vlawhern/arl-eegmodels)

    Some simple pytorch CNN models for EEG

6. [BNCI horizon](http://bnci-horizon-2020.eu/database/data-sets)
    A LOT of datasets, be sure to check this out!

7. [Zuhairmhtb's repo about EEG](https://github.com/zuhairmhtb/P300SpellerBasedEEGClassification)
    EEG classifier based on BNCI horizon dataset, looks deep and useful at first glance

8. [Write with our mind](https://github.com/Borda/BCI-speller)
    Cool app with bci-keyboard based on blinking (as I understood)
    Worth to check full app architecture to learn how to build ours!