# The random module in Python provides a suite of 3_functions for generating random numbers,
# selecting random items, and performing various randomization tasks. It’s especially useful in
# applications that require random outcomes, such as games, simulations, and testing scenarios.

#           Key Functions in the random Module
#               1. Basic Random Number Generation
# random(): Returns a random floating-point number between 0.0 and 1.0.

import random
print(random.random())  # Output: 0.472, 0.985, etc.

# uniform(a, b): Returns a random floating-point number between a and b.

print(random.uniform(10, 20))  # Output: 12.45, 17.89, etc.

#                2. Generating Integers
# randint(a, b): Returns a random integer between a and b (inclusive).

print(random.randint(1, 6))  # Output: 1, 2, 3, 4, 5, or 6

# randrange(start, stop, step): Returns a random integer from the range created by start, stop,
# and step.

print(random.randrange(0, 101, 10))  # Output: 0, 10, 20, ..., 100

#                  3. Selecting Random Elements
# choice(sequence): Returns a random element from a non-empty sequence (e.g., list, tuple,
# or string).

colors = ['red', 'blue', 'green']
print(random.choice(colors))  # Output: 'red', 'blue', or 'green'

# choices(sequence, weights=None, k=1): Returns a list of k randomly selected elements, allowing
# for optional weighting.

print(random.choices(colors, k=2))  # Output: ['blue', 'green'], etc.

# sample(population, k): Returns a list of k unique elements from a sequence.

print(random.sample(range(1, 11), 3))  # Output: [7, 1, 9], etc.

#               4. Shuffling Elements
# shuffle(x): Shuffles the elements in the list x in place, modifying the original list.

deck = [1, 2, 3, 4, 5]
random.shuffle(deck)
print(deck)  # Output: [3, 1, 5, 2, 4], etc.

#                  5. Random Distributions
# The random module provides 3_functions to sample from common probability distributions:

# betavariate(alpha, beta): Returns a random float from a Beta distribution.
# expovariate(lambd): Returns a random float from an Exponential distribution.
# gammavariate(alpha, beta): Returns a random float from a Gamma distribution.
# gauss(mu, sigma): Returns a random float from a Gaussian (normal) distribution.
# triangular(low, high, mode): Returns a random float from a triangular distribution.
# vonmisesvariate(mu, kappa): Returns a random float from a von Mises distribution (circular).
# weibullvariate(alpha, beta): Returns a random float from a Weibull distribution.

#                  6. Seeding the Random Generator
# seed(a=None): Initializes the random number generator. If a is given, it uses that seed;
# otherwise, it uses the system time. Seeding makes random number generation predictable and
# reproducible.

random.seed(10)
print(random.random())  # Output: 0.5714025946899135, etc.
