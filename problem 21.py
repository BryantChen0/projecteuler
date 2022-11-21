{
 "cells": [
  {
   "cell_type": "markdown",
   "source": [
    "Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).\n",
    "If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.\n",
    "\n",
    "For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.\n",
    "\n",
    "Evaluate the sum of all the amicable numbers under 10000."
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
   "execution_count": 11,
   "outputs": [
    {
     "data": {
      "text/plain": "31626"
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import sympy\n",
    "#find sum of divisors in num\n",
    "def sum_divisors(num):\n",
    "    a = sympy.factorint(num)\n",
    "    res = 1\n",
    "    for i in a:\n",
    "        res *= (i**(a[i]+1)-1)//(i-1)\n",
    "    return res - num\n",
    "\n",
    "#find the amicable num\n",
    "def amicable_num (n):\n",
    "    list = []\n",
    "    for i in range (2,n+1):\n",
    "        a = sum_divisors(i)\n",
    "        if a != i and i == sum_divisors(a):\n",
    "            list.append(i)\n",
    "    return sum(list)\n",
    "\n",
    "amicable_num(10000)"
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