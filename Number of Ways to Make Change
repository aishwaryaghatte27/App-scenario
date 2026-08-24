# Number of Ways to Make Change
# Find the total number of combinations

coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter target amount: "))

# dp[i] = number of ways to make amount i
dp = [0] * (amount + 1)

# There is one way to make amount 0: choose no coins
dp[0] = 1

for coin in coins:
    for i in range(coin, amount + 1):
        dp[i] += dp[i - coin]

print("Total possible combinations:", dp[amount])
