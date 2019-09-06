'''
X419-01: InClass Assignment 1
Write a program named reporter that reads stdin, takes the following command line arguments and
reports every time a given column in the input goes above a threshold n consecutive times:
reporter column threshold n
your program could be used as follow to parse periodic output by tools like vmstat:
vmstat | reporter column threshold n
Your tool must ignore heading lines like the ones shown below:
'''
# import sys
#
#
# def main(argv):
#     target_column = argv[0]
#     threshold = int(argv[1])
#     n = int(argv[2])
#
#     idx = 0
#     cnt = 0
#     # for i, line in enumerate(sys.stdin):
#     for i, line in enumerate(sys.stdin):
#         # print(line)
#         if i == 1:
#             lst = line.split()
#             # print(lst)
#             for s in lst:
#                 if s == target_column:
#                     break
#                 else:
#                     idx += 1
#         elif i > 1:
#             lst = line.split()
#             if len(lst) >= idx:
#                 if int(lst[idx]) > threshold:
#                     cnt += 1
#                     if cnt >= n:
#                         print('Out of threshold {N} times consecutively'.format(N = n))
#                         cnt = 0
#                 else:
#                     cnt = 0
#
#
# if __name__ == '__main__':
#     main(sys.argv[1:])
#
from sys import argv
from sys import stdin


def analyze(colname, threshold, n):
    stdin.readline()  # useless line
    idx = stdin.readline().split().index(colname)

    cnt = 0
    for line in stdin:
        val = int(line.split()[idx])
        if val >= threshold:
            cnt += 1
            if cnt >= n:
                print('Value {VAL} exceeds threshold {THRESHOLD} consecutively for {N} times'.format(VAL=val, THRESHOLD=threshold, N=n))
        else:
            cnt = 0


if __name__ == '__main__':
    if len(argv) != 4:
        raise Exception('Incorrect number of arguments.')
    else:
        analyze(argv[1], int(argv[2]), int(argv[3]))