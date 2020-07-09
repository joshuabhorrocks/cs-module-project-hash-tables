def word_count(s):
    cache = {}
    bad_chars = ["\"", ":", ";", ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    count = 0

    lower_s = s.lower()

    for i in bad_chars:
        lower_s = lower_s.replace(i, "")
    fixed_s = lower_s.split()
    
    for x in fixed_s:
        for y in fixed_s:
            if x == y:
                count += 1
            else:
                pass
        cache.update(dict(zip({x}, {count})))
        count = 0
    return cache




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
