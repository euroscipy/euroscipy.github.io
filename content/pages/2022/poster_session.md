---
title: EuroSciPy 2022 - Spotlight and Poster Session
url: 2022/poster_session.html
save_as: 2022/poster_session.html
section: euroscipy_2022
template: page
slug: poster_session_2022
---

# Spotlight and Poster Session

On Wednesday, a poster session is organized from 3.40 pm to 5 pm. During the
first 40 minutes, each poster presenter will give a 2-minutes spotlight
presentation. These presentations will be followed by a 40 minutes poster
session.

You can find below the list of the poster.

## BioConvert: a comprehensive format converter for life sciences

*thomas cokelaer*

**Abstract:** Life science uses many different formats. They may be old, or with complex syntax and converting these formats may be challenging for scientists. Bioconvert aims to provide a standard tool/interface to convert life science data formats from one to another.

Many conversion tools already exist but they may be dispersed, focused on a few specific formats, difficult to install, or not optimised. With Bioconvert, we plan to cover a wide spectrum of format conversions; we will re-use existing tools when possible and provide an interface to compare different conversion tools or methods via benchmarking. New implementations are provided when considered better than existing ones.

Bioconvert is developed in Python using continuous integration, a test suite and extensive Sphinx documentation. In March 2022, we had 48 formats, 98 direct conversions (125 different methods).

<a href="https://pretalx.com/euroscipy-2022/talk/7SNGMW/"><button type="button" class="btn btn-primary">All details</button></a>


## Sequana: a set of Next Generation Sequencing pipelines

*thomas cokelaer*

**Abstract:** Sequana software is developed within a Sequencing platform at Institut Pasteur. It provides a Python library dedicated to Next Generation Sequencing (NGS) analysis including visualisation of NGS formats.
Sequana is also a project that provides (i) a set of pipelines dedicated to NGS in the form of Snakefiles (Makefile-like with Python syntax based on Snakemake framework), (ii) tools to help in the creation of such pipelines, (iii) a graphical interface for Snakemake framework, (iv) standalone applications for NGS analysis. Pipelines can be run locally or on HPC clusters. Common user interface is provided to ease user interface. These NGS pipelines are ready for production and have been applied on hundreds of projects including Covid variant detection, genomic, transcriptomics, etc

<a href="https://pretalx.com/euroscipy-2022/talk/8JT9QA/"><button type="button" class="btn btn-primary">All details</button></a>


## Conda Store : easy environments management & reproducibility for Teams and Enterprises

*Pierre-Olivier Simonard*

**Abstract:** End users think in terms of environments, not packages. Conda Store makes it easy for data scientists to define their environments, ensures reproducibility, productionizing, easing collaboration, and reduces friction and latency between developers and IT.

<a href="https://pretalx.com/euroscipy-2022/talk/9QBKCE/"><button type="button" class="btn btn-primary">All details</button></a>


## JupyterLab 4 and the future of Jupyter Notebook

*Jeremy Tuloup, Frédéric Collonval*

**Abstract:** JupyterLab is a powerful computational environment for interactive data science in the browser, and the new version 4 release comes with many new features and improvements.

The Jupyter Notebook project decided to base its next major version 7 on JupyterLab components and extensions, which means many JupyterLab features are also available to Jupyter Notebook users.

In this presentation, we will demo all the features coming in these new versions and how users can seamlessly switch from one notebook interface to another.

<a href="https://pretalx.com/euroscipy-2022/talk/ALLCZ7/"><button type="button" class="btn btn-primary">All details</button></a>


## The Beauty of Zarr

*Sanket Verma, Jonathan Striebel*

**Abstract:** This poster showcases Zarr, an open-source data format for storing chunked, compressed N-dimensional arrays. We present a systematic approach to understanding and implementing Zarr by showing how it works and the need for using it. Zarr is based on an open technical specification, making implementations across several languages possible. The focus here is on Zarr’s Python implementation and its interoperability with the existing libraries in the PyData stack.

<a href="https://pretalx.com/euroscipy-2022/talk/APTJNF/"><button type="button" class="btn btn-primary">All details</button></a>


## Scipp plot: modular interactive plotting from graph nodes

*nvaytet*

**Abstract:** We present the plotting framework of the Scipp package (https://scipp.github.io/) for multi-dimensional arrays.
Based on the Model View Controller pattern, it uses a set of nodes connected in a graph to represent a sequence of processing steps that can be applied to the data before plotting it onto the figure axes.
A common example of this could be a 2D scatter plot, accompanied by 1D histograms of the data points on the top and right hand side of the scatter axes.
The histogramming nodes, that lie below the original root data node in the graph, perform a histogram operation in each of the X and Y dimensions, and their results get sent to the top and right plotting axes.

The use of a graph of connected nodes opens up the opportunity for a very modular way of creating interactive plots.
For instance, using a library of widgets (such as ipywidgets), we can change the input to one of the nodes, which notifies all the nodes below it about the change.
This means that modifying a parameter of the scatter data with e.g. a slider, would automatically update not only the main scatter plot, but also the histograms on the sides.

Any function (smoothing, fitting, filtering …) can be used inside a node, and any number of axes (or views) can be attached to a given node. This flexibility allows users to create complicated interactive visualizations with just a few lines of code.

<a href="https://pretalx.com/euroscipy-2022/talk/BAL88N/"><button type="button" class="btn btn-primary">All details</button></a>


## CLAIMED - An open source unified platform for batch, streaming and microservices based data science

*Romeo Kienzler*

**Abstract:** Data are processed in pipelines – either an entire data set, in batches or one by one. A variety of programming languages, frameworks and libraries exists. In CLAIMED – the component library for AI, Machine Learning, ETL and Data Science – we provide an opinionated set of coarse grained components implemented as jupyter notebooks. Through C3, the claimed component compiler those can be (as of now) transformed into Kubeflow Pipeline Components, Airflow Operators or simple (docker) container images to be executed on Knative. An adapter implemented as side car transforms those into either streaming components (currently http(s) and Kafka) or micro services – with scale to zero support. Using the jupyter lab Elyra pipeline editor and CLAIMED, anybody can create data science pipelines without programming skills. But the source code is only one click away. The jupyter notebook backing the component is available for review, adjustments or improvements of the components.

<a href="https://pretalx.com/euroscipy-2022/talk/BZDJXH/"><button type="button" class="btn btn-primary">All details</button></a>


## Python in Storm

*Soundharya Khanapur*

**Abstract:** The advancement and development in the field of Technology and Communication call for a need for Real-time data processing that is fast and fault-tolerant. Apache Storm provides an epoch platform to develop applications that can process a multitude of data in real-time. Being distributed, Storm is predominantly fast and maintains high accuracy with its topological analysis and task completion checks.

<a href="https://pretalx.com/euroscipy-2022/talk/GMBXCA/"><button type="button" class="btn btn-primary">All details</button></a>


## Informative and pleasant dataviz with Raincloud plot

*Davide Poggiali*

**Abstract:** Categorical plots offer a variety of plotting styles that allows the user to picture even large datasets showing some summary statistics of the data. In some case graphs can be misleading, either unwilling or on purpose. The reader can be confused or even get an incorrect idea of the phenomenon underlying the data.
In this talk we introduce the Raincloud plot, a multi-language plotting style aimed to create charming and informative graphical representations of a dataset. After some introduction, we will offer a simple tutorial that will cover different use cases. We will then compare the Raincloud plots with some other plot styles, showing that some data misunderstanding can be avoided with a sufficiently detailed plot.

<a href="https://pretalx.com/euroscipy-2022/talk/KWFH9N/"><button type="button" class="btn btn-primary">All details</button></a>


## Renku-Python: Reproducible and Reusable Workflows

*Ralf Grubenmann*

**Abstract:** Renku is a platform that bundles together various tools for reproducible and collaborative data analysis projects. Here we take a deep dive into the Python CLI and library component of the Renku platform, highlighting its functionality for recording and executing workflows both locally and remotely, as well as its architecture for storing recorded metadata in a knowledge graph and how this can be extended by third-party plugins.

<a href="https://pretalx.com/euroscipy-2022/talk/PFQPTF/"><button type="button" class="btn btn-primary">All details</button></a>


## dirty_cat : a Python package for Machine Learning on Dirty Categorical Data

*Lilian Boulard*

**Abstract:** In this talk, we will introduce "dirty_cat", a Python library for encoding dirty, non-curated categorical features into numerical features while preserving similarities.
We will focus on a few methods implemented in the similarity encoder, the Gamma-Poisson encoder, the min-hash encoder and the super-vectorizer.

<a href="https://pretalx.com/euroscipy-2022/talk/PRYDKM/"><button type="button" class="btn btn-primary">All details</button></a>


## Scipp: Multi-dimensional data arrays with labeled dimensions for dense and binned data

*Simon Heybrock*

**Abstract:** Inspired by Xarray, Scipp (https://scipp.github.io/) enriches raw NumPy-like multi-dimensional arrays of data by adding named dimensions and associated coordinates. For an even more intuitive and less error-prone user experience, Scipp furthermore adds physical units to arrays and their coordinates. Scipp data arrays additionally support a dictionary of masks, basic propagation of uncertainties, and bin-edge coordinates.

On top of the above, Scipp's key feature is support for multi-dimensional non-destructive binning of record-based "tabular" data into arrays of bins. The use of labeled arrays with coordinates to represent the table of records allows for clear conceptual association of a record's metadata with dimensions and coordinates of the array of bins. Based on this, Scipp can provide fast, flexible, and efficient binning, rebinning, and filtering operations, all while preserving the original individual records.

Scipp ships with data display and visualization features for Jupyter notebooks, including a powerful plotting interface.

<a href="https://pretalx.com/euroscipy-2022/talk/RANUF3/"><button type="button" class="btn btn-primary">All details</button></a>


## ReservoirPy: Efficient Training of Recurrent Neural Networks for Timeseries Processing

*Xavier Hinaut*

**Abstract:** ReservoirPy is a simple user-friendly library based on Python scientific modules. It provides a flexible interface to implement efficient Reservoir Computing (RC) architectures with a particular focus on Echo State Networks (ESN). Advanced features of ReservoirPy allow to improve computation time efficiency on a simple laptop compared to basic Python implementation, with datasets of any size.

Some of its features are: offline and online training, parallel implementation, sparse matrix computation, fast spectral initialization, advanced learning rules (e.g. Intrinsic Plasticity) etc. It also makes possible to easily create complex architectures with multiple reservoirs (e.g. deep reservoirs), readouts, and complex feedback loops. Moreover, graphical tools are included to easily explore hyperparameters with the help of the hyperopt library. It includes several tutorials exploring exotic architectures and examples of scientific papers reproduction. Moreover, graphical tools are included to easily explore hyperparameters with the help of the hyperopt library. ReservoirPy is available on GitHub https://github.com/reservoirpy/reservoirpy with the open source MIT license, it includes a detailed documentation https://reservoirpy.readthedocs.io and a pypi package for easy installation.

<a href="https://pretalx.com/euroscipy-2022/talk/S7NHQE/"><button type="button" class="btn btn-primary">All details</button></a>


## pyLife – a python package for mechanical lifetime assessment

*Johannes Mueller*

**Abstract:** pyLife is a Python package covering state of the art algorithms of mechanical lifetime assessment and material fatigue. In this talk we will see a very quick glance of mechanical lifetime estimation and how we can combine classical methods from mechanical engineering with methods from data science. We will see how pyLife's modules can be used to build versatile solutions for the engineer's desktop as well as server based solutions for manufacturing and quality assurance with a high degree of automation. As pyLife is an Open Source project, everyone is welcome to collaborate. We are curious if we can establish a developer community in the realm of mechanical engineering. We are aiming especially towards university teachers using pyLife for teaching and research purposes.

<a href="https://pretalx.com/euroscipy-2022/talk/WBLY9B/"><button type="button" class="btn btn-primary">All details</button></a>


## napari: a multi-dimensional image visualization, annotation, and analysis platform in Python

*Kevin Yamauchi*

**Abstract:** Napari is an interactive, GPU-accelerated, nD image viewer written in python. It displays images in a 2D or 3D canvas, then provides sliders for any additional dimensions in a dataset. It can also overlay associated data such as segmentations, points, polygons, surfaces, vectors, and tracks. Finally, napari is well-integrated with the scientific python ecosystem: NumPy arrays are the primary data structure used for visualization, and other standard arrays (such as Zarr or Dask arrays) are also supported. This makes it easy to insert interactive visualization, curation, and annotation steps into any workflow using standard SciPy libraries such as NumPy, SciPy, dask, and scikit-image. In this talk, I will introduce napari and demonstrate how napari can be used for interactive image analysis.

<a href="https://pretalx.com/euroscipy-2022/talk/ZPLK87/"><button type="button" class="btn btn-primary">All details</button></a>
