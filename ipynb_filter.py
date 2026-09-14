#!/usr/bin/env python3

# `ipynb_filter.py`:
# This is a git filters that strips out the ai-education-parallel-learning-tools and
# meta data of a Jupyer notebook using `nbconvert`.
# Execute the following line in order to activate this filter:
# python ipynb_filter.py
#
# The following line should be in `.gitattributes`:
# *.ipynb filter=ipynb_filter

from nbconvert.preprocessors import Preprocessor


class RemoveMetadata(Preprocessor):
    pass  # TODO: implement
    def preprocess(self, nb, resources):
        pass  # TODO: implement


if __name__ == "__main__":

else:
