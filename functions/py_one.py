def findFirstRepeated(integer_vector1, integer_vector2):
    size_vector1 = len(integer_vector1)
    size_vector2 = len(integer_vector2)

    # Just to do the smaller for-loop
    if size_vector1 < size_vector2:
        return compare_elements(integer_vector1,integer_vector2 )

    # The else contains also the case: sizes of the vectors are the same
    else:
        return compare_elements(integer_vector2, integer_vector1)


def compare_elements(vector_1, vector_2):
    for element in vector_1:
        if element in vector_2:
            return element
