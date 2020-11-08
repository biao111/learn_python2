from colorama import Fore,Style
from getpass import getpass
from service.user_service import UserService
from service.news_service import NewsService
from service.role_service import RoleService
from service.type_service import TypeService
import os
import sys
import time

__user_service = UserService()
__news_service = NewsService()
__role_service = RoleService()
__type_service = TypeService()

while True:
    os.system("cls")
    print(Fore.LIGHTBLUE_EX,"\n\t===================")
    print(Fore.LIGHTBLUE_EX,"\n\t欢迎来到新闻管理系统")
    print(Fore.LIGHTBLUE_EX, "\n\t===================")
    print(Fore.LIGHTGREEN_EX,"\n\t1.登陆系统")
    print(Fore.LIGHTGREEN_EX,"\n\t2.退出系统")
    print(Style.RESET_ALL)
    op = input("\n\t输入操作编号：")
    #登录系统
    if op == "1":
        os.system("cls")
        username = input("\n\t请您输入用户账号:")
        password = getpass("\n\t请您输入用户密码:")
        result = __user_service.login(username,password)
        #登陆成功
        if result == True:
            #查询角色
            role = __user_service.search_user_role(username)

            while True:
                os.system("cls")
                if role == "新闻编辑":
                    print(Fore.LIGHTGREEN_EX, "\n\t1.发表新闻")
                    print(Fore.LIGHTGREEN_EX, "\n\t2.编辑新闻")
                    print(Fore.LIGHTGREEN_EX, "\n\tback.退出登录")
                    print(Fore.LIGHTGREEN_EX, "\n\texit.退出系统")
                    print(Style.RESET_ALL)
                    opt = input("\n\t输入操作编号：")
                    if opt == "1":
                        os.system("cls")
                        title = input("\n\t新闻标题:")
                        userid = __user_service.search_userid(username)
                        result  = __type_service.search_list()
                        for index in range(len(result)):
                            one = result[index]
                            print(Fore.LIGHTBLUE_EX, "\n\t%d.%s" % (index + 1, one[1]))
                        print(Style.RESET_ALL)
                        opt = input("\n\t输入角色编号：")
                        type_id = result[int(opt) - 1][0]
                        #TODO 新闻正文
                        path = input("\n\t请输入文件的路径:")
                        file = open(path,"r",encoding='utf-8')
                        content = file.read()
                        file.close()
                        is_top = input("\n\t置顶的级别(0-5):")
                        is_commit = input("\n\t是否提交(Y/N):")
                        if is_commit == "Y" or is_commit == "y":
                            __news_service.insert(title,userid,type_id,content,is_top)
                            print("\n\t提交成功！（3秒自动返回）")
                            time.sleep(3)
                    elif opt == "2":
                        page = 1
                        while True:
                            os.system("cls")
                            count_page = __news_service.search_count_page()
                            result = __news_service.search_list(page)
                            for index in range(len(result)):
                                one = result[index]
                                print(Fore.LIGHTBLUE_EX, "\n\t%d\t%s\t%s\t%s" % (index + 1, one[1], one[2], one[3]))
                            print(Fore.LIGHTBLUE_EX, "----------------")
                            print(Fore.LIGHTBLUE_EX, "{0}/{1}".format(page, count_page))
                            print(Fore.LIGHTBLUE_EX, "----------------")
                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                            print(Fore.LIGHTRED_EX, "\n\tprev.返回上一页")
                            print(Fore.LIGHTRED_EX, "\n\tnext.返回下一页")
                            print(Style.RESET_ALL)
                            opt = input("\n\t输入操作编号：")
                            if opt == "back":
                                break
                            elif opt == "prev" and page > 1:
                                page -= 1
                            elif opt == "next" and page < count_page:
                                page += 1
                            elif int(opt) >= 1 and int(opt) <= 10:
                                os.system("cls")
                                news_id = result[int(opt) - 1][0]
                                result = __news_service.search_by_id(news_id)
                                title = result[0]
                                type = result[1]
                                is_top = result[2]
                                print("\n\t新闻原标题：{0}".format(title))
                                new_title = input("\n\t新标题：")
                                print("\n\t原标题类型：{0}".format(type))
                                result = __type_service.search_list()
                                for index in range(len(result)):
                                    one = result[index]
                                    print(Fore.LIGHTBLUE_EX, "\n\t%d.%s" % (index + 1, one[1]))
                                print(Style.RESET_ALL)
                                opt = input("\n\t输入角色编号：")
                                type_id = result[int(opt) - 1][0]
                                #TODO 新闻正文
                                path = input("\n\t请输入文件的路径:")
                                file = open(path, "r",encoding='utf-8')
                                content = file.read()
                                file.close()
                                print("\n\t原置顶级别：{0}".format(is_top))
                                new_is_top = input("\n\t置顶级别（0-5）：")
                                is_commit = input("\n\t是否提交（Y/N）")
                                if is_commit == "Y" or is_commit == "y":
                                    __news_service.update(news_id,new_title,type_id,content,new_is_top)
                                    print("\n\t提交成功！三秒自动返回")
                                    time.sleep(3)
                    elif opt == "back":
                        break;
                    elif opt == "exit":
                        sys.exit(0)

                elif role == "管理员":
                    print(Fore.LIGHTGREEN_EX,"\n\t1.新闻管理")
                    print(Fore.LIGHTGREEN_EX,"\n\t2.用户管理")
                    print(Fore.LIGHTGREEN_EX,"\n\tback.退出登录")
                    print(Fore.LIGHTGREEN_EX,"\n\texit.退出系统")
                    print(Style.RESET_ALL)
                    opt = input("\n\t输入操作编号：")
                    os.system("cls")
                    if opt == "1":
                        print(Fore.LIGHTGREEN_EX, "\n\t1.新闻审批")
                        print(Fore.LIGHTGREEN_EX, "\n\t2.删除新闻")
                        print(Fore.LIGHTGREEN_EX, "\n\tback.返回上一层")
                        print(Style.RESET_ALL)
                        opt = input("\n\t输入操作编号：")
                        if opt == "1":
                            page = 1
                            while True:
                                os.system("cls")
                                count_page = __news_service.search_unreview_count_page()
                                result = __news_service.search_unreview_list(page)
                                for index in range(len(result)):
                                    one = result[index]
                                    print(Fore.LIGHTBLUE_EX,"\n\t%d\t%s\t%s\t%s"%(index+1,one[1],one[2],one[3]))
                                print(Fore.LIGHTBLUE_EX,"----------------")
                                print(Fore.LIGHTBLUE_EX,"{0}/{1}".format(page,count_page))
                                print(Fore.LIGHTBLUE_EX, "----------------")
                                print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                print(Fore.LIGHTRED_EX, "\n\tprev.返回上一页")
                                print(Fore.LIGHTRED_EX, "\n\tnext.返回下一页")
                                print(Style.RESET_ALL)
                                opt = input("\n\t输入操作编号：")
                                if opt == "back":
                                    break
                                elif opt == "prev" and page > 1:
                                    page -= 1
                                elif opt == "next" and page < count_page:
                                    page += 1
                                elif int(opt) >= 1 and int(opt) <= 10:
                                    news_id = result[int(opt) - 1][0]
                                    __news_service.update_unreview_news(news_id)
                                    result = __news_service.search_cache(news_id)
                                    title = result[0]
                                    username = result[1]
                                    type = result[2]
                                    content_id = result[3]
                                    #TODO 查找新闻正文
                                    content = __news_service.conetent_by_id(content_id)
                                    is_top = result[4]
                                    create_time = str(result[5])
                                    __news_service.cache_news(news_id,title,username,type,content,is_top,create_time)

                        elif opt == "2":
                            page = 1
                            while True:
                                os.system("cls")
                                count_page = __news_service.search_count_page()
                                result = __news_service.search_list(page)
                                for index in range(len(result)):
                                    one = result[index]
                                    print(Fore.LIGHTBLUE_EX,"\n\t%d\t%s\t%s\t%s"%(index+1,one[1],one[2],one[3]))
                                print(Fore.LIGHTBLUE_EX,"----------------")
                                print(Fore.LIGHTBLUE_EX,"{0}/{1}".format(page,count_page))
                                print(Fore.LIGHTBLUE_EX, "----------------")
                                print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                print(Fore.LIGHTRED_EX, "\n\tprev.返回上一页")
                                print(Fore.LIGHTRED_EX, "\n\tnext.返回下一页")
                                print(Style.RESET_ALL)
                                opt = input("\n\t输入操作编号：")
                                if opt == "back":
                                    break
                                elif opt == "prev" and page > 1:
                                    page -= 1
                                elif opt == "next" and page < count_page:
                                    page += 1
                                elif int(opt) >= 1 and int(opt) <= 10:
                                    news_id = result[int(opt) - 1][0]
                                    __news_service.delete_by_id(news_id)
                                    __news_service.delete_cache(news_id)

                        elif opt == "back":
                            break

                    elif opt == "2":
                        while True:
                            os.system("cls")
                            print(Fore.LIGHTGREEN_EX, "\n\t1.添加用户")
                            print(Fore.LIGHTGREEN_EX, "\n\t2.修改用户")
                            print(Fore.LIGHTGREEN_EX, "\n\t3.删除用户")
                            print(Fore.LIGHTGREEN_EX, "\n\tback.返回上一层")
                            print(Style.RESET_ALL)
                            opt = input("\n\t输入操作编号：")
                            if opt =="back":
                                os.system("cls")
                                break
                            elif opt == "1":
                                os.system("cls")
                                username = input("\n\t输入用户名：")
                                password = getpass("\n\t请输入密码：")
                                repassword = getpass("\n\t请再次输入密码：")
                                if password != repassword:
                                    print(Fore.LIGHTRED_EX,"请重新输入，三秒后自动返回！")
                                    print(Style.RESET_ALL)
                                    time.sleep(3)
                                    continue
                                email = input("\n\t输入邮箱：")
                                result = __role_service.search_list()
                                for index in range(len(result)):
                                    one = result[index]
                                    print(Fore.LIGHTBLUE_EX,"\n\t%d.%s"%(index+1,one[1]))
                                print(Style.RESET_ALL)
                                opt = input("\n\t输入角色编号：")
                                role_id = result[int(opt)-1][0]
                                __user_service.insert_user(username,password,email,role_id)
                                print(Fore.LIGHTRED_EX,"录入成功，三秒后自动返回！")
                                print(Style.RESET_ALL)
                                time.sleep(3)
                            elif opt == "2":
                                page = 1
                                while True:
                                    os.system("cls")
                                    count_page = __user_service.search_count_page()
                                    result = __user_service.search_list(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTBLUE_EX,
                                              "\n\t%d\t%s\t%s" % (index + 1, one[1], one[2]))
                                    print(Fore.LIGHTBLUE_EX, "----------------")
                                    print(Fore.LIGHTBLUE_EX, "{0}/{1}".format(page, count_page))
                                    print(Fore.LIGHTBLUE_EX, "----------------")
                                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTRED_EX, "\n\tprev.返回上一页")
                                    print(Fore.LIGHTRED_EX, "\n\tnext.返回下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t输入操作编号：")
                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page > 1:
                                        page -= 1
                                    elif opt == "next" and page < count_page:
                                        page += 1
                                    elif int(opt) >= 1 and int(opt) <= 10:
                                        os.system("cls")
                                        user_id = result[int(opt) - 1][0]
                                        username = input("\n\t新的用户名：")
                                        password = getpass("\n\t输入密码：")
                                        repassword = getpass("\n\t再次输入密码：")
                                        if password != repassword:
                                            print(Fore.LIGHTRED_EX,"\n\t输入的密码不正确，请重新输入！")
                                            print(Style.RESET_ALL)
                                            time.sleep(3)
                                            continue
                                        email = input("\n\t输入邮箱：")
                                        result = __role_service.search_list()
                                        for index in range(len(result)):
                                            one = result[index]
                                            print(Fore.LIGHTBLUE_EX, "\n\t%d.%s" % (index + 1, one[1]))
                                        print(Style.RESET_ALL)
                                        opt = input("\n\t输入角色编号：")
                                        role_id = result[int(opt) - 1][0]
                                        opt = input("是否保存（Y/N）")
                                        if opt == "Y" or opt == "y":
                                            __user_service.update_user(username,password,email,role_id,user_id)
                                            print(Fore.LIGHTRED_EX,"保存成功，三秒自动返回！")
                                            print(Style.RESET_ALL)
                                            time.sleep(3)
                            elif opt == "3":
                                page = 1
                                while True:
                                    os.system("cls")
                                    count_page = __user_service.search_count_page()
                                    result = __user_service.search_list(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTBLUE_EX,
                                              "\n\t%d\t%s\t%s" % (index + 1, one[1], one[2]))
                                    print(Fore.LIGHTBLUE_EX, "----------------")
                                    print(Fore.LIGHTBLUE_EX, "{0}/{1}".format(page, count_page))
                                    print(Fore.LIGHTBLUE_EX, "----------------")
                                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTRED_EX, "\n\tprev.返回上一页")
                                    print(Fore.LIGHTRED_EX, "\n\tnext.返回下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t输入操作编号：")
                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page > 1:
                                        page -= 1
                                    elif opt == "next" and page < count_page:
                                        page += 1
                                    elif int(opt) >= 1 and int(opt) <= 10:
                                        os.system("cls")
                                        user_id = result[int(opt) - 1][0]
                                        __user_service.delete_by_id(user_id)
                                        print(Fore.LIGHTRED_EX,"删除成功，三秒自动返回！")
                                        time.sleep(3)
                    elif opt == "back":
                        break
                    elif opt == "exit":
                        sys.exit(0)
        else:
            print("\n\t登录失败！！！3秒返回登录")
            time.sleep(3)
    elif op == "2":
        sys.exit(0)
