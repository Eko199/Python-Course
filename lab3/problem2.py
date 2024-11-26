class Solution:
    def findWords(self, words):
        return [word for word in words
                        if (letters := set(word.lower())) <= set("qwertyuiop")
                            or letters <= set("asdfghjkl") 
                            or letters <= set("zxcvbnm")]