def minion_game(word):
    Kevin_scores = 0
    Stuart_scores = 0
    vowels = 'AEOUI'

    for i in range (len(word)):
        if  word[i] in vowels:
            Kevin_scores += len(word[i:])
        else:
            Stuart_scores += len(word[i:])
    

    if Stuart_scores > Kevin_scores:
        print(f'Stuart {Stuart_scores}')
    elif Stuart_scores < Kevin_scores:
        print(f'Kevin {Kevin_scores}')
    else:
        print('Draw')  


if __name__ == '__main__':
    s = input('input a word: ')
    minion_game(s)

# Note:
# computing len(string[i:]) every time is time consuming and makes our code not efficient.
# In Task29_v2 we will optmize the code to make it faster.