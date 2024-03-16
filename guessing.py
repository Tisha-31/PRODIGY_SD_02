{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38f76a7d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to the guessing game!\n",
      "I've picked a number between 1 and 100. Can you guess it?\n",
      "Enter your guess: 32\n",
      "Too low, try again!\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "def guessing_game():\n",
    "    number = random.randint(1, 100)\n",
    "    attempts = 0\n",
    "    \n",
    "    print(\"Welcome to the guessing game!\")\n",
    "    print(\"I've picked a number between 1 and 100. Can you guess it?\")\n",
    "    \n",
    "    while True:\n",
    "        guess = int(input(\"Enter your guess: \"))\n",
    "        attempts += 1\n",
    "        \n",
    "        if guess < number:\n",
    "            print(\"Too low, try again!\")\n",
    "        elif guess > number:\n",
    "            print(\"Too high, try again!\")\n",
    "        else:\n",
    "            print(f\"Congratulations! You've guessed the number in {attempts} attempts!\")\n",
    "            break\n",
    "\n",
    "guessing_game()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f95f3385",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
