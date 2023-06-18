def sortSentence(self, s: str) -> str:
        s=s.split()
        s=list(map(lambda x:x[0:len(x)-1],list(sorted(s,key=lambda x:int(x[-1])))))
        return ' '.join(s)
