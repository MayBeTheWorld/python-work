text = """
    As shown by the picture, the Internet is changing the way we communicate. In the cartoon setting, a man and a woman 
sit together and talk on their mobile phones. The objects in the background tell us they are in a bar or lounge-type 
atmosphere.
    The action taking place shows the two people exchanging messages with one another. As the conversation develops, the 
expressions on their faces and body language show that they are both excited and happy to be in each other's physical 
presence. There is a sense of connection and happy to be in each other's physical presence. There is a sense of 
connection and chemistry between them as they enjoy their evening out.
    Their relationship is likely built on their online correspondence but they appear to have taken it to the next level
by meeting in person. The use of messaging to communicate has allowed for initial projections of personalities and 
interests to develop without the pressures of a face-to-face interaction. However, it is only through physical 
interaction that deeper connections can be made.
    This situation highlights the concept of "love at first text", where people can form relationships based on online 
communication alone. Nonetheless, it is important to recognize the limitations of virtual communication and the value of
in-person interactions.
    In conclusion, where virtual communication has changed the way connect with others, ultimately physical interactions
are crucial to forming deep and meaningful relationships. We should embrace the advancement of technology while also 
cherishing and prioritizing time spent together in person.e and lowercase letters.
"""

word_count = {}

# 统计字符个数
for word in text:
    if word.isalnum():  # 判断字符是否为字母或数字
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

# 输出结果
for word, count in word_count.items():
    print(f"字符 '{word}': {count} 个")
