{
 "cells": [
  {
   "cell_type": "markdown",
   "source": [
    "The sum of the squares of the first ten natural numbers is,\n",
    "\n",
    "The square of the sum of the first ten natural numbers is,\n",
    "\n",
    "Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .\n",
    "\n",
    "Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."
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
   "execution_count": 13,
   "outputs": [
    {
     "data": {
      "text/plain": "25164150"
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from functools import reduce\n",
    "def sum_of_square(a):\n",
    "    c=0\n",
    "    for i in range (a+1):\n",
    "        b = i**2\n",
    "        c += b\n",
    "    return c\n",
    "\n",
    "def square_of_sum(n):\n",
    "    def sum(a,b):\n",
    "        return a+b\n",
    "    return reduce(sum,range(1,n+1))**2\n",
    "\n",
    "def difference(b):\n",
    "    return abs(sum_of_square(b)-square_of_sum(b))\n",
    "\n",
    "difference(100)"
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