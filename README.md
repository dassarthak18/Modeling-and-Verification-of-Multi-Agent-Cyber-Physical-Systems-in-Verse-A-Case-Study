## Modeling and Verification of Multi-Agent Cyber-Physical Systems in Verse : A Case Study
Submitted to ISEC 2024.

### Abstract

Verification tools for cyber-physical systems (CPS) often have their own input specification language based on formal models of CPS. This requires tool users to have acquaintance to formal models and thus poses a barrier for new users to get introduced to the verification technology. To address this concern, [Verse](https://github.com/AutoVerse-ai/Verse-library) is a recent Python library that aims to make modeling and verification of CPS more accessible. This library does not require the users to have prior knowledge of formal models of CPS. In this paper, we study the Verse library and its capabilities through two case studies: one in vehicle control and the other in robotics, demonstrating the differences from conventional CPS modeling.

### ACC

Our source code for ACC can be found here. We see that our control strategy is unsafe. Additionally, we provide some plots.

1. For the initial condition:
* $x = 5$, $y = 0$, $vx = 28$, $ax = 0$ for the ego;
* $x = 15$, $y = 0$, $vx = 28$, $ax = 0$ for the lead;

we plot y vs. x:

![Plot 1](ACC/plot1.png)

and x vs. t:

![Plot 2](ACC/plot3.png)

2. For the initial condition range:
* $x \in [0,5]$, $y = 0$, $vx \in [0,15]$, $ax = 0$ for the ego;
* $x \in [7.5,20]$, $y = 0$, $vx = 28$, $ax = 0$ for the lead;

we plot y vs. x:

![Plot 1](ACC/plot4.png)

and x vs. t:

![Plot 2](ACC/plot2.png)
