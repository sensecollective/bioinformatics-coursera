#!/usr/bin/env python

import sys
import math

def pad(s, l):
    return "A"*(l - len(s)) + s

def number_to_pattern(n):
    digits = "ACGT"
    base = 4
    if n < 0 or base < 2 or base > 36:
        return ""
    s = ""
    while 1:
        r = n % base
        s = digits[r] + s
        n = n / base
        if n == 0:
            break
    return s

seq = "ATCGTCAAATGGGTTCGAAAGCTCCCCTCCGGGCCTTAGCGGCCTGGAACGTCGGCTAGCCTTAACTTTGCACACGGCAGTCGTTTTCTAGACTGCAGGACAGGCCATAATTCTGTATGCTTACCGAACAGACACATCATTCCCTGAGTCTCTTTGGCCCGAGTAGGCCGATGGTAGTAGATCAGTGTGCAATTCGGCAGTTTTAAGTTTCATTGGGTGGGATATGCGGTTTTTCCTAAAGGCCATTGCAGAGCCTCTCCACGCCTCTGCAGTGTATGTCTCTCATGGCGTCAATAGAGTGCAGCTCATCCATCCATCGCTCTGACACAAAATGAGCCTCAGGGGATGTGGGGTGTTGCTCGGAACTCTACCGTCAAATTGGTGCTTAGAGGGTGGTATGGTCGCCCCAGCACCACGCGGTTATGTTGGATAGTCCGAAGCAGATTTGCAACGTACCTAGTCTCTATCGGGTCACTCCCTGGGAGGACCCGCCGAGACTCGGAGTCTATACAACGCTGTGCCCGGTGACCTGTCGCAATCCTTCAACTCCAGCAACAGCGTAGCTGACAATCTGTACCGAATTTGCTAGGTAACATGATTTGCGTGCGACGGGTGACCTGTCTTTGGCTGACCATAGTCCGGACGACGTTCTTTAGGGACGCCCGCTACGCGTCCAACGAGTCAGTGCGCATTCATGTAGTATGCGCGATAGTATATTTTCTCCTAAATCTTGGAGCAATTTTACCGCCGCACCGTCTGGGCGGATACGGGTACCAGCGGC"
#seq = "GGAGGTGCCGTTCAGCAAAGTCCTTTTCTCTCTACGCAACCGCCCGAAGAAAGGGGAACGCGCATAAATGGATTCTCTGATAGGTTAACTCCGCAGCTTCGGGGTGGTTGAAGCGAACCCGAGTATGCTAAGCAGACTTCGCGGGAGGCGATTATTGGATTGTCCTTGAAAATATCTCTATTAAATGGTACGAAAACCGACCGAAAATTACGGGAGGACCAGCGCATCTGCGGGTGCAAGGTAAGCAACACAGCGCTAGTCCGTAGTTTGAGTGGATACCAAGTAGTTGAAACGGATACTGTCAATCGTATGGAAGGACAGGGTGAAACGTATTAGTAGTTGTGCAAGACCGCTTGTCACGTTACCTGAATAATGGGTCCGTAACCTGGAGGGAGATGGCATCGGTGAAGCGATACGAGTCTGGGACTCCCGTGTCAACCCCCGCCCGCATCTCATCGTCAGACTTGAAATTTGGCATTGAACAATAGCCAAACCTGATGATCACACTGCTGTCAGGCCTTATTACCATAACCCAAAGGACAAAGACAGCCCTCTAAGAAAAGTCAGCGTAAATCTATGCTGTAATGCAGTTGCCGCATTTCCCCAAAGCGTGCTGTCCTTATCAGGATGACCACCGGGTTCCCCAAGTTCTAGCTCGTAGTTCATAGGGGATCACGACTCCCGTCCGGTTAGCT"

k = 8#int(sys.argv[2])

mers = {}

for n in range(0, int(math.pow(4, k))):
   mers[pad(number_to_pattern(n),k)] = 0

for i in xrange(len(seq)-(k-1)):
    x = seq[i:i+k]
    print x
    mers[x] += 1
    print mers[x]

print mers

#print mers
answer = ""

for n in sorted(mers):
    print "n: {0}, mers[n]: {1}".format(n, mers[n])
    answer += str(mers[n]) + " "

print answer
