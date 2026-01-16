class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        
        volwels = "aeiouAEIOU"
        words = sentence.split()
        new_sentence = []

        for i, word in enumerate(words): 
            if word[0] in volwels:
                new_word = word + "ma"
                new_word = new_word + ("a" * (i+1))
            else :
                new_word = word[1:] + word[0] + "ma"
                new_word = new_word + ("a" * (i+1))

            new_sentence.append(new_word)

        return " ".join(new_sentence)
