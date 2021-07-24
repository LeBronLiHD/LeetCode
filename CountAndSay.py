# -*- coding: utf-8 -*-

class Solution(object):
    match_n_list = []
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        size_haved = len(self.match_n_list)
        for i in range(size_haved):
            if n == self.match_n_list[i][0] and len(self.match_n_list[i][1]) != 0:
                return self.match_n_list[i][1]

        if n == 1:
            return "1"
        else:
            last_str = self.countAndSay(n - 1)
        count = []  # docu the count of each digit number
        size = len(last_str)

        if size == 1:
            return "1" + last_str

        cur_char = last_str[0]
        last_char = last_str[0]
        right_index = 0
        left_index = 0

        for i in range(size):
            # if reaches the end, append and break
            # if non-equal, cut and
            cur_char = last_str[i]
            if cur_char != last_char:
                sub_str = last_str[left_index:right_index]
                count.append(sub_str)
                left_index = right_index
                last_char = cur_char
            if i == size - 1:
                sub_str = last_str[left_index:size]
                count.append(sub_str)
                break
            if cur_char == last_char and i < size - 1:
                right_index += 1

        list_size = len(count)
        ans_str = ""
        for i in range(list_size):
            ans_str += str(len(count[i]))
            ans_str += count[i][0]

        self.match_n_list.append([n, ans_str])

        return ans_str


def main():
    obj = Solution()
    for i in range(20):
        i += 1
        print(i, "  \t-> ", obj.countAndSay(i))


if __name__ == "__main__":
    main()