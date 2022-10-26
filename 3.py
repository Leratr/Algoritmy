def numJewelsInStones(jewels, stone):
    count_jewels = 0
    for i in jewels:
        if i in stone:
            count_jewels += stone.count(i)
        return count_jewels

jewels = input("jewels: ")
stone = input("stone: ")
print(numJewelsInStones(jewels, stone))
