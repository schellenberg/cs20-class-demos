def count_odds(a_list):
    # keep a running total of how many odd numbers we have seen -- accumulator pattern
    number_of_odds = 0
    # check each number in the list one at a time
    for num in a_list:
        # a number is odd if it leaves a remainder when divided by 2
        if num % 2 != 0:
            number_of_odds += 1
    return number_of_odds