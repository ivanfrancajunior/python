'''
Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.

https://edabit.com/challenge/gt9LLufDCMHKMioh2

'''

def stutter(word):
    stutteing = (f'{word[0]}{word[1]}...')
    return (f'{stutteing} {stutteing} {word}?')

print(stutter('bala'))


'''
Create a function that takes a number as input and returns True if the sum of its digits has the same parity as the entire number. Otherwise, return False.

https://edabit.com/challenge/jzCGNwLpmrHQKmtyJ

'''
def parity_analysis(number):
    replaceToNumbers = str(number)
    count = 0
    for alg in replaceToNumbers:
        count += int(alg)
    
    if count % 2 == 0:

        return True, count
     
    return False, count

print(parity_analysis(123))

'''
Create a function which concatenates the number 7 to the end of every chord in a list. Ignore all chords which already end with 7.

https://edabit.com/challenge/jhghtvT2s58FnDr5T

'''

def jazzify(notes):
    for note in notes:
        if note[len(note)-1] != '7':
            print(note + '7')
     
        else:
            print(note)


jazzify(["A", "C", "F7"])
