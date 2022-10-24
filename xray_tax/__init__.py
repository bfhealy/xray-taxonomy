"""
This module contains an X-ray source taxonomy based on Yang et al. (2022, https://arxiv.org/abs/2206.13656).
"""

__version__ = '1.0.0'
__all__ = ["__version__", "taxonomy", "name", "provenance"]

import os
from os.path import join
import yaml
from yaml import FullLoader

tax_path = join(os.path.dirname(__file__), 'xray_source.yaml')

with open(tax_path) as taxonomy_yaml:
    taxonomy = yaml.load(taxonomy_yaml, Loader=yaml.FullLoader)

name = 'X-ray Source Taxonomy'
provenance = 'https://github.com/bfhealy/xray-taxonomy'
