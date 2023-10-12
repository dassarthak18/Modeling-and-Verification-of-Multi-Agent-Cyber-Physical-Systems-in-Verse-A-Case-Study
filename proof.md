**Mathematical Proofs for the Number of Transitions in the Parallel Compositions of our Proposed Models for Clock Synchronization in a Swarm of Robots**

1. *lsync III*

Consider one of the $n$ robots, say robot $i$ in the swarm to take a $flash_i$ transition, which is a synchronizing transition. The structure of the automata are such that the guards of the two $flash_{j\neq i}$ transitions are complementary ($x \geq f/\alpha$ and $x < f/\alpha$) for all $i,j$.

Therefore, when robot $i$ takes its $flash_i$ transition, each of the remaining $n-1$ robots has to take exactly one of the two $flash_i$ transitions defined in their automata, resulting in a total of $2^{n-1}$ possible combinations. Each combination corresponds to a transition in the parallel composition with the synchronization label $flash_i$.

Since there are $n$ such possible $flash_i$ labels, the number of transitions in the parallel composition of lsync III satisfies no. of trans = $n.2^{n-1}$.

2. *shd III*

Each of the $n$ robots has three transitions in their automaton that do not correspond to any synchronization label. All of these transitions appear in the parallel composition, resulting in a total of $3.n$ transitions.

There is also a synchronizing transition $count$ in each of the $n$ automata. This leads to exactly one possible combination where all robots take their respective $count$ transitions, corresponding to a transition in the parallel composition with the synchronization label $count$.

Hence, the number of transitions in the parallel composition of shd III satisfies no. of trans = $3.n+1$.
