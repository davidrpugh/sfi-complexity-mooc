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
* Discussion of pre-requisites with pointers to other relevant SFI MOOCS as well as third-party materials.
* Primer on use of Jupyter notebooks in the cloud (include pointers to instructions for installing software including on where to go to learn more about [best-practices for scientific computing](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745); no support for software install will be given!).

Also we will need to leave time to cover usual course logistics.

# Lecture 2: Cobweb Models, Expectations, and Learning
**Key ideas: Illustrate the important role of expectations in economic models. Distinguish between extreme forms of expectations (i.e., naive vs rational) and stress that real expectations formation rules fall somewhere in between.**

Our YouTube length segments...

1. Discuss the basic idea behind the cobweb model. Explain the basic building blocks of the classic Brock and Hommes' [Rational Route to Randomness](http://www.ssc.wisc.edu/~wbrock/rp457a.pdf). This model provides a nice framework that can be easily extended to incorporate some of the ingredients of Car's more recent work.
2. Describe different rules for forming expectations in the cobweb model.  Expectation formations rules are predictor functions that take a time series of prices and return a predicted value for a future price.  Contrast various expectations formation rules with rational expectations.
3. Simulate the Brock and Hommes model with homogenous beliefs (i.e., all agents use the same expectation formation rule)! Under what conditions does one get limit cycles? Chaotic dynamics? Equilibria? Brock and Hommes model with homogenous beliefs is *very* close to the earlier Hommes model in [Dynamics of the cobweb model with adaptive expectations and non-linear supply and demand](http://www.parisschoolofeconomics.eu/docs/guesnerie-roger/hommes94.pdf).
4. Simulate the Brock and Hommes model with heterogenous beliefs (i.e., agents use different expectation formation rules!). Under what conditions does one get limit cycles? Chaotic dynamics? Equilibria?
5. Short quiz.
6. **Cars Hommes contribution: Lecture on experimental evidence on how real market participants form expectations.  Need to discuss this with Cars ASAP!**
7. Explicitly make the link between simulation and computation and experimental work by use simulations to replicate some of the experimental evidence that Cars discusses in his lecture.
8. Short quiz.

# Lecture 3: Networks
**Key ideas: Networks are pervasive in real world economies. Depending on underlying network topology, networks can either amplify or dampen idiosyncratic shocks. This has important policy implications. Traditional economics approach focuses on "equilibrium" and (mostly ignores) dynamics, complexity economics approach explicitly models dynamics and "equilibrium", if it exists, is a secondary consideration.**

Start with branch of complexity economics that has been the most successful at impacting mainstream economics.  Focus on Input-Output networks. Acemoglu et al's [Network Origins of Aggregate Fluctuations](http://economics.mit.edu/files/8135) and [Networks, Shocks, and Systemic Risk](http://economics.mit.edu/files/10423) which focus on equilibrium analysis, and the [Bouchaud et al paper](http://arxiv.org/pdf/1406.5022.pdf) which focuses on underlying dynamics would be natural points of departure but are perhaps too advanced. Do simpler alternatives exist? Can make use of [pyBEA](https://github.com/davidrpugh/pyBEA) to grab data on U.S. input-output networks directly from the BEA data API. Another source  of IO network data is the [WIOD database](http://www.wiod.org/new_site/database/wiots.htm).

Can we tie in what we are doing in this lecture to the other Complexity Explorer MOOC on Dynamics of Complex Networks?

Our 10 youtube length segments...

1. Basics of networks: should summarize relevant bits of the network literature and point interested students at the SFI MOOC on networks for more details.
2. What are input-output networks, and why are they important.  Where do we find data on input output networks? How do we find the data we will use for this lecture.
3. Traditional economics approach to IO networks focuses on equilibrium networks and is exemplified by recent Acemoglu et al papers. Focus on Acemoglu et al handbook chapter rather than their Econometrica and AER papers.
4. Solve for the equilibrium of the Acemgolu et al model using real world IO network data. Informally compare model predictions to data.
5. Short quiz.
6. Acemoglu et al model has no dynamics at all. Quick discussion of the literature on dynamics on networks.  
7. Use the [Bouchaud et al paper](http://arxiv.org/pdf/1406.5022.pdf) papers which extend the Acemoglu framework and explicitly model dynamics.
8. Simulate the Bouchaud et al model(s) and informally compare to data.
9. Compare contrast Acemoglu et al (equilibrium) with Bouchaud et al (dynamics).
10. Short quiz.

Additional applications of networks in complexity economics can be found on Prof. Leigh Tesfatsion's [website](http://www2.econ.iastate.edu/tesfatsi/anetwork.htm).

# Lecture 3: Business Cycles
Key idea: business cycles are fundamentally endogenous phenomena and are not driven by exogenous shocks as is typically (but not always!) assumed in mainstream approaches.  Models of "Predator-prey" dynamics.

# Lectures 4 and 5: Growth and Innovation
Will use the Solow growth model as point of departure for lecture 4  Will need to explain the basic idea behind the model to non-economics audience. Solow model can be used to motivate the importance of explicitly modeling the process of technological innovation.

Evolutionary view of technological progress. See W. Brian Arthur’s Nature of Technology.  We should ask Brian if he would be interested in giving some parts of lectures 4 and 5.

# Lectures 6 and 7: Financial Markets
This lecture will motivate the use of ABMs by covering two different ABMs of financial markets: SFI stock market (old) and Farmer, et al Leverage Causes Fat Tails and Clustered Volatility model (new).


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

## Additional teaching resources
Leigh Tesfatsion’s [excellent website](http://www2.econ.iastate.edu/tesfatsi/ace.htm).  We need to find a way to include more of her work into the course!!!!
