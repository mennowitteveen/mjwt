# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_utils.ipynb.

# %% auto 0
__all__ = ['legimplot']

# %% ../nbs/00_utils.ipynb 4
import pickle
import inspect
from sys import getsizeof
from collections import defaultdict
from IPython.display import Audio, display, Javascript
from IPython import get_ipython
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.colors as mcolors

def legimplot(arg):
    print(arg)
    return 'fun'
# def legimplot(M, show=True, cmap=None, interpolation='none', title=None, figsize=None, **kwargs):
#     if title is None:
#         #title = find_varname(M) # so so..
#         frame = inspect.getouterframes(inspect.currentframe())[1]
#         string = inspect.getframeinfo(frame[0]).code_context[0].strip()
#         args = string[string.find('(') + 1:-1].split(','); names = []
#         for i in args:
#             if i.find('=') != -1:
#                 names.append(i.split('=')[1].strip())
#             else:
#                 names.append(i)    
#         title = names[0]
    
#     # Determining plot aspect ratios and figsizes:
#     aspect = 'auto' if (('aspect' not in kwargs.keys()) & (figsize is not None)) else defaultdict(lambda:None,kwargs)['aspect']
#     if figsize is not None: plt.figure(figsize=figsize)
#     if aspect == 'auto': title = title + ', aspect=\'auto\''
        
#     # Do the plot:
#     plt.imshow(M, cmap=cmap, aspect=aspect, interpolation=interpolation); plt.colorbar(); plt.title(title); 
#     if show: plt.show() #optional .show supression
