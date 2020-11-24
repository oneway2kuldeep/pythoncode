# Given a string, determine if a permutation of the string could form a palindrome.

def is_palindrome_permutation(s):
    s = s.replace(' ', '')
    my_dict = {}
    for i in s:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    
    odd_count = 0
    for k, v in my_dict.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

print(is_palindrome_permutation('code'))


