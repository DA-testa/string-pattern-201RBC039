# python3

B=17
Q=256

def read_input():
    actionChoose = input()
    if  "i" in actionChoose.lower():        
        patternInput = input()
        textData = input()

    elif "f" in actionChoose.lower():
        name = "./tests/06"
        with open(name, mode = "r") as f:
            patternInput = f.readline()
            textData = f.readline()
            
    return (patternInput.rstrip(), textData.rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    man =[]
    patternLn = len(pattern)
    hash_pattern_res = get_hash(patternLn)
    textLn = len(text)
    for j in range(0, textLn-patternLn+1):
        hash_text_res = get_hash(text[j:j+patternLn])
        if hash_pattern_res == hash_text_res:
            if pattern==text[j:j+patternLn]:
                man.append(j)

    return man


def get_hash(pattern) -> int:
    global B,Q
    patternLength = len(pattern)
    res = 0
    for i in range(patternLength):
        res = (B*res+ord(pattern[i]))%Q
    return res
    
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

