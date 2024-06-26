#
def fib(n,k):
# Initialize the ages list with 1 followed by (k-1) zeros
# This represents the number of rabbit pairs at each age
  ages = [1] + [0]*(k-1)
  # Loop through each month
  for i in range(n-1):
    # Calculate the number of new pairs born (sum of all pairs of age 1 to k-1)
    # Shift the age list to the right and add the new pairs at the beginning
    ages = [sum(ages[1:])] + ages[:-1]
    # Return the total number of rabbit pairs after n months
  return sum(ages)

# %%
print(fib(98,19))




