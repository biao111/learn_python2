import pygame
import sys

import constants
from game.plane import OurPlane, SmallEnemyPlane
from store.result import PlayRest


class PlaneWar(object):
    ''' 飞机大战 '''

    READY = 0       #游戏准备中
    PLAYING = 1     #游戏中
    OVER = 2        #游戏结束
    status = READY  # 游戏的状态： 0.准备中 1. 游戏中  3.游戏结束

    # 我方飞机
    our_plane = None

    frame = 0  # 播放的帧数
    # 一架飞机可以属于多个精灵组
    small_enemies = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    #游戏结果
    rest = PlayRest()

    def __init__(self):
        #初始化游戏
        pygame.init()
        # 屏幕宽度，高度
        self.width, self.height = 480, 852

        # 屏幕对象
        self.screen = pygame.display.set_mode((self.width, self.height))
        # 设置窗口标题
        pygame.display.set_caption('飞机大战')
        # 加载
        # 加载背景图片
        self.bg = pygame.image.load(constants.BG_IMG)
        self.bg_over = pygame.image.load(constants.BG_IMG_OVER)
        # bg_ready = pygame.image.load(constants.BG_IMG_READY)       #图片一样不用实现

        # 游戏的标题
        self.img_game_title = pygame.image.load(constants.IMG_GAME_TITLE)
        self.img_game_title_rect = self.img_game_title.get_rect()
        # 获取游戏标题的宽度和高度
        t_width, t_height = self.img_game_title.get_size()
        # 标题摆放的位置
        self.img_game_title_rect.topleft = (int((self.width - t_width) / 2),
                                       int(self.height / 2 - t_height))

        # 开始按钮
        self.btn_start = pygame.image.load(constants.IMG_GAME_START_BTN)
        self.btn_start_rect = self.btn_start.get_rect()
        # 获取按钮的宽度和高度
        btn_width, btn_height = self.btn_start.get_size()
        # 开始按钮摆放的位置
        self.btn_start_rect.topleft = (int((self.width - btn_width) / 2),
                                  int(self.height / 2 + btn_height))

        #游戏文字对象
        self.score_font = pygame.font.Font(constants.FONT_SCORE,32)

        # 加载背景音乐
        pygame.mixer.music.load(constants.BG_MUSIC)
        # 循环播放音乐
        pygame.mixer.music.play(-1)
        # 设置音量的大小
        pygame.mixer.music.set_volume(0.2)

        #我放飞机实例
        self.our_plane = OurPlane(self.screen, speed=4)

        self.clock = pygame.time.Clock()

        #上次按的键盘的某一键，用于控制飞机
        self.key_down = None

    def bind_event(self):
      ''' 绑定事件 '''

      # 1.监听事件
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              # 退出事件
              pygame.quit()
              sys.exit()
          elif event.type == pygame.MOUSEBUTTONDOWN:
              # 鼠标点击进入游戏
              # 游戏在准备中，才能进入 游戏
              if self.status == self.READY:
                  self.status = self.PLAYING
              elif self.status == self.OVER:
                  self.status = self.READY
                  self.add_small_enemies(6)
          elif event.type == pygame.KEYDOWN:
              # 键盘事件
              self.key_down = event.key
              # 游戏正在游戏中才需要控制键盘事件 ASWD
              if self.status == self.PLAYING:
                  if event.key == pygame.K_w or event.key == pygame.K_UP:
                      self.our_plane.move_up()
                  elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                      self.our_plane.move_down()
                  elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                      self.our_plane.move_left()
                  elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                      self.our_plane.move_right()
                  elif event.key == pygame.K_SPACE:
                      # 发射子弹
                      self.our_plane.shoot()

    def add_small_enemies(self,num):
        '''
        随即添加n架小型敌机
        :param num: 飞机产生的数量
        :return:
        '''
        # 随机添加六架小型飞机
        for i in range(num):
            plane = SmallEnemyPlane(self.screen, 4)
            plane.add(self.small_enemies, self.enemies)

    def run_game(self):
        ''' 游戏的主循环 '''
        #1.设置帧速率
        while True:
            self.clock.tick(60)
            self.clock.tick(60)
            self.frame += 1
            if self.frame >= 60:
                self.frame = 0
            # 2.绑定事件
            self.bind_event()

            #3.更新游戏的状态：
            if self.status == self.READY:
                # 游戏正在准备中
                # 3.绘制游戏状态
                # 3.1绘制背景图片
                self.screen.blit(self.bg, self.bg.get_rect())
                #标题
                self.screen.blit(self.img_game_title, self.img_game_title_rect)
                # 开始按钮
                self.screen.blit(self.btn_start, self.btn_start_rect)
                self.key_down = None
                self.rest.score = 0
            elif self.status == self.PLAYING:
                #游戏进行中
                #绘制背景
                self.screen.blit(self.bg,self.bg.get_rect())
                #绘制飞机
                self.our_plane.update(self)
                #绘制子弹
                self.our_plane.bullets.update(self)
                #绘制敌方飞机
                self.small_enemies.update()
                #绘制游戏分数
                score_text = self.score_font.render(
                    '得分:{0}'.format(self.rest.score),
                    False,
                    constants.TEXT_SCORE_COLOR
                    )
                self.screen.blit(score_text,score_text.get_rect())
            elif self.status == self.OVER:
                #游戏结束
                #游戏背景
                self.screen.blit(self.bg_over, self.bg_over.get_rect())
                #分数统计
                #1.绘制本次总分
                score_text = self.score_font.render(
                    '{0}'.format(self.rest.score),
                    False,
                    constants.TEXT_SCORE_COLOR
                )
                score_text_rect = score_text.get_rect()
                text_w,text_h = score_text.get_size()
                #改变文字位置
                score_text_rect.topleft = (
                    int( (self.width - text_h) / 2),
                    int(self.height / 2)
                )
                self.screen.blit(score_text, score_text_rect)
                #2.历史最高分
                score_his = self.score_font.render(
                    '{0}'.format(self.rest.get_max_core()),
                    False,
                    constants.TEXT_SCORE_COLOR
                )
                self.screen.blit(score_his,(150,40))


            # 4.更新屏幕
            pygame.display.flip()
