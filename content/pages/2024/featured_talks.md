---
title: EuroSciPy 2024 - Featured Talks
url: 2024/featured_talks.html
save_as: 2024/featured_talks.html
section: euroscipy_2024
template: page
slug: accepted_talks_2024
---

# Featured Talks


## LPython: Novel, Fast, Retargetable Python Compiler

*Naman Gera*,  *Talk (25 mins + Q&A)*, *High Performance Computing*

**Abstract:** Python is one of the most used languages today, known for its simplicity and versatile ecosystem. For performance applications such as High Performance Computing (HPC) or any other kind of numerical computing the standard CPython implementation is often not fast enough. To address these issues, enter the fascinating world of LPython, a Python compiler designed to give you the best possible performance for numerical, array-oriented code, and can also generate code using multiple backends like LLVM, C, C++, WASM.

<a href="https://pretalx.com/euroscipy-2024/talk/3K8ZXN/"><button type="button" class="btn btn-primary">All details</button></a>


## Simulated data is all you need: Bayesian parameter inference for scientific simulators with SBI

*Jan Boelts (Teusen)*,  *Talk (25 mins + Q&A)*, *Scientific Applications*

**Abstract:** Simulators play a crucial role in scientific research, but accurately determining their parameters to reproduce observed data remains a significant challenge. Classical parameter inference methods often struggle due to the stochastic or black-box nature of these simulators. Simulation-based inference (SBI) offers a solution by enabling Bayesian parameter inference for simulation-based models: It only requires simulated data as input and returns a posterior distribution over suitable model parameters, including uncertainty estimates and parameter interactions. In this talk, we introduce SBI and present [`sbi`](https://sbi-dev.github.io/sbi/), an open source library that serves as a central resource for SBI practitioners and researchers, offering state-of-the-art SBI algorithms, comprehensive documentation and tutorials.

<a href="https://pretalx.com/euroscipy-2024/talk/893KBK/"><button type="button" class="btn btn-primary">All details</button></a>


## Using the Array API to write code that runs with Numpy, Cupy and PyTorch

*Tim Head, Sebastian Berg*,  *Tutorial*, *High Performance Computing*

**Abstract:** Python code that works with Numpy, Cupy and PyTorch arrays? Use a GPU when possible, but fallback to using a CPU if there is none? We will show you how you can write Python code that can do all of the above. The not so secret ingredient to do this is the Array API. In this workshop you will learn what the Array API is and how to use it to write programs that can take any compatible array as input.

<a href="https://pretalx.com/euroscipy-2024/talk/89KK7L/"><button type="button" class="btn btn-primary">All details</button></a>


## From data analysis in Jupyter Notebooks to production applications: AI infrastructure at reasonable scale

*Frank Sauerburger*,  *Talk (15 mins + Q&A)*, *Machine and Deep Learning*

**Abstract:** The availability of AI models and packages in the Python ecosystem has revolutionized many applications across domains. This talk discusses infrastructural decisions and best practices that bridge the gap between interactive data analyses in notebooks and production applications at a reasonable scale, suitable for both commercial and scientific contexts. In particular, the talk introduces the on-premises, Python-based AI architecture employed at MDPI, one of the largest open-access publishers. The presentation emphasizes the impact of the design on reproducibility, decoupling of different resources, and ease of use during the development and exploration phases.

<a href="https://pretalx.com/euroscipy-2024/talk/8NJGVH/"><button type="button" class="btn btn-primary">All details</button></a>


## Multi-dimensional arrays with Scipp

*Mridul Seth*,  *Tutorial*, *High Performance Computing*

**Abstract:** Inspired by xarray, Scipp enriches raw NumPy-like multi-dimensional data arrays by adding named dimensions and associated coordinates. For an even more intuitive and less error-prone user experience, Scipp adds physical units to arrays and their coordinates. Through this tutorial, participants will learn about the basics of modelling their data with the Scipp library and using in built tools in Scipp for scientific data analysis.

One of Scipp's key features is the possibility of using multi-dimensional non-destructive binning to sort record-based "tabular"/"event" data into arrays of bins. This provides fast and flexible binning, rebinning, and filtering operations, all while preserving the original individual records.

Scipp ships with data display and visualization features for Jupyter notebooks, including a powerful plotting interface. Named Plopp, this tool uses a graph of connected nodes to provide interactivity between multiple plots and widgets, requiring only a few lines of code from the user.

Scipp is available via pip and conda and runs on Linux, Mac and Windows.

<a href="https://pretalx.com/euroscipy-2024/talk/8WL8GX/"><button type="button" class="btn btn-primary">All details</button></a>


## Decorators - A Deep Dive

*Mike Müller*,  *Tutorial*, *Scientific Applications*

**Abstract:** Python offers decorator to implement re-usable code for cross-cutting task.
The support the separation of cross-cutting concerns such as logging, caching,
or checking of permissions.
This can improve code modularity and maintainability.

This tutorial is an in-depth introduction to decorators.
It covers the usage of decorators and how to implement simple and more advanced
decorators.
Use cases demonstrate how to work with decorators.
In addition to showing how functions can use closures to create decorators,
the tutorial introduces callable class instance as alternative.
Class decorators can solve problems that use be to be tasks for metaclasses.
The tutorial provides uses cases for class decorators.

While the focus is on best practices and practical applications, the tutorial
also provides deeper insight into how Python works behind the scene.
After the tutorial participants will feel comfortable with functions that take
functions and return new functions.

<a href="https://pretalx.com/euroscipy-2024/talk/BCAUKU/"><button type="button" class="btn btn-primary">All details</button></a>


## The joys and pains of reproducing research: An experiment in bioimaging data analysis

*Marianne Corvellec*,  *Talk (25 mins + Q&A)*, *Data Science and Visualisation*

**Abstract:** The conversation about reproducibility is usually focused on how to make research workflows (more) reproducible. Here, we consider it from the opposite perspective, and ask: How feasible is it, in practice, to reproduce research which is meant to be reproducible? Is it even done or attempted? We provide a detailed account of such an attempt, trying to reproduce some segmentation results for 3D microscopy images of a developing mouse embryo. The original research is a monumental work of bioimaging and analysis at the single-cell level, published in *Cell* in 2018, alongside with all the necessary research artifacts. Did we succeed in this attempt? As we share the joys and pains of this journey, many questions arise: How do reviewers assess the reproducibility claims exactly? Incentivizing reproducible research is still an open problem, since it is so much more costly (in time) to produce. And how can we incentivize those who test reproducibility? Not only is it costly to set up computational environments and execute data-intensive scientific workflows, but it may not appear as rewarding at first thought. In addition, there is a human factor: It is thorny to show authors that their publication does not hold up to their reproducibility claims.

<a href="https://pretalx.com/euroscipy-2024/talk/BXNEY8/"><button type="button" class="btn btn-primary">All details</button></a>


## Building robust workflows with strong provenance

*Alexander Goscinski, Julian Geiger, Ali Khosravi*,  *Tutorial*, *Scientific Applications*

**Abstract:** In computational science, different software packages are often glued together as scripts to perform numerical experiments. With increasing complexity, these scripts become unmaintainable, prone to crashes, hard to scale up and to collaborate on. AiiDA solves these problems via a powerful workflow engine and by keeping provenance for the entire workflow. In this tutorial, we learn how to create dynamic workflows combining together different executables that automatically can restart from failed runs and reuse results from completed calculations via caching.

<a href="https://pretalx.com/euroscipy-2024/talk/BYESWT/"><button type="button" class="btn btn-primary">All details</button></a>


## The Array API Standard in SciPy

*Lucas Colley*,  *Talk (15 mins + Q&A)*, *High Performance Computing*

**Abstract:** The array API standard is unifying the ecosystem of Python array computing, facilitating greater interoperability between array libraries, including NumPy, CuPy, PyTorch, JAX, and Dask. Find out how we are using it in SciPy to bring support for hardware-accelerated (e.g. GPU) and distributed arrays to our users, and how you can do the same in your library.

<a href="https://pretalx.com/euroscipy-2024/talk/BYTCSC/"><button type="button" class="btn btn-primary">All details</button></a>


## From stringly typed to strongly typed: Insights from re-designing a library to get the most out of type hints

*Janos Gabler*,  *Talk (25 mins + Q&A)*, *Community, Education, and Outreach*

**Abstract:** Many scientific Python packages are "stringly typed," i.e., using strings to select algorithms or methods and dictionaries for configuration. While easy for beginners and convenient for authors, these libraries miss out on static typing benefits like error detection before runtime and autocomplete. This talk shares insights from redesigning the optimagic library from the ground up with static typing in mind. Without compromising on simplicity, we achieve better static analysis, autocomplete, and fewer runtime errors. The insights are not specific to numerical optimization and apply to a wide range of scientific Python packages.

<a href="https://pretalx.com/euroscipy-2024/talk/CETWRS/"><button type="button" class="btn btn-primary">All details</button></a>


## sktime - python toolbox for time series – introduction and new features 2024: foundation models, deep learning backends, probabilistic models, changepoints and segmentation

*Franz Kiraly*,  *Tutorial*, *Machine and Deep Learning*

**Abstract:** sktime is the most widely used scikit-learn compatible framework library for learning with time series. sktime is maintained by a neutral non-profit under permissive license, easily extensible by anyone, and interoperable with the python data science stack.

This tutorial gives a hands-on introduction to sktime, for common time series learning tasks such as forecasting, and an overview of different model categories, pipeline building, feature engineering, model tuning, and autoML.

The tutorial also showcases newest features in 2024, including support for foundation models, hugging face connectors, probabilistic models, categorical features, anomaly and changepoint detection, time series segmentation.

<a href="https://pretalx.com/euroscipy-2024/talk/DF3VHU/"><button type="button" class="btn btn-primary">All details</button></a>


## Free-threaded (aka nogil) CPython in the Scientific Python ecosystem : status and road ahead

*Loïc Estève*,  *Talk (25 mins + Q&A)*, *Machine and Deep Learning*

**Abstract:** CPython 3.13 will be released in October 2024 and has been in beta since May 2024. One of its most awaited features is the possibility to remove the GIL (Global Interpreter Lock) through a compile-time flag.

In this talk we will explain the relevance of free-threaded CPython for the Scientific Python ecosystem, what already works, some of the caveats, and how to try it out on your favourite use case. 

In particular we will discuss:
- the historic effort in the scikit-learn project to add Continuous Integration for the `nogil` fork of CPython 3.9, and the kind of issues that were surfaced
- the ongoing effort in the Scientific Python ecosystem (Numpy, Scipy, scikit-learn, etc ...) to test free-threaded CPython 3.13 and fix issues along the way
- how a typical scikit-learn grid-search use case can benefit from free-threaded CPython
- how to try out free-threaded CPython on your favourite use case
- possible future developments

<a href="https://pretalx.com/euroscipy-2024/talk/DLYRXH/"><button type="button" class="btn btn-primary">All details</button></a>


## The Parallel Universe in Python - A Time Travel to Python 3.13 and beyond

*Mike Müller*,  *Talk (25 mins + Q&A)*, *High Performance Computing*

**Abstract:** Parallel computing is essential for many performance-critical applications. Python provides many solutions for this problem. New versions of Python will support sub-interpreters and a, currently experimental, free-threading version without the Global Interpreter Lock (GIL).

This talk starts with a short overview over this topic, clarifying terms such parallel, concurrent, and distribute computing as well as CPU-bound, memory-bound, and IO-bound problems. The presentation explains how Python and its standard library support parallel programming tasks. In addition, many Python libraries provide very useful approaches and tools for parallel computing. An overview of important libraries provides guidance which library can be used for what type of parallel problem.

How do Python's new features such as sub-interpreters and free-threading without the Global Interpreter Lock (GIL) impact parallel Programming in Python? This talk address this question by providing examples where these features might help to make programs simpler and/or faster.

<a href="https://pretalx.com/euroscipy-2024/talk/E8HD9K/"><button type="button" class="btn btn-primary">All details</button></a>


## wgpu and pygfx: next-generation graphics for Python

*Almar Klein*,  *Talk (25 mins + Q&A)*, *Data Science and Visualisation*

**Abstract:** This talk introduces a new render engine for Python, called pygfx (pronounced "py-graphics"). Its purpose is to bring powerful and reliable visualization to the Python world. Since pygfx is built on wgpu, it has superior performance and reliability compared to OpenGL-based solutions. It is also designed to be versatile: with its modular architecture, one can assemble graphical scenes for diverse applications, ranging from scientific visualization to video games.

<a href="https://pretalx.com/euroscipy-2024/talk/GKYTSY/"><button type="button" class="btn btn-primary">All details</button></a>


## The Mission Support System and its use in planning an aircraft campaign

*Reimar Bauer*,  *Talk (15 mins + Q&A)*, *Scientific Applications*

**Abstract:** The Mission Support System (MSS) is an open source software package that has been used for planning flight tracks of scientific aircraft in multiple measurement campaigns during the last decade. It consists of many components, a data-retrieval tool chain, a wms server which creates 2-D figures from 4-D meterogical data. A client application for displaying the figures in combination with the planned flight track and other data. For data exchange between participants a collaboration server is used. The talk describes how we used these components for a campaign.

<a href="https://pretalx.com/euroscipy-2024/talk/GQN8AF/"><button type="button" class="btn btn-primary">All details</button></a>


## Reproducible workflows with AiiDA - The power and challenges of full data provenance

*Marnik Bercx, Xing Wang*,  *Talk (25 mins + Q&A)*, *Scientific Applications*

**Abstract:** AiiDA is a workflow manager with a strong focus on reproducibility through automated data provenance. In this talk we discuss what it means to have full “data provenance” for scientific workflows, the advantages it offers, but also the challenges it represents for new users and how we deal with them.

<a href="https://pretalx.com/euroscipy-2024/talk/HKVEXW/"><button type="button" class="btn btn-primary">All details</button></a>


## A Comparative Study of Open Source Computer Vision Models for Application on Small Data: The Case of CFRP Tape Laying

*Thomas Fraunholz*,  *Talk (25 mins + Q&A)*, *Machine and Deep Learning*

**Abstract:** The world of open source computer vision has never been so exciting - and so challenging. With so many options available to you, what's the best way to solve your real world problem? The questions are always the same: Do I have enough data? Which model should I choose? How can I fine-tune and optimize the hyperparameters? 

In collaboration with the German Aerospace Center, we investigated these questions to develop a model for quality assurance of CFRP tape laying, with only a small real data set fresh from production. We are very pleased to present a machine learning setup that can empirically answer these questions. Not only for us, but also for you - our setup can easily be transferred to your application!

Dive with us into the world of Open Source machine learning tools that are perfectly tailored for your next project. Discover the seamless integration of Hugging Face Model Hub, DvC and Ray Tune. You'll also gain unique insights into the fascinating world of CFRP tape laying, specifically how well different architectures of open source models perform on our small dataset.

If you want to level up your MLOps game and gain practical knowledge of the latest computer vision models and practices, this talk is a must for you. Don't miss the opportunity, and look forward to your next computer vision projects!

<a href="https://pretalx.com/euroscipy-2024/talk/JWAMDE/"><button type="button" class="btn btn-primary">All details</button></a>


## Building optimized packages for conda-forge and PyPI

*Wolf Vollprecht*,  *Talk (15 mins + Q&A)*, *High Performance Computing*

**Abstract:** In this talk we're introducing a new tool to build conda packages. It has been adopted by the conda community and is being rolled out in the widely used conda-forge distribution. The new recipe format has been vetted in multiple Conda Enhancement Proposals (CEPs). We are going to introduce the exciting new features of rattler-build (reproducible builds, high speed build execution, etc.). Using some examples, we will then discuss how you can use rattler-build & conda-forge to build highly optimized packages with SIMD and CUDA support. We will also take a look at `cibuildwheel` and recent improvements in the PyPI space for CUDA.

<a href="https://pretalx.com/euroscipy-2024/talk/JXB79J/"><button type="button" class="btn btn-primary">All details</button></a>


## Skrub: prepping tables for machine learning

*Guillaume Lemaitre*,  *Talk (25 mins + Q&A)*, *Machine and Deep Learning*

**Abstract:** When it comes to designing machine learning predictive models, it is reported that data scientists spend over 80% of their time preparing the data to input to the machine learning algorithm.

Currently, no automated solution exists to address this problem. However, the `skrub` Python library is here to alleviate some of the daily tasks of data scientists and offer an integration with the `scikit-learn` machine learning library.

In this talk, we provide an overview of the features available in `skrub`.

First, we focus on the preprocessing stage closest to the data sources. While predictive models usually expect a single design matrix and a target vector (or matrix), in practice, it is common that data are available from different data tables. It is also possible that the data to be merged are slightly different, making it difficult to join them. We will present the `skrub` joiners that handle such use cases and are fully compatible with `scikit-learn` and its pipeline.

Then, another issue widely tackled by data scientists is dealing with heterogeneous data types (e.g., dates, categorical, numerical). We will present the `TableVectorizer`, a preprocessor that automatically handles different types of encoding and transformation, reducing the amount of boilerplate code to write when designing predictive models with `scikit-learn`. Like the joiner, this transformer is fully compatible with `scikit-learn`.

<a href="https://pretalx.com/euroscipy-2024/talk/MFF7GE/"><button type="button" class="btn btn-primary">All details</button></a>


## Introduction to Polars: Fast and Readable Data Analysis

*Geir Arne Hjelle*,  *Tutorial*, *Data Science and Visualisation*

**Abstract:** Polars is a new, powerful library for doing analysis on structured data. The library focuses on processing speed and a consistent and intuitive API. This tutorial will help you get started with Polars, by showing you how to read and write data and manipulate it with Polars' powerful expression syntax. You'll learn about how the lazy API is an important key to Polars' efficiency.

<a href="https://pretalx.com/euroscipy-2024/talk/MPMRUZ/"><button type="button" class="btn btn-primary">All details</button></a>


## Optimagic: Can we unify Python's numerical optimization ecosystem?

*Janos Gabler*,  *Talk (25 mins + Q&A)*, *Community, Education, and Outreach*

**Abstract:** Python has many high quality optimization algorithms but they are scattered across many different packages. Switching between packages is cumbersome and time consuming. Other languages are ahead of Python in this respect. For example, `Optimization.jl` provides a unified interface to more than 100 optimization algorithms and is widely accepted as a standard interface for optimization in Julia. 

In this talk, we take stock of the existing optimization ecosystem in Python and analyze pain points and reasons why no single package has emerged as a standard so far. We use these findings to derive desirable features a Python optimization package would need to unify the ecosystem. 

We then present optimagic, a NumFocus affiliated Project with the goal of unifying the Python optimization ecosystem. Optimagic provides a common interface to optimization algorithms from scipy, NlOpt, pygmo, and many other libraries. The minimize function feels familiar to users of scipy.optimize who are looking for a more extensive set of 
supported optimizers. Advanced users can use optional arguments to configure every aspect of the optimization, create a persistent log file, turn local optimizers global with a multistart framework, and more. 

Finally, we discuss an ambitious roadmap for improvements, new features, and planned community activities for optimagic.

<a href="https://pretalx.com/euroscipy-2024/talk/NGECXK/"><button type="button" class="btn btn-primary">All details</button></a>


## Conformal Prediction with MAPIE: A Journey into Reliable Uncertainty Quantification

*Claudio G. Giancaterino*,  *Talk (15 mins + Q&A)*, *Data Science and Visualisation*

**Abstract:** In the ever-evolving landscape of data science, accurate uncertainty quantification is crucial for decision-making processes. Conformal Prediction (CP) stands out as a powerful framework for addressing this challenge by providing reliable uncertainty estimates alongside predictions. In this talk, I'll delve into the world of Conformal Prediction, with a focus on the MAPIE Python library, offering a comprehensive understanding of its advantages and practical applications.

<a href="https://pretalx.com/euroscipy-2024/talk/NH7LGF/"><button type="button" class="btn btn-primary">All details</button></a>


## Federated Learning: Where we are and where we need to be

*Katharine Jarmul*,  *Talk (25 mins + Q&A)*, *Machine and Deep Learning*

**Abstract:** In this talk, we'll review the landscape of open-source federated learning libraries with a lens on actual real world data problems, use cases and actors who could benefit from federated learning. We'll then analyze gaps, weaknesses and explore new ways we could formulate federated learning problems (and their associated libraries!) to build more useful software and use decentralized machine learning in real world use cases.

<a href="https://pretalx.com/euroscipy-2024/talk/PFVX9L/"><button type="button" class="btn btn-primary">All details</button></a>


## Paths in Parallel: Creating Custom NetworkX Backends

*Erik Welch, Aditi Juneja*,  *Talk (25 mins + Q&A)*, *Community, Education, and Outreach*

**Abstract:** Hi! Have you ever wished your Python libraries could run faster algorithms? Or wanted to fundamentally improve a python library by re-writing everything in a faster language like C or Rust? 

NetworkX is a popular, pure Python library used for graph(aka network) analysis. But, when the graph size increases (like a network of everyone in the world) then networkx algorithms could take days to solve a simple graph analysis problem. So, to address these performance issues, recently, a backend dispatch mechanism was developed. This mechanism leverages Python's package discovery mechanism using [`entry_points`](https://packaging.python.org/en/latest/specifications/entry-points) specification.

In this talk, we will unveil NetworkX's API Dispatching architecture that lets us redirect the plain old NetworkX’s function call to an alternative implementation present in a backend package, just by specifying a `backend` kwarg like this:

    >>> nx.betweenness_centrality(Graph, backend=“parallel”)

We will also go over all the implementation details and challenges of this dispatching mechanism, and then we’ll use the example of the nx-parallel as a guide to building our own custom NetworkX backend. And then using the NetworkX's testing suite to test this backend of ours. Ending with a quick dive into the details of the nx-parallel backend and a quick walk through of other backends and future ToDos. And then finally conclude with an interactive Q&A.

<a href="https://pretalx.com/euroscipy-2024/talk/QLVBYY/"><button type="button" class="btn btn-primary">All details</button></a>


## Enhancing Bayesian Optimization with Ensemble Models for Categorical Domains

*Ilya Komarov*,  *Talk (15 mins + Q&A)*, *Data Science and Visualisation*

**Abstract:** Bayesian optimization is a powerful technique for optimizing black-box, costly-to-evaluate functions, widely applicable across diverse fields. However, Gaussian process (GP) models commonly used in Bayesian optimization struggle with functions defined on categorical or mixed domains, limiting optimization in scenarios with numerous categorical inputs. In this talk, we present a solution by leveraging ensemble models for probabilistic modelling, providing a robust approach to optimize functions with categorical inputs. We showcase the effectiveness of our method through a Bayesian optimization setup implemented with the BoTorch library, utilizing probabilistic models from the XGBoostLSS framework. By integrating these tools, we achieve efficient optimization on domains with categorical variables, unlocking new possibilities for optimization in practical applications.

<a href="https://pretalx.com/euroscipy-2024/talk/SPUZPK/"><button type="button" class="btn btn-primary">All details</button></a>


## Regularizing Python using Structured Control Flow

*Valentin Haenel*,  *Talk (25 mins + Q&A)*, *High Performance Computing*

**Abstract:** In this talk we will present applied research and working code to regularize
Python programs using a Structured Control Flow Graph (SCFG). This is a novel
approach to rewriting programs at the source level such that the resulting
(regularized) program is potentially more amenable to compiler optimizations,
for example when using Numba[1] to compile Python.  The SCFG representation of
a program is simpler to analyze and thus significantly easier to optimize
because the higher order semantic information regarding the program structure
is explicitly included. This can be of great benefit to many scientific
applications such as High Performance Computing (HPC), a discipline that relies
heavily on compiler optimizations to turn user source code into highly
performant executables. Additionally the SCFG format is a first step to
representing Python programs as Regionalized Value State Dependence Graphs
(RVSDGs). This is another recently proposed program representation which is
expected to unlock even more advanced compiler optimizations at the
Intermediary Representation (IR) level. The talk will cover an introduction to
the theory of SCFGs and RVSDG and demonstrate how programs are transformed. We
will start with simple Python programs containing control-flow constructs and
then show both the SCFG representation and the resulting regularized result to
illustrate the transformations.

<a href="https://pretalx.com/euroscipy-2024/talk/U3EMKF/"><button type="button" class="btn btn-primary">All details</button></a>


## Introduction to NumPy

*Sarah Diot-Girard*,  *Tutorial*, *Data Science and Visualisation*

**Abstract:** Are you starting to use Python for scientific computing? Join this tutorial to know more about NumPy, the building block for nearly all libraries in the scientific ecosystem.
You will learn how to manipulate NumPy arrays, understand how they store data and discover how to get optimal performances. By the end of this tutorial, you will be able to start working with NumPy and know the main pitfalls to avoid.

<a href="https://pretalx.com/euroscipy-2024/talk/UDVD77/"><button type="button" class="btn btn-primary">All details</button></a>


## Probabilistic classification and cost-sensitive learning with scikit-learn

*Guillaume Lemaitre, Olivier Grisel*,  *Tutorial*, *Machine and Deep Learning*

**Abstract:** Data scientists are repeatedly told that it is absolutely critical to align their model training methodology with a specific business objective. While being a rather good advice, it usually falls short on details on how to achieve this in practice.

This hands-on tutorial aims to introduce helpful theoretical concepts and concrete software tools to help them bridge this gap. This method will be illustrated on a worked practical use case: optimizing the operations of a fraud detection system for a payment processing platform.

More specifically, we will introduce the concepts of calibrated probabilistic classifiers, how to evaluate them and fix common causes of mis-calibration. In a second part, we will explore how to turn probabilistic classifiers into optimal business decision makers.

<a href="https://pretalx.com/euroscipy-2024/talk/UNYV7V/"><button type="button" class="btn btn-primary">All details</button></a>


## forecasting foundation models: evaluation and integration with sktime – challenges and outcomes

*Franz Kiraly*,  *Talk (25 mins + Q&A)*, *Machine and Deep Learning*

**Abstract:** Foundation models are here for forecasting! This will conclusively solve all forecasting problems with a one-model-fits-all approach! Or … maybe not?

Fact is, an increasingly growing number of foundation models for time series and forecasting hitting the market.

To innocent end users, this situation raises various challenges and questions. How do I integrate the models as candidates into existing forecasting workflows? Are the models performant? How do they compare to more classical choices? Which one to pick? How to know whether to “upgrade”?

At sktime, we have tried so you don’t have to! Although you will probably be forced to anyway, but even then, it’s worth sharing experiences.

Our key challenges and findings are presented in this talk – for instance, the unexpected fragmentation of the ecosystem, difficulties in evaluating the models fairly, and more.

(sktime is an openly governed community with neutral point of view. You may be surprised to hear that this talk will not try to sell you a foundation model)

<a href="https://pretalx.com/euroscipy-2024/talk/XBXX89/"><button type="button" class="btn btn-primary">All details</button></a>

