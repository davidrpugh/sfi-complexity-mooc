[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/davidrpugh/sfi-complexity-mooc)

# SFI Complexity Economics MOOC

Instructors: Prof. J. Doyne Farmer and Dr. David R. Pugh (and co-conspirators!)

From one of Gabby’s previous emails…

> On average an SFI MOOC is 10 weeks long, with 1 unit per week.  Each unit is made up of roughly six-ten subunits.  Most of the subunits consists of 1 to 3 video segments (ideally less than 10 minutes long), exercises (if appropriate) a quiz, and quiz solutions (in text or video form).  The last subunits may not have video, instead having a homework assignment and homework solution, and an end of unit test. As an example of how a course is structured see the outline for the Introduction to Complexity MOOC.

## Course Outline

### Lecture 1: Introduction to Complexity Economics
We want to highlight the frontier research (hopefully in a way the will make it digestible to second year undergraduates).

Might make sense to have the following sub-units:
Introductory video providing clear explanation of what complexity economics is (and what it isn’t). We will want to define key themes that will run throughout the course as well as terms and definitions (i.e., what is equilibrium, etc).  A constructive critique of the mainstream approach to economics.

* Video on the scientific method and how it differs in physics and economics.
* Primer on power laws.
* Primer on dynamical systems.
* Primer on basic network theory.
* Primer on use of Jupyter notebooks in the cloud (include pointers to instructions for installing software including on where to go to learn more about [best-practices for scientific computing](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745); no support for software install will be given!).

Also we will need to leave time to cover usual course logistics.

# Lecture 2: Networks
**Key ideas: Networks are pervasive in real world economies. Depending on underlying network topology, networks can either amplify or dampen idiosyncratic shocks. This has important policy implications. Traditional economics approach focuses on "equilibrium" and (mostly ignores) dynamics, complexity economics approach explicitly models dynamics and "equilibrium", if it exists, is a secondary consideration.**

Start with branch of complexity economics that has been the most successful at impacting mainstream economics.  Focus on Input-Output networks. Acemoglu et al's [Network Origins of Aggregate Fluctuations](http://economics.mit.edu/files/8135) and [Networks, Shocks, and Systemic Risk](http://economics.mit.edu/files/10423) which focus on equilibrium analysis, and the [Bouchaud et al paper](http://arxiv.org/pdf/1406.5022.pdf) which focuses on underlying dynamics would be natural points of departure but are perhaps too advanced. Do simpler alternatives exist? Can make use of [pyBEA](https://github.com/davidrpugh/pyBEA) to grab data on U.S. input-output networks directly from the BEA data API. Another source  of IO network data is the [WIOD database](http://www.wiod.org/new_site/database/wiots.htm).

Can we tie in what we are doing in this lecture to the other Complexity Explorer MOOC on Dynamics of Complex Networks?

Our 10 youtube length segments...

1. Basics of networks: should summarize relevant bits of the network literature and point interested students at the SFI MOOC on networks for more details.
2. What are input-output networks, and why are they important.  Where do we find data on input output networks? How do we find the data we will use for this lecture.
3. Traditional economics approach to IO networks focuses on equilibrium networks and is exemplified by recent Acemoglu et al papers. Focus on Acemoglu et al handbook chapter rather than their Econometrica and AER papers.
4. Finish discussion of the Acemoglu et al approach.
5. Short quiz.
6. Acemoglu et al model has no dynamics at all. Quick discussion of the literature on dynamics on networks.  
7. Use the [Bouchaud et al paper](http://arxiv.org/pdf/1406.5022.pdf) papers which extend the Acemoglu framework and explicitly model dynamics.
8. More Bouchaud et al...
9. Even more Bouchaud et al...
10. Short quiz.

# Lecture 3: Business Cycles
Key idea: business cycles are fundamentally endogenous phenomena and are not driven by exogenous shocks as is typically (but not always!) assumed in mainstream approaches.  Models of "Predator-prey" dynamics.

# Lectures 4 and 5: Growth and Innovation
Will use the Solow growth model as point of departure for lecture 4  Will need to explain the basic idea behind the model to non-economics audience. Solow model can be used to motivate the importance of explicitly modeling the process of technological innovation.

Evolutionary view of technological progress. See W. Brian Arthur’s Nature of Technology.  We should ask Brian if he would be interested in giving some parts of lectures 4 and 5.

# Lecture 6: Financial Markets
This lecture will motivate the use of ABMs by covering two different ABMs of financial markets: SFI stock market (old) and Farmer, et al Leverage Causes Fat Tails and Clustered Volatility model (new).

# Lecture 7: Experimental Economics
Motivated by the work of Cars Hommes on experimental models of expectations formation. Will touch on use of “rules of thumb,” models of learning, etc.

# Lecture 8: Game Theory
Obvious ties with the mainstream literature.  Motivated by recent (and ongoing) work of Farmer & Galla.  Key idea: learning and convergence to “equilibrium”. When and under what circumstances do learning rules lead to a convergence to Nash-like equilibrium in games.

Iterated Prisoner's dilemma tournament using code from Alan Isaac's [Simulating Evolutionary Games: A Python-Based Introduction(http://jasss.soc.surrey.ac.uk/11/3/8.html).  Perhaps could make use of Luzius's code to run the tournament.  Each student would submit a simple Python agent with a particular strategy and then we would run face them off against one another.

# Lectures 9: Inequality
Sugarscape-esque simulations to demonstrate conditions for skewed distributions of wealth.  Can be tied to Edgeworth Box diagrams.  Contrast the robustness of the first welfare theorem, with the fragility of the second welfare theorem.

# 10: Overflow!
I expect that this lecturers will fill out once we start filling in lecturers 1-8…

Topics that don’t seem to fit anywhere yet:

Rob’s model of firms…
Brian’s work on increasing returns to scale and path dependence.
Need to figure out a way to incorporate ScalABM to some extent. Possibly have some web application running interesting model on AWS that students can interact. Fabulous opportunity to build user community…
However, ScalABM is cutting edge research tool.  Pedagogically better to teach simulation and computation using Python a la Software Carpentry.  

Lecture: DSGE vs. Complexity Economics
A Beginner’s Guide to the DSGE Model
Material for this lecture is heavily influenced by David Colander’s Macroeconomics (pg. 293).

Start with the Bob Solow quote…

[The DSGE model is] a model in which a single immortal consumer-worker-owner maximizes a perfectly conventional time-additive utility function over an infinite horizon, under perfect foresight or rational expectations, and in an institutional and technological environment that favors universal price-taking behavior.

Discuss each of the following in turn…
single immortal consumer-worker-owner
perfectly conventional time-additive utility function
perfect foresight or rational expectations
universal price-taking behavior

Generic policy implications of DSGE models…
Ricardian Equivalence
Time-Inconsistency/Credibility
Lucas Critique

Complexity Approach to Macro

Consider simple variant of the Cobweb model that clearly demonstrates differences between standard macro mode, DSGE, and complex systems models.
Standard macro model: Backward looking expectations
DSGE model: rational expectations
Complex systems models: smart people with less than perfect foresight


## Additional teaching resources
Leigh Tesfatsion’s [excellent website](http://www2.econ.iastate.edu/tesfatsi/ace.htm).  We need to find a way to include more of her work into the course!!!!
