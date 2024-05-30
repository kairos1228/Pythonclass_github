import os

file_path = 'score.bin'

if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        print('[파일 읽기]\n\n[점수 출력]')
        all_scores = file.read()
        print('개인점수:', all_scores)
else :
    print('[점수 입력]')
    scores = []
    for i in range(3):
        score = int(input(f'#{i+1}?'))
        if 0 <= score <= 100:
            scores.append(score)

    if scores:
        avg = sum(scores) / len(scores)
    else:
        avg = 0 

    with open(file_path, 'a', encoding='utf8') as file:
        if scores:
            file.write('개인점수: ')
            for i in range(len(scores)):
                if i != 0:
                    file.write(' ')
                file.write(str(scores[i]))
            file.write('\n')
            file.write(f'평균: {avg:.1f}\n')

    print('\n[점수 출력]')

    print('입력 점수:', scores)
    print('평균: %.1f' % avg)