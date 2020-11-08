

def test_div(num1,num2):
    ''' 当除数为0'''
    return num1 / num2

def test_file():
    ''' 读取文件'''
    try:
        f = open('test.txt','r',encoding='utf-8')
        rest = f.read()
        print(rest)
    except:
        print('error')
    finally:
        try:
            f.close()
            print('closed')
        except:
            pass

if __name__ == '__main__':
   # try:
   #    rest = test_div(5,"s")
   #    print(rest)
   # except (ZeroDivisionError,TypeError) as err:
   #   print('报错了')
   #   print(err)

   # except ZeroDivisionError:
   #     print('报错了，除数不能为0')
   # except TypeError:
   #     print('报错了，请输入数字')

   # rest = test_div(5, 0)
   # print(rest)

    test_file()