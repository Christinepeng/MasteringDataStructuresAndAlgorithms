import random


class Solution:
    def parse_file(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        lines = [line.strip() for line in lines]

        lst = []
        block = []
        for i, line in enumerate(lines):
            if line != '%':
                block.append(line)
            else:
                lst.append(block)
                block = []
        if block:
            lst.append(block)
        return lst

    def fortune_unix(self, filename):
        lst = self.parse_file(filename)
        num = random.randint(0, len(lst) - 1)
        return '\n'.join(lst[num])


def main():
    sol = Solution()
    print(sol.fortune_unix(filename='fortunes.txt'))


if __name__ == '__main__':
    main()