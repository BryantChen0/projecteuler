{
 "cells": [
  {
   "cell_type": "markdown",
   "source": [
    "Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:\n",
    "\n",
    "1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...\n",
    "\n",
    "By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."
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
   "execution_count": 1,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4613732\n"
     ]
    }
   ],
   "source": [
    "sum = 0\n",
    "current_num = 2\n",
    "pre_num = 1\n",
    "while current_num < 4000000:\n",
    "    if current_num % 2 == 0:\n",
    "        sum += current_num\n",
    "    next_num = current_num + pre_num\n",
    "    pre_num = current_num\n",
    "    current_num = next_num\n",
    "\n",
    "print(sum)"
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