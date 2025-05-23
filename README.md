# CECS427Assignment6
# Brandon Cazares
# Professor Ponce 
# CECS 427 Sec 1 
# Due Date: 5/11/2025 
# Objective
- This assignment requires us to understand cascade effects because the Susceptible-Infectious-Recovered-Suseptible (SIRS) model will create a program to validate whether a set of selected initiated triggers can complete a cascade.
- Subsequently, we will develop a simulation to test out COVID-19 using the SIRS model within a random directed graph.
- Additionally, it extends the model to the to simulate the impacts of shelter-in-place measures and vaccinations.
# Requirements 
- This is the command to execute the Pyhton script called dynamic_population.py to simulate the spread of a phenomenon (e.g. a cascade or a pandemic) across a network.
- This simulation will take account of various parameters such as the initiator, the spreading threshold, lifespan,  sheltering, and vaccination.
- This assignment requires us to create a Python code that runs in a terminal. This program accepts optional parameters.
- The command to execute the Python is shown in the following line:
python ./dynamic_population.py graph.gml --action [cascade|covid] --initiator m --threshold q --probability_of_infection p --probability_of_death q --lifespan l --shelter s --vaccination r --plot --interactive
# Description of Parameters 
- This script dynamic_population.py must be located in the current directory.
- This program must read the graph .gml file because that'll describe the main graph.
- This program's output plots a resulting graph and the plots of understanding the behavior because it also ensures a robusting file handling mechanisms such as error checking, file existence validation and appropriate error messages.
--action [cascade|covid]
- This either simulates a cascade effect through the network (e.g. information spread) or similuates the spread of the COVID-19 pandemic across the network
--initiator m
- We chose the initial node(s) from which the action will start. We replace m with specific node indentifiers because these are seperated by commas
--threshold q
Set the threshold value q (e.g., between 0 and 1) of the cascade effect.
--probability_of_infection p
- We set the probability of infection p for the infections
--probability_of_death q
- Set the probability q of death while infected
--lifespan l
- We define the lifespan of l (e.g a number of time steps of days) of the rounds.
--shelter s
- We set the sheltering parameter s (e.g. a proportion or list of nodes that will be sheltered or protected from the infection)
--vaccination r
- We set the vaccination rate or proportion r (e.g. a number between 0 and 1) representing the proportion of the network that is already vaccinated
--interactive
- We plot the graph and the state of nodes every round.
--plot
-- We finally plot the number of new infections per day when the simulation completes
- Test runs
- When I test ran my cascade graph using this command i got this result:
python ./dynamic_population.py graph.gml --action cascade --initiator 1,3,6 --threshold 0.33 --plot
- My result was 6 total active nodes and my cascade finished in 3 steps.
- When I rest ran my covid graph using this command i got this result
python ./dynamic_population.py graph.gml --action covid --initiator 3,4 --probability_of_infection 0.05 --lifespan 15 --shelter 0.3 --vaccination 0.25 --plot
- My result was initiators 3 and 4, probability of infecting at 0.05, it simulates 15-time steps (days) with 30 percent shelter in place and 25 percent of the population fully vaccinated. 
