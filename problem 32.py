{
 "cells": [
  {
   "cell_type": "markdown",
   "source": [
    "We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.\n",
    "\n",
    "The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.\n",
    "\n",
    "Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.\n",
    "\n",
    "HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum."
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
   "execution_count": 27,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "45228\n"
     ]
    }
   ],
   "source": [
    "set_res = set()\n",
    "for i in range (1,100):\n",
    "    start_num = 1000 if i < 9 else 100\n",
    "    for j in range (start_num,100000//i):\n",
    "        res = i * j\n",
    "        str_num = str(j) + str(i) + str(res)\n",
    "        if len(str_num) == 9 and set(str_num) == set(\"123456789\"):\n",
    "            set_res.add(res)\n",
    "print(sum(set_res))"
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