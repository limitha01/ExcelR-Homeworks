{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a6132ead-d1f7-488c-9e87-8d64aaa7c5cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a positive integer:  8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Numbers from 1 to 8 :\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "The sum of numbers from 1 to 8 is: 36\n"
     ]
    }
   ],
   "source": [
    "# Task 1: Using for and while loops\n",
    "\n",
    "# Step 1: Ask the user to enter a positive integer\n",
    "n = int(input(\"Enter a positive integer: \"))\n",
    "\n",
    "# Step 2: Use a for loop to print all numbers from 1 to n on separate lines\n",
    "print(\"Numbers from 1 to\", n, \":\")\n",
    "for i in range(1, n + 1):\n",
    "    print(i)\n",
    "\n",
    "# Step 3: Use a while loop to calculate the sum of all numbers from 1 to n\n",
    "sum_of_numbers = 0\n",
    "i = 1\n",
    "while i <= n:\n",
    "    sum_of_numbers += i\n",
    "    i += 1\n",
    "\n",
    "# Print the sum\n",
    "print(\"The sum of numbers from 1 to\", n, \"is:\", sum_of_numbers)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fa578abe-8d9e-4bdc-9c00-8870f3ff64e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a positive integer:  10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The square of 10 is: 100\n"
     ]
    }
   ],
   "source": [
    "# Task 2: Function to calculate square of a number\n",
    "\n",
    "# Step 1: Define the calculate_square function\n",
    "def calculate_square(n):\n",
    "    return n ** 2\n",
    "\n",
    "# Step 2: Ask the user to input a positive integer\n",
    "num = int(input(\"Enter a positive integer: \"))\n",
    "\n",
    "# Step 3: Call the calculate_square function and display the result\n",
    "square = calculate_square(num)\n",
    "print(\"The square of\", num, \"is:\", square)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "83dfdca7-36bf-41c8-a7f7-48cfef9bee5f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
