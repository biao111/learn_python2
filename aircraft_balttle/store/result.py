import constants


class PlayRest(object):
    ''' 统计游戏结果 '''
    _score = 0      #总分
    _life = 3       #生命
    _blood = 1000   #生命值

    @property
    def score(self):
        ''' 单次游戏分数'''
        return self._score

    @score.setter
    def score(self,value):
        ''' 设置游戏分数 '''
        if value < 0:
            return None
        self._score = value

    def set_history(self):
        ''' 记录游戏最高分 '''
        #1.读取文件中的存储的分数
        #2.如果新的分数比文件中的分数要大，则进行存储
        # 如果小于文件的分数，不需要处理
        #3.存取分数是替换模式w，而不是追加模式a+
        if int(self.get_max_core()) < self.score:
            with open(constants.PLAY_RESULT_STORE_FILE,'w') as f:
                f.write('{0}'.format(self.score))

    def get_max_core(self):
        ''' 读取历史记录最高分'''
        rest = 0
        with open(constants.PLAY_RESULT_STORE_FILE,'r') as f:
            r = f.read()
            if r:
                rest = r
        return rest