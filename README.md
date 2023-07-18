# ZipperMerge
Simulation of the zipper merge using Vpython.

# Motivation/Background 
After experencing painful traffic delays in the summer months and observing a few patterns in behaviors of drivers, I became curious how much time the zipper merge would actually save drivers in my local area. I explored two spheres of thought: pro merge and anti merge. I simulated two formations of traffic to see what formation would be faster for 21 cars. Note I also coded this up for a comedy show.

# Comedy Performance and Simultaion
Here's a link to the simulation: https://www.youtube.com/watch?v=VTmDIXYBgLw

Here's a link to the performance: https://www.youtube.com/watch?v=3QOnXhCjp3Q


# References
Huge shout out to Bilal Himite who posted the below towardsdatascience article on simulating traffic. I used the intelligent driver model referenced in the paper as a basis for the calculations in the Vpython code. I tried using Bilal's Pygame code but struggled adapting the code to successfully model merging. I also thought Vpython would be funnier for the performance. If you are serious about simulating traffic though, I recommend reading Bilal's article and building off of their code. https://towardsdatascience.com/simulating-traffic-flow-in-python-ee1eab4dd20f

# Collaboration
Go for it! Would love to hear how you use it. I'm sure there are manny errors and better ways to modularize the code. 


# Vpython as a simulation language?
I found zooming in and out using Vpythons native controls while the simulation was running affected the outcome of the simluation. Unclear if this is due to Vpython or my code (probably my code). I'm sure there is something with the interaction between the order in which the camera angle/zoom calls, my time counter, and series of updates to the cars (spheres). 
