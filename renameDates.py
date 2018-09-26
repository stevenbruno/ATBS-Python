#!/user/bin/env python

# renameDates.py = renames filenames with american MM-DD-YYYY format 
# to european DD-MM-YYYY format.

import shutil
import os
import re

datePattern = re.compile(r"""^(.*?)
                        ((0|1)?\d)-
                        ((0|1|2|3)?\d)-
                        ((19|20)\d\d)
                        (.*?)$
                        """, re.VERBOSE)

