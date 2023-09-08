from itertools import product
def solution(word):
    word_list = ['A', 'E', 'I', 'O', 'U']
    vocab_list = []
    for i in range(1, 6):
        vocab_list += list(product(word_list, repeat = i))
    for idx, vocab in enumerate(vocab_list):
        temp = ''
        for s in vocab:
            temp += s
        vocab_list[idx] = temp
    print(vocab_list)
    vocab_list.sort() # 정렬
    answer = vocab_list.index(word)+1
    return answer
