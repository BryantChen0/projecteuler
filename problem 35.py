{
 "cells": [
  {
   "cell_type": "markdown",
   "source": [
    "The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.\n",
    "\n",
    "There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.\n",
    "\n",
    "How many circular primes are there below one million?"
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
   "execution_count": 37,
   "outputs": [
    {
     "data": {
      "text/plain": "55"
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sympy import isprime\n",
    "\n",
    "def circular (num):#find circular num\n",
    "    str_num = str(num)\n",
    "    res = {num}\n",
    "    for i in range (len(str_num)):\n",
    "        str_new_num = str_num[1:] + str_num[0]\n",
    "        res.add(int(str_new_num))\n",
    "        str_num = str_new_num\n",
    "    return res\n",
    "\n",
    "def primes (n):#all prime below 1000000\n",
    "    primes = [True]*n\n",
    "    primes[0],primes[1] = False,False\n",
    "    for (i,prime) in enumerate (primes):\n",
    "            if prime:\n",
    "                    for j in range (i*i, n, i):\n",
    "                            primes[j] = False\n",
    "    return [k for (k,trueprime) in enumerate(primes) if trueprime]\n",
    "\n",
    "def true_prime ():#find all prime can be use\n",
    "    true_prime_set = set()\n",
    "    num = {\"1\",\"3\",\"7\",\"9\"}\n",
    "    for a in primes(1000000):\n",
    "        if set(str(a)) <= num:\n",
    "            true_prime_set.add(a)\n",
    "    return true_prime_set\n",
    "\n",
    "def main ():#use circular to check the true prime\n",
    "    res_set = true_prime()\n",
    "    for x in res_set:\n",
    "        y = circular(x)\n",
    "        for z in y:\n",
    "            if isprime(z) == False:\n",
    "                res_set = res_set-y\n",
    "                break\n",
    "    return len(res_set)+2\n",
    "\n",
    "main()"
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