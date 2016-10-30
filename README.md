# The Monty Hall Problem in Python
## Simple algorithm to help demonstrate the real probabilities in the Monty Hall Problem

### Brief Description
Before you start, I highly recommend you watch [this video on YouTube](https://www.youtube.com/watch?v=mhlc7peGlGg) which quickly explains the Monty Hall Problem. After watching that video for the first time, I was so intrigued by the solution given there that I decided to quickly write a few lines of python to help me see if the video was right or wrong. I really felt like the video had to be wrong, and the probability of choosing the right door between the last two doors was 50/50. After writing this program, it became clear to me that I was wrong.

### How to Run
This is built for Python 2. Type `python montyhall.py` on the terminal and enter the desired iterations to run (the higher this value is, the more accurate the results will be, although the algorithm will also take more time).

### Final Results
In the end, the program prints the percentage of times that the swapping method won, the percentage of times that the non-swapping method won, and the sum of both percentages.

According to the mathematical resolution of this problem, the end results of this problem should be:
```
The swapping method won 66.66% of the time;
The non-swapping method won 33.33% of the time;
The sum of both results is 100.00%.
```
Obviously you'll almost certainly never get exactly these results, but if you run the program for enough iterations they shouldn't deviate more than 0.1% from the mathematically accurate results.