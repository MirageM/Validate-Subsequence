#Validate Subsequence
#Time Complexity: O(n) || Space Complexity: O(1)
def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if value == sequence[seqIdx]:
            seqIdx += 1
    return seqIdx == len(sequence)
    