{
 "cells": [
  {
   "cell_type": "markdown",
   "source": [
    "n! means n × (n − 1) × ... × 3 × 2 × 1\n",
    "\n",
    "For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,\n",
    "and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.\n",
    "\n",
    "Find the sum of the digits in the number 100!"
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
   "execution_count": 6,
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'int' object is not iterable",
     "output_type": "error",
     "traceback": [
      "\u001B[1;31m---------------------------------------------------------------------------\u001B[0m",
      "\u001B[1;31mTypeError\u001B[0m                                 Traceback (most recent call last)",
      "Input \u001B[1;32mIn [6]\u001B[0m, in \u001B[0;36m<cell line: 11>\u001B[1;34m()\u001B[0m\n\u001B[0;32m      8\u001B[0m         \u001B[38;5;28msum\u001B[39m \u001B[38;5;241m+\u001B[39m\u001B[38;5;241m=\u001B[39m \u001B[38;5;28mint\u001B[39m(i)\n\u001B[0;32m      9\u001B[0m     \u001B[38;5;28;01mreturn\u001B[39;00m \u001B[38;5;28msum\u001B[39m\n\u001B[1;32m---> 11\u001B[0m \u001B[43mmain\u001B[49m\u001B[43m(\u001B[49m\u001B[43m)\u001B[49m\n",
      "Input \u001B[1;32mIn [6]\u001B[0m, in \u001B[0;36mmain\u001B[1;34m()\u001B[0m\n\u001B[0;32m      5\u001B[0m res \u001B[38;5;241m=\u001B[39m fac(\u001B[38;5;241m100\u001B[39m)\n\u001B[0;32m      6\u001B[0m str_res \u001B[38;5;241m=\u001B[39m \u001B[38;5;28mstr\u001B[39m(res)\n\u001B[1;32m----> 7\u001B[0m \u001B[38;5;28;01mfor\u001B[39;00m i \u001B[38;5;129;01min\u001B[39;00m res:\n\u001B[0;32m      8\u001B[0m     \u001B[38;5;28msum\u001B[39m \u001B[38;5;241m+\u001B[39m\u001B[38;5;241m=\u001B[39m \u001B[38;5;28mint\u001B[39m(i)\n\u001B[0;32m      9\u001B[0m \u001B[38;5;28;01mreturn\u001B[39;00m \u001B[38;5;28msum\u001B[39m\n",
      "\u001B[1;31mTypeError\u001B[0m: 'int' object is not iterable"
     ]
    }
   ],
   "source": [
    "from math import factorial as fac\n",
    "\n",
    "def main():\n",
    "    sum = 0\n",
    "    res = fac(100)\n",
    "    str_res = str(res)\n",
    "    for i in str_res:\n",
    "        sum += int(i)\n",
    "    return sum\n",
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