#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2021-S1-MX-5"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['NGC6946'] = [100632, 100633 ]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['NGC6946']   = ""

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['NGC6946']   = "pix_list=-0,5  srdp=1 sdfits=1 admit=0"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, sys.argv)
