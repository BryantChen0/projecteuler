{
 "cells": [
  {
   "cell_type": "markdown",
   "source": [
    "Euler discovered the remarkable quadratic formula:\n",
    "\n",
    "\n",
    "It turns out that the formula will produce 40 primes for the consecutive integer values . However, when  is divisible by 41, and certainly when  is clearly divisible by 41.\n",
    "\n",
    "The incredible formula  was discovered, which produces 80 primes for the consecutive values . The product of the coefficients, −79 and 1601, is −126479.\n",
    "\n",
    "Considering quadratics of the form:\n",
    "\n",
    ", where  and\n",
    "\n",
    "where  is the modulus/absolute value of\n",
    "e.g.  and\n",
    "Find the product of the coefficients,  and , for the quadratic expression that produces the maximum number of primes for consecutive values of , starting with ."
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
      "text/plain": "-59231"
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sympy import isprime\n",
    "\n",
    "def quadratic(n, a, b):\n",
    "    return n**2 + a*n + b\n",
    "\n",
    "def is_prime(a,b):\n",
    "    x = 0\n",
    "    while True:\n",
    "        if isprime(quadratic(x, a, b)):\n",
    "            x += 1\n",
    "        else:\n",
    "            return x\n",
    "\n",
    "def find_max():\n",
    "    res = {}\n",
    "    for i in range(-999, 1000, 2):\n",
    "        for k in [j for j in range(-1000, 1001) if isprime(j)]:\n",
    "            res[is_prime(i, k)] = (i, k)\n",
    "    a,b = res[max(res)]\n",
    "    return a*b\n",
    "\n",
    "find_max()"
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