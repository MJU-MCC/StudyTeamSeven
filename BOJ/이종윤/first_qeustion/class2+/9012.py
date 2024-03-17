#괄호

#한 쌍의 괄호 기호가 된 ()문자열은 기본 VPS라고 함
# VPS 인지 아닌지 판단해야함
# stack을 활용해서 '('를 넣는다.  ')'를 만나면 stack에 있는걸 pop을 한다.

def is_vps(sentence):
    stack=[]
    for word in sentence:
        if word =='(':
            stack.append(word)
        elif word==")":
            if not stack:
                return "NO"
            else:
                stack.pop()
    if stack:
        return "NO"
    else:
        return "YES"
t= int(input())
for _ in range(t):
    sentence=input()
    print(is_vps(sentence))