# -*- coding: utf-8 -*-
"""
Hack for djaml, library not supported django 1.4
"""

from django.template.loaders import filesystem, app_directories
from djaml.loaders import get_haml_loader

DjamlFilesystemLoader = get_haml_loader(filesystem)
DjamlAppDirectoriesLoader = get_haml_loader(app_directories)