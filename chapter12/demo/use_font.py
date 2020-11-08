#引包
import sys,pygame

#初始化pygame
pygame.init()

#屏幕显示
screen = pygame.display.set_mode((500,500))

#加载字体
#['arial', 'arialblack', 'bahnschrift', 'calibri', 'cambriacambriamath', 'cambria', 'candara', 'comicsansms', 'consolas', 'constantia', 'corbel', 'couriernew', 'ebrima', 'franklingothicmedium', 'gabriola', 'gadugi', 'georgia', 'impact', 'inkfree', 'javanesetext', 'leelawadeeui', 'leelawadeeuisemilight', 'lucidaconsole', 'lucidasans', 'malgungothic', 'malgungothicsemilight', 'microsofthimalaya', 'microsoftjhengheimicrosoftjhengheiui', 'microsoftjhengheimicrosoftjhengheiuibold', 'microsoftjhengheimicrosoftjhengheiuilight', 'microsoftnewtailue', 'microsoftphagspa', 'microsoftsansserif', 'microsofttaile', 'microsoftyaheimicrosoftyaheiui', 'microsoftyaheimicrosoftyaheiuibold', 'microsoftyaheimicrosoftyaheiuilight', 'microsoftyibaiti', 'mingliuextbpmingliuextbmingliuhkscsextb', 'mongolianbaiti', 'msgothicmsuigothicmspgothic', 'mvboli', 'myanmartext', 'nirmalaui', 'nirmalauisemilight', 'palatinolinotype', 'segoemdl2assets', 'segoeprint', 'segoescript', 'segoeui', 'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric', 'segoeuisemibold', 'segoeuisemilight', 'segoeuisymbol', 'simsunnsimsun', 'simsunextb', 'sitkasmallsitkatextsitkasubheadingsitkaheadingsitkadisplaysitkabanner', 'sitkasmallsitkatextboldsitkasubheadingboldsitkaheadingboldsitkadisplayboldsitkabannerbold', 'sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic', 'sitkasmallsitkatextitalicsitkasubheadingitalicsitkaheadingitalicsitkadisplayitalicsitkabanneritalic', 'sylfaen', 'symbol', 'tahoma', 'timesnewroman', 'trebuchetms', 'verdana', 'webdings', 'wingdings', 'yugothicyugothicuisemiboldyugothicuibold', 'yugothicyugothicuilight', 'yugothicmediumyugothicuiregular', 'yugothicregularyugothicuisemilight', 'dengxian', 'fangsong', 'kaiti', 'simhei', 'holomdl2assets', 'acaslonproboldopentype', 'acaslonprobolditalicopentype', 'acaslonproitalicopentype', 'acaslonproregularopentype', 'acaslonprosemiboldopentype', 'acaslonprosemibolditalicopentype', 'adobefangsongstdregularopentype', 'adobefanheitistdboldopentype', 'adobegothicstdboldopentype', 'adobeheitistdregularopentype', 'adobekaitistdregularopentype', 'adobenaskhmediumopentype', 'agaramondproboldopentype', 'agaramondprobolditalicopentype', 'agaramondproitalicopentype', 'agaramondproregularopentype', 'birchstdopentype', 'blackoakstdopentype', 'brushscriptstdopentype', 'chaparralproboldopentype', 'chaparralprobolditopentype', 'chaparralproitalicopentype', 'chaparralprolightitopentype', 'chaparralproregularopentype', 'charlemagnestdboldopentype', 'cooperblackstditalicopentype', 'cooperblackstdopentype', 'giddyupstdopentype', 'hobostdopentype', 'kozgoproboldopentype', 'kozgoproextralightopentype', 'kozgoproheavyopentype', 'kozgoprolightopentype', 'kozgopromediumopentype', 'kozgoproregularopentype', 'kozminproboldopentype', 'kozminproextralightopentype', 'kozminproheavyopentype', 'kozminprolightopentype', 'kozminpromediumopentype', 'kozminproregularopentype', 'lithosproblackopentype', 'lithosproregularopentype', 'mesquitestdopentype', 'minionproboldcnopentype', 'minionproboldcnitopentype', 'minionpromediumopentype', 'minionpromediumitopentype', 'minionprosemiboldopentype', 'minionprosemibolditopentype', 'myriadarabicopentype', 'nuevastdboldopentype', 'nuevastdboldcondopentype', 'nuevastdboldconditalicopentype', 'nuevastdcondopentype', 'nuevastdconditalicopentype', 'nuevastditalicopentype', 'ocrastdopentype', 'oratorstdslantedopentype', 'oratorstdopentype', 'poplarstdopentype', 'prestigeelitestdbdopentype', 'rosewoodstdregularopentype', 'stencilstdopentype', 'tektonproboldopentype', 'tektonproboldcondopentype', 'tektonproboldextopentype', 'tektonproboldoblopentype', 'trajanproboldopentype', 'trajanproregularopentype', 'adobearabicboldopentype', 'adobearabicbolditalicopentype', 'adobearabicitalicopentype', 'adobearabicregularopentype', 'adobedevanagariboldopentype', 'adobedevanagaribolditalicopentype', 'adobedevanagariitalicopentype', 'adobedevanagariregularopentype', 'adobehebrewboldopentype', 'adobehebrewbolditalicopentype', 'adobehebrewitalicopentype', 'adobehebrewregularopentype', 'adobemingstdlightopentype', 'adobemyungjostdmediumopentype', 'adobesongstdlightopentype', 'kozgopr6nboldopentype', 'kozgopr6nextralightopentype', 'kozgopr6nheavyopentype', 'kozgopr6nlightopentype', 'kozgopr6nmediumopentype', 'kozgopr6nregularopentype', 'kozminpr6nboldopentype', 'kozminpr6nextralightopentype', 'kozminpr6nheavyopentype', 'kozminpr6nlightopentype', 'kozminpr6nmediumopentype', 'kozminpr6nregularopentype', 'lettergothicstdboldopentype', 'lettergothicstdboldslantedopentype', 'lettergothicstdslantedopentype', 'lettergothicstdopentype', 'minionproboldopentype', 'minionprobolditopentype', 'minionproitopentype', 'minionproregularopentype', 'myriadhebrewopentype', 'myriadproboldopentype', 'myriadproboldcondopentype', 'myriadproboldconditopentype', 'myriadprobolditopentype', 'myriadprocondopentype', 'myriadproconditopentype', 'myriadproitopentype', 'myriadproregularopentype', 'myriadprosemiboldopentype', 'myriadprosemibolditopentype', 'century', 'wingdings2', 'wingdings3', 'bookantiqua', 'garamond', 'monotypecorsiva', 'bookmanoldstyle', 'bookshelfsymbol7', 'msreferencesansserif', 'msreferencespecialty', 'fzshuti', 'fzyaoti', 'lisu', 'stcaiyun', 'stfangsong', 'sthupo', 'stkaiti', 'stliti', 'stsong', 'stxihei', 'stxingkai', 'stxinwei', 'stzhongsong', 'youyuan', 'extra', 'arialms']

fonts = pygame.font.get_fonts()
print(fonts)
red = pygame.Color(255, 0, 0)

#加粗 斜体
#方式一：使用系统默认的字体加载
#font = pygame.font.SysFont('youyuan',40)
#方式二：自己准备文件ttf，放到项目里
font = pygame.font.Font('./static/STCAIYUN.TTF',40)

#字体对象
text = font.render('得分',True,red)

#加载音乐
bg_music = pygame.mixer.music.load('./static/逆战.mp3')
#设置音量大小，范围：0-1
pygame.mixer.music.set_volume(0.5)
#循环播报背景音乐
pygame.mixer.music.play(-1)


#游戏主循环
while True:
    #处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #更新状态

    #绘制
    screen.blit(text,(20,20))
    pygame.display.flip()
