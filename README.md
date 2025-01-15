# ScaleRPy

A Python package for obtaining scaling relationships between two parameters using the 'ridge line' technique. 
Designed for use with global (i.e., integrated) and spatially-resolved astrophysical data. 
This software is compatable with observed and simulated data, facilitating strong quantitative comparisons between studies.

This project and README file are in development.

## Table of Contents
- [Introduction](#introduction)
- [Scientific Motivation](#motivation)
- [Features](#features)
- [Installation](#installation)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Citation](#citation)
- [References](#references)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## Introduction
Scaling relationships are correlations between two (or more) parameters. There are numerous such scaling relationships between properties of galaxies, as well as properties of spatially-resolved elements of galaxies. 

This package contains software for obtaining scaling relationships using the ridge line technique proposed by Renzini & Peng (2015) for the global star formation main sequence ($M_* -$SFR relation). The find_ridge() function identifies the 'ridge' of a 2D distribution. To do so, a kernel density estimate (KDE) is made on the y-axis data in bins of the x-axis paramater. The peaks of the KDEs define the ridge. Users can then specify whether a single or double linear function is fit to the ridge data. This software is modifiable so that ridges can be fit to functions with other shapes. 

The GalDat module features two classes for managing data and identifying scaling relationships, serving as wrappers for the fit_funcs module. The GalDat class is designed for use with global (i.e., integrated) galaxy parameters. SpatGalDat is designed for use with spatially resolved elements. 

## Scientific Motivation
While software for fitting relationships to data are widely available (e.g., scipy.optimize.curve_fit), relationships obtained with these methods are not necessarily broadly comparable. Variations in the source data can result in significant differences between relationships obtained in different studies.

Spatially resolved elements are sometimes referred to as "spaxels" from "spectral pixels," as many observed spatially resolved parameters are derived from integral field spectroscopy, where each pixel has an associated spectra. 

## Features
List the main features of the project.

## Installation
Instructions on how to install the project and its dependencies.

## Examples
Provide additional examples and use cases.

## Contributing
Guidelines for contributing to the project.

## License
Copyright 2025 Bryanne McDonough

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Citation

## References

## Acknowledgements

## Contact
