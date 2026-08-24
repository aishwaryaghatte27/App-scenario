# Coin Change Problem
# Find the minimum number of coins required

coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter target amount: "))

# dp[i] = minimum coins needed to make amount i
dp = [float('inf')] * (amount + 1)

# 0 coins are needed to make amount 0
dp[0] = 0

for i in range(1, amount + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[amount] == float('inf'):
    print("Amount cannot be made using the given coins.")
else:
    print("Minimum number of coins:", dp[amount])
