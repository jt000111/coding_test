def solution(new_id):
    #STEP 1  전부 소문자로 바꾸기
    new_id1 = new_id.lower()

    #2단계 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    import re

    new_id2 = re.sub(r'[^a-z0-9-._]','',new_id1)

    #3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    index_list = []
    new_id2 = list(new_id2)
    for i in range(len(new_id2)-1):
        if new_id2[i] == new_id2[i+1] and ".":
            index_list.append(i)

    for j in range(len(index_list)):
        new_id2[index_list[j]] = ""

    new_id3 = "".join(new_id2)
    #4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if new_id3[0] == ".":
        new_id4 = new_id3[1:]
    elif new_id3[len(new_id3)-1] == ".":
        new_id4 = new_id3[:len(new_id3)-1]
    else:
        new_id4 = new_id3

    #5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    from string import ascii_lowercase

    alpha = list(ascii_lowercase)
    count = 0

    for i in range(len(alpha)):
        if alpha[i] in new_id4:
            count += 1
        elif alpha[i] not in new_id4:
            pass

    if count == 0:
        new_id5 = new_id4 + "a"
    else:
        new_id5 = new_id4

    #6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    ###만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.

    if len(new_id5) > 15:
        if new_id5[14] == ".":
            new_id6 = new_id5[:14]
        elif new_id5[14] != ".":
            new_id6 = new_id5[:15]
    else:
        new_id6 = new_id5
    #7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(new_id6) < 3:
        last_word = new_id6[len(new_id6)-1]
        add = len(new_id6)
        new_id7 = new_id6 + last_word * (3-add)
    else:
        new_id7 = new_id6

    answer = new_id7
    return answer
