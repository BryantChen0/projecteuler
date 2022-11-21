{
 "cells": [
  {
   "cell_type": "markdown",
   "source": [
    "By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.\n",
    "\n",
    "What is the 10 001st prime number?"
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
      "False\n",
      "104743\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "\n",
    "def is_prime(n):\n",
    "    if n==2:\n",
    "        return True\n",
    "    elif n % 2 ==0:\n",
    "        return False\n",
    "    else:\n",
    "        for i in range(2,int(math.sqrt(n)+1)):\n",
    "            if n % i ==0:\n",
    "                return False\n",
    "                break\n",
    "        else:\n",
    "            return True\n",
    "\n",
    "print(is_prime(9))\n",
    "\n",
    "n = 3\n",
    "i = 2\n",
    "while i < 10002:\n",
    "    if is_prime(n):\n",
    "        i += 1\n",
    "    n += 2\n",
    "print (n-2)"
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