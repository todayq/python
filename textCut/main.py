import math,os



def main(num):
    with open('./name.txt', 'r') as n:
        namelines = n.readlines()
        if len(namelines)< num:
            print("没找到名字，或名字数量不够")
            return

        with open('./sb.txt', 'r') as f:
            lines = f.readlines()
            l = len(lines)
            one_list = []
            for i in range(num):
                one_list = lines[math.floor(i / num * l):math.floor((i + 1) / num * l)]
                with open("./第%d份-%s.txt" % (i + 1,namelines[i].replace('\n', '')), "w") as f:
                    f.write("".join(one_list))
                    print("第%d份-%s保存成功" % (i + 1,namelines[i].replace('\n', '')))



if __name__ == '__main__':

        print("请确认待分割文本为sb.txt\n请输入分割份数[Enter确认]\n")
        ii = input("份数：")
        main(int(ii))
        print("全部分割完成！回车退出\n")
        input()

