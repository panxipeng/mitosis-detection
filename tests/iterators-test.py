# Fix Import
# from test import root_path
# Actual Imports
import os
from src.utilities import TT
from src.iterators import BatchGenerator, Dataset, ImageIterator
from src.dataset import icpr2012

root = os.getcwd()

# 1. Test BatchGenerator
# flt, mapper = icpr2012()
TT.verbose = True
# batches = BatchGenerator(Dataset(root+'/datasets/ICPR 2012/testing/set1', mapper=mapper, filename_filter=flt), 1000, 500)
# for batch in batches:
#     continue

batches = BatchGenerator(ImageIterator(root + '/tests/patch_at/utilities.tiff', root + '/tests/patch_at/utilities.csv'),
                         batch_size=1000)
for batch in batches:
    continue
