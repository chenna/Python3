#!/usr/bin/env python3
# 将一段字符以古文格式输出

# 方法1 参考自http://my.oschina.net/flynewton/blog/9989
def main(offset=6):
    string = '静夜思 李白床前明月光，疑是地上霜。举头望明月，低头思故乡。090131'
    a = [[' ']*offset for row in range(offset)]
    for i in range(offset):
        for j in range(offset):
            a[i][j] = string[j + i * offset]
    b = [[r[col] for r in a[::-1]] for col in range(len(a[0]))]
    print('\n'.join(['|'.join(c for c in row)for row in b]))

# 方法2 自己写的，更强壮
def testfunc(arg):
    if arg:
        return 1
    else:
        return 0
def main2(offset=6):
    string = '静夜思　李白床前明月光，疑是地上霜。举头望明月，低头思故乡。'
    for i in range(offset):
        k = len(string)//offset + testfunc(len(string)%offset)
        for j in range(k):
            if i + (k-1-j) * offset >= len(string):
                print('　'+'|',end='')
            else:
                print(string[i + (k-1-j) * offset]+'|',end='')
        print()

if __name__ == '__main__':
    for i in range(50):
        main2(i+1)
        print('************************')
