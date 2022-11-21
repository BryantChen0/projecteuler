{
 "cells": [
  {
   "cell_type": "markdown",
   "source": [
    "The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.\n",
    "\n",
    "Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.\n",
    "\n",
    "(Please note that the palindromic number, in either base, may not include leading zeros.)"
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
   "execution_count": 41,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "872187\n"
     ]
    }
   ],
   "source": [
    "def decimal_to_binary(num):#reslut is string type\n",
    "    remain_num_reverse= \"\"\n",
    "    while num != 0:\n",
    "        remain = num % 2\n",
    "        num = num//2\n",
    "        remain_num_reverse += str(remain)\n",
    "    remain_num = remain_num_reverse[::-1]\n",
    "    return remain_num\n",
    "\n",
    "def palindromic_num (num_str):#reslut is string type\n",
    "    flip_num = num_str[::-1]\n",
    "    if flip_num == num_str:\n",
    "        return num_str\n",
    "\n",
    "sum = 0\n",
    "for i in range (1, 1000000):\n",
    "    if palindromic_num(str(i)) == str(i):\n",
    "        binary_i = decimal_to_binary(i)\n",
    "        if palindromic_num(binary_i) == binary_i:\n",
    "            sum += i\n",
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