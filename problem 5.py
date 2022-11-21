{
 "cells": [
  {
   "cell_type": "markdown",
   "source": [
    "2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.\n",
    "\n",
    "What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%% md\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "2\n",
      "3\n",
      "6\n",
      "4\n",
      "12\n",
      "5\n",
      "60\n",
      "6\n",
      "60\n",
      "7\n",
      "420\n",
      "8\n",
      "840\n",
      "9\n",
      "2520\n",
      "10\n",
      "2520\n",
      "11\n",
      "27720\n",
      "12\n",
      "27720\n",
      "13\n",
      "360360\n",
      "14\n",
      "360360\n",
      "15\n",
      "360360\n",
      "16\n",
      "720720\n",
      "17\n",
      "12252240\n",
      "18\n",
      "12252240\n",
      "19\n",
      "232792560\n",
      "20\n"
     ]
    },
    {
     "data": {
      "text/plain": "232792560"
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from math import gcd\n",
    "from functools import reduce\n",
    "\n",
    "def lcm(n):\n",
    "    def lcm2(a, b):\n",
    "        return (a * b) // gcd(a, b)\n",
    "    return reduce(lcm2, range(1,n+1))\n",
    "\n",
    "lcm(20)"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}