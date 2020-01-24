# majority-dynamics-simulation
Source code of the simulation of the majority dynamics in our paper titled "The Power of Few".

The source code is written in Python. We recommend the installation of the package <code>numpy</code>, version 1.13 or above, before running this source code. Users who have Python <code>numpy</code> installed can run the simulation via two steps. First, copy the code and save as <code>simulation.py</code>. Second, run the following command from terminal (assuming the command for Python is <code>python</code>):

<code>python simulation.py [n] [p] [c] [T]</code>

Here <code>n</code> and <code>p</code> are the parameters of the distribution <code>G(n, p)</code>, <code>c</code> is the advantage (so that Red has <code>n/2 + c</code> members), and <code>T</code> is the number of trials. For example, one runs <code>2000</code> trials on <code>G(1000, 0.5)</code> with <code>5001</code> Red and <code>4999</code> Blue members using the following command:

<code>python simulation.py 1000 0.5 1 2000</code>
