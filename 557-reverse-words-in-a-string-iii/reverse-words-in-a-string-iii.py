class Solution:
    def reverseWords(self, s: str) -> str:
        s2=s.split()
        s3=''
        for i in range(len(s2)):
            if i!=len(s2)-1:
                s3=s3+s2[i][::-1]+" "
            else:
                s3=s3+s2[i][::-1]
        return s3
            