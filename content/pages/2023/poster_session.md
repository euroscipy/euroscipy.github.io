---
title: EuroSciPy 2023 - Spotlight and Poster Session
url: 2023/poster_session.html
save_as: 2023/poster_session.html
section: euroscipy_2023
template: page
slug: poster_session_2023
---

# Spotlight and Poster Session

On Wednesday, a poster session is organized from 4.15 pm to 5.30 pm.
It will be preceded by a spotlight session taking place in Aula room.

You can find below the list of the poster.

## Predictive survival analysis and competing risk modeling with Gradient Boosted CIF

*Vincent Maladiere*

**Abstract:** This tutorial is an introduction to our new survival analysis estimator called Gradient Boosted CIF. This model predicts cumulative incidence functions (CIF) in competing risk settings by leveraging scikit-learn's HistGradientBoostingClassifier.

<a href="https://pretalx.com/euroscipy-2023/talk/8NHQGJ/"><button type="button" class="btn btn-primary">All details</button></a>


## PyBAMM, an open-source Python package for battery simulation, contributes to a solid understanding of lithium-ion batteries degradation

*Maria Kaninia*

**Abstract:** Being able to predict the degradation (capacity and power fade) of lithium-ion batteries is critical for the procurement and asset management of batteries. Often, this exercise is undertaken using empirical or semi-empirical models, which blend out the degradation mechanisms in favour or computational speed and simplicity.

By using PyBaMM (an open source package for battery simulation), we build bottom-up understanding of the discrete ageing mechanisms that impact battery State-of-Health indicators. In addition, PyBaMM comes complete with validated sets of parameters for different chemistries, which accelerates the deployment of the model.

<a href="https://pretalx.com/euroscipy-2023/talk/A8BJLV/"><button type="button" class="btn btn-primary">All details</button></a>


## scicode-widgets: A toolkit to bring computational thinking into the classroom

*Alexander Goscinski*

**Abstract:** We introduce scicode-widgets, a Python package designed for educational purposes that facilitates the creation of interactive exercises for students in interdisciplinary fields of computational sciences. The implementation of computational experiments often demands extensive coding, hindering students' ability to effectively learn the interwork of coding experiments and analyzing their results. To reduce this workload for students, instructors can already provide a codebase and demand educational contributions from students. These contributions have to be embedded into a general workflow that involves coding experiments and analyzing their results. For that task scicode-widget provides the tools to connect custom pre- and postprocessing of students’ code, with the ability to verify the solution and to pass it to interactive visualizations driven by jupyter widgets. In the talk we demonstrate an example from a materials science class for teaching atomistic modeling and discuss a potential direction to integrate with nbgrader.

<a href="https://pretalx.com/euroscipy-2023/talk/ALH9X8/"><button type="button" class="btn btn-primary">All details</button></a>


## Molgri: grids for molecular dynamics

*Hana Zupan*

**Abstract:** Computational chemistry studies how molecules approach and interact at atomic precision and femtosecond timescales, a level of detail that is difficult to achieve in experiments. This enables us to understand important processes like the binding of drugs to receptors.

However, especially the first phase of binding – the approach and guidance towards a binding site - is difficult to study with the usual molecular dynamics approach. In the python package molgri, we instead create two sets of grids to study binding pathways. A grid of approach directions is generated based on a subdivision of an icosahedron; a grid of approach orientations based on a division of a half-hypercube.

After the user provides two molecular structures and the desired level of discretization, the molgri package generates a sequence of structures (a pseudo-trajectory) featuring all combinations of approach directions, distances and orientations. The output is immediately compatible with chemical software like GROMACS and openMM, so that this grid-based approach can be used as a starting point for simulations or used on its own to study long-range interactions guiding ligands to binding sites and to extract simulation-free models of kinetics (rate matrix).

The ease of use is taken into account during development; the generation of pseudo-trajectories can be easily done as a single command-line instruction, with examples provided in documentation.

<a href="https://pretalx.com/euroscipy-2023/talk/FQSXE7/"><button type="button" class="btn btn-primary">All details</button></a>


## Streamlining Geospatial Machine Learning with SRAI

*Szymon Woźniak, Piotr Szymański, Piotr Gramacki, Kamil Raczycki, Kacper Leśniara*

**Abstract:** This talk will introduce the audience to the Spatial Representations for Artificial Intelligence (srai), a Python library that provides an efficient, unified, and easy-to-use approach to geospatial problems. Attendees will get insights into the key functionalities and use cases of srai with a focus on how it enhances the Python scientific stack and encourages the application of Python in scientific and industrial geospatial research.

<a href="https://pretalx.com/euroscipy-2023/talk/GRHSGN/"><button type="button" class="btn btn-primary">All details</button></a>


## SciPy❤Java with GraalPy

*Tim Felgentreff, Cosmin Basca*

**Abstract:** GraalPy brings up to date data science packages from Python to Java. Whether
analyzing data from Java enterprise applications or embedding Python
visualizations in Java's cross-platform UIs, GraalPy makes it easier than ever.
In this talk we will show you how to get GraalPy from Conda or Pyenv, how it
performs on scientific Python workloads, and how to easily set up a
multi-language application with Java, Pygal, and SciPy.

<a href="https://pretalx.com/euroscipy-2023/talk/GSKSQJ/"><button type="button" class="btn btn-primary">All details</button></a>


## RNA-seq data normalization in Python

*Jure Zmrzlikar*

**Abstract:** Gene expression is commonly measured using RNA sequencing. In a nutshell, bioinformatic analysis includes aligning sequencing reads to a reference genome and counting expression as the number of reads per gene or transcript. Normalization of gene counts is important for accurate interpretation and downstream analysis, and the widely used methods like TPM and RPKM make us believe that RNA-seq normalization is a solved problem. This poster will present some alternatives and discuss why there may be more suitable ways of transforming gene expression counts for machine learning applications.

We developed [RNAnorm](https://github.com/genialis/rnanorm), an RNA-seq data normalization toolkit in Python. This open-source package (re-)implements a range of normalization methods including CPM, FPKM, TPM, TMM, UQ, CUF, and CTF. The code architecture is compatible with scikit-learn’s fit and transform interface, allowing users to rapidly prototype normalization strategies and assess their impact on model performance.

The poster will present the theoretical background of the methods from the perspective of the bias they address (i.e. library size, gene length, RNA composition) and their respective strengths and weaknesses. It will also showcase the usage od RNAnorm package to perform various normalization tasks: from simple one-line normalization to a more complex grid search to find the best combination of normalizations for a given machine learning problem.

<a href="https://pretalx.com/euroscipy-2023/talk/JBUYJL/"><button type="button" class="btn btn-primary">All details</button></a>


## scverse: Foundational tools for single-cell omics analysis

*Isaac Virshup*

**Abstract:** scverse (scverse.org) is a consortium of core Python tools for storage and analysis of high-dimensional single-cell data. These tools provide scalable infrastructure for hundreds of dependent packages and have been used to study the human immune system, aging, and COVID-19. The consortium provides a continued maintenance plan, community platforms, and organization for the hubs of our research software ecosystem. We will introduce scverse and present ongoing work addressing scalability, spatial omics, and community building.

<a href="https://pretalx.com/euroscipy-2023/talk/NPNXNA/"><button type="button" class="btn btn-primary">All details</button></a>


## Runtime-Control of Numerical Groundwater Models

*Mike Müller, Lúcia Pedrosa*

**Abstract:** The widely-used finite volume groundwater flow and transport model MODLFOW 6 is implemented in Fortran. The typical work flow consists of the steps (1) pre-processing on input data, (2) running the model, and (3) post-processing of model results. For a variety of problems this workflow has to be applied repeatedly, modifying values of input data based on modeling results  The here presented tool `pymf6` enables the model user to access intermediate model results at runtime and modifying model variables with Python. This allows to greatly reduce the number of model runs. Often, one model run can replace many manual iterations, leading to a much faster workflow. Furthermore, complex tasks that would not be feasibly with the manual workflow can be solved. `pymf6` can also be used to couple MODLFOW 6 with other numerical or analytical models.

<a href="https://pretalx.com/euroscipy-2023/talk/P39VK3/"><button type="button" class="btn btn-primary">All details</button></a>


## Automating data collection and analysis in citizen science projects

*Dimitrios Ladakis*

**Abstract:** Citizen science is a powerful tool used by scientists in a wide range of fields to aid the utilisation of scientific data, that would otherwise take a very long time to process and analyse, while being an important way to engage with the public. RFI has a number of citizen science projects, under the name ‘Science Scribbler’, for collecting annotation data from biological 3D imaging techniques. Annotated data can be used to guide segmentation from images in order to understand morphological features at the cellular level in health and disease. To support current citizen science projects, and to facilitate planning of future ones, automating the way images are generated and annotation data is processed is of major importance. A web tool for on-the-fly image generation from 3D volumes of data is being created to provide an easy way to generate images for annotation by volunteers via the Zooniverse citizen science platform, but also to allow minimisation of storage space requirements. Furthermore a library for automating data processing and analysis is in construction that can be used as a pipeline to extract, pool, visualise, filter and prepare annotation data for segmentation and other types of analysis.

<a href="https://pretalx.com/euroscipy-2023/talk/P9E7HX/"><button type="button" class="btn btn-primary">All details</button></a>


## Writing tests for your containers with Container Canary

*Jacob Tomlinson*

**Abstract:** When we write code we also write tests to ensure that our software functions as expected. But with containers, it is far more common to document assumptions and leave it at that.

Containers are the building blocks of modern compute platforms and they have interfaces like any other software. The software they contain, commands they run and ports they listen on all make up that interface and when composed into larger systems many assumptions are made about how containers will behave. So we should test that!

Container Canary is a black-box testing tool for container images and in this talk, we will talk about why you should test your containers, how to write canary test manifests and how to use the canary CLI tool to run them.

<a href="https://pretalx.com/euroscipy-2023/talk/RLJETB/"><button type="button" class="btn btn-primary">All details</button></a>


## skrub: preparing tables for machine learning

*Jovan Stojanovic*

**Abstract:** Are you wondering what to do with all of the tables you have?
And how to make sense of all of the dirty data?

Data science is increasingly faced with multiple-sourced, non-standardized dirty tables.

We have what you need: skrub is a Python package for preparing your dirty tables for machine learning!

dirty-cat evolves into skrub and gives you the right tools to clean, transform and join your tables for machine learning.

<a href="https://pretalx.com/euroscipy-2023/talk/SCLBPU/"><button type="button" class="btn btn-primary">All details</button></a>


## From ab-initio to scattering experiments: A Python workflow for constructing neuroevolution potentials

*Eric Lindgren*

**Abstract:** Computer simulations such as Molecular Dynamics (MD) are an effective tool in studying a broad range of structural and dynamical properties in atomic-scale systems, but the connection to X-ray or neutron scattering experiments is not always straightforward.
In this work, we present a Python workflow that starts with the construction of machine learned potentials and ends with the prediction of experimental observables, such as the dynamical structure factor.
Specifically, the Python package `Calorine` is used to train neuro-evolution potentials (NEP) with ab-initio level accuracy using the software package `GPUMD`, whilst still retaining a familiar interface based around the Python framework `ASE`.
The trained potentials are then used to run MD within GPUMD, also done through `Calorine`.
Finally, the resulting MD trajectories are analyzed with the Python package `Dynasor` in order to calculate dynamical structure factors, which in turn may be convoluted with instrument parameters in order to compare to experiments.
We apply our workflow to crystalline benzene as a prototype system, but the workflow may be readily extended to different systems.

<a href="https://pretalx.com/euroscipy-2023/talk/XPHSMW/"><button type="button" class="btn btn-primary">All details</button></a>


## MLEES - An Initial Guide through the Thickets of Machine Learning Research in Earth and Environmental Sciences

*Milton Gomez*

**Abstract:** Students in earth and environmental sciences generally have limited time dedicated to learning programming. As machine learning (ML) techniques become more widespread in our fields, we find that providing course materials that introduce the concepts behind ML techniques and materials showcasing the use of techniques in recent literature helps students develop the skills necessary to apply ML to their own research. We tackle each ML concept through notebooks that use benchmark datasets and take inspiration from renowned references. We then focus on reproduction of the work in over 5 papers/preprints that successfully applied ML to climate science, emphasizing the importance of reproducibility and establishing trust in ML research. We also provide a platform to highlight the result of our students' work via final projects in which they apply the course’s concepts in their Master's research. These further show how the course promotes work at the intersection of environmental science and elementary ML methods. The materials are open source, hosted on GitHub, and further developments will increase the variety in deep learning algorithms presented throughout the course. We also provide materials covering an introduction to the Python skills required to follow the notebooks.  Finally, part of the materials have already been used in a Massively Open Online Course (MOOC) developed by ECMWF, we hope to continue with development of a more robust Jupyter book and to develop our own MOOC.

<a href="https://pretalx.com/euroscipy-2023/talk/YQNNB7/"><button type="button" class="btn btn-primary">All details</button></a>


## Streamline Your Scientific Work with AutoML

*Piotr Płoński, Aleksandra Płońska*

**Abstract:** How can AutoML technology be used in scientific research? Take a sneak peek at where your data analysis can be easier with mljar-supervised. By automating every step of the pipeline, from preprocessing to algorithm selection and explanation, researchers can easily advance their work. We will showcase the various fields in which scientists have implemented AutoML technology

<a href="https://pretalx.com/euroscipy-2023/talk/ZMLBES/"><button type="button" class="btn btn-primary">All details</button></a>
