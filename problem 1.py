{
 "cells": [
  {
   "cell_type": "markdown",
   "source": [
    "If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.\n",
    "\n",
    "Find the sum of all the multiples of 3 or 5 below 1000."
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
   "execution_count": 2,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "233168\n"
     ]
    }
   ],
   "source": [
    "sum = 0\n",
    "num = 0\n",
    "while num < 999:\n",
    "    num +=1\n",
    "    if num % 3 == 0 or num % 5 == 0:\n",
    "        sum += num\n",
    "print(sum)"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "outputs": [],
   "source": [],
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