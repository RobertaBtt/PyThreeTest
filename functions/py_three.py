from bitarray import bitarray


def countChangeCoinInterval(coins: str):
    if coins != '':
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

            # The two patters have both regular intervals,
            # but, depending on the coins, they may have more
            # changes to be calculated, so we take the minimum

            return min(count_pattern1, count_pattern2)
        except ValueError:
            raise ValueError
    return None


def buildMaskReguralIntervals(size: int, start_with: bool) -> bitarray:
    mask = bitarray(size)
    mask.setall(not start_with)
    mask[1:size:2] = start_with
    return mask

if __name__ == '__main__':


    # coins = '01101011'
    # #Mask bitarray('10101010') return 3
    # Mask bitarray('01010101') return 5

    coins = '0110'
    print(countChangeCoinInterval(coins))
