class Stats:
    '''Остлеживание статистики'''

    def __init__(self):
        '''Инициализирует статистику'''
        self.reset_stats()

    def reset_stats(self):
        '''статистика изменяющаяся во время игры'''
        self.guns_left = 3