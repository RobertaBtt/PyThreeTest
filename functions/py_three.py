from bitarray import bitarray


def countChangeCoinInterval(coins: str):
    if coins !='':
        try:
            a = bitarray(coins)
            mask2 = buildMaskReguralIntervals(len(a), True)
            mask1 = buildMaskReguralIntervals(len(a), False)
            count_pattern1 = 0
            count_pattern2 = 0

            for key, value in enumerate(a):
                if value != mask1[key]:
                    count_pattern1 += 1

                if value != mask2[key]:
                    count_pattern2 += 1

            return min(count_pattern1, count_pattern2)
        except ValueError:
            pass
    return None


def buildMaskReguralIntervals(size: int, start_with: bool) -> bitarray:
    mask = bitarray(size)
    mask.setall(not start_with)
    mask[1:size:2] = start_with
    return mask


if __name__ == '__main__':
    #coins = '0110'
    #print(countChangeCoinInterval(coins))

    #coins = '10010000'
    #print(countChangeCoinInterval(coins))

#################################33
    # coins = '01101011'  #Mask bitarray('10101010') return 3
    # print(countChangeCoinInterval(coins))
    #
    # coins = '10010100' # Mask bitarray('10101010') return 5
    # print(countChangeCoinInterval(coins))

    #coins = '01101011'  #Mask bitarray('01010101') return 5
    #print(countChangeCoinInterval(coins))

    #coins = '10010100' # Mask bitarray('01010101') return 3
    #print(countChangeCoinInterval(coins))

    #coins = '0110'
    #print(countChangeCoinInterval(coins))

    coins = ''
    print(countChangeCoinInterval(coins))