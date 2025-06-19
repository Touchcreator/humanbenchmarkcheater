
from hbc_tests.reaction_time_test import ReactionTimeTest
from hbc_tests.aim_trainer_test import AimTrainerTest

# init stuff
test_to_use = 0
tests = [1, 2]

print("Welcome to the Human Benchmark Cheater!")

print("What game would you like to cheat on?")

print("1. Reaction Time Test")
print("2. Aim Trainer Test")

while test_to_use not in tests:
    test_to_use = int(input("> "))

if test_to_use == 1:
    ReactionTimeTest.run()


if test_to_use == 2:
    AimTrainerTest.run()