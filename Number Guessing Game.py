{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f742deb0-e1f4-4da5-ba89-764718a326a5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "user input 99\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Computer number 4\n",
      "your guess is high ✌😎\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "Cnumber = random.randrange(1,101)\n",
    "Userinput = int(input(\"user input\"))\n",
    "if Userinput < Cnumber:\n",
    "                print(\"Computer number\", Cnumber)\n",
    "                print(\"your guess is low 😢\")\n",
    "elif Userinput > Cnumber:\n",
    "                print(\"Computer number\",Cnumber)\n",
    "                print(\"your guess is high ✌😎\")\n",
    "else:\n",
    "                print(\"Computer number\",Cnumber)    \n",
    "                print(\"your guess is equal ✌\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24c2ea8f-1f9d-4ed3-a61c-a59c30a0f7e9",
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
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
