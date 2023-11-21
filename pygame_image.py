import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20231121/fig/pg_bg.jpg") #練習1
    kk_img = pg.image.load("ex01-20231121/fig/3.png") # 練習2
    kk_img = pg.transform.flip(kk_img, True, False) # 練習2
    bg_imgs = [bg_img, pg.transform.flip(bg_img, True, False)]
    kk_imgs = [kk_img,pg.transform.rotozoom(kk_img, 4, 1.0), pg.transform.rotozoom(kk_img, 7, 1.0), pg.transform.rotozoom(kk_img, 10, 1.0)] # 練習3
    tmr = 0
    while True:
        #a += 1
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        x = tmr%4800
        screen.blit(bg_imgs[0], [-x, 0]) #練習4
        screen.blit(bg_imgs[1], [1600-x, 0]) # 練習6
        screen.blit(bg_imgs[0], [3200-x, 0])
        screen.blit(bg_imgs[1], [4800-x, 0])
        screen.blit(kk_imgs[tmr%2], [300, 200]) # 練習5

        if tmr % 8 == 0 or tmr % 8 == 7 :
            screen.blit(kk_imgs[0], [300, 200])
        elif tmr % 8 == 1 or tmr % 8 == 6:
            screen.blit(kk_imgs[1], [300, 200])
        elif tmr % 8 == 2 or tmr % 8 == 5:
            screen.blit(kk_imgs[2], [300, 200])
        else:
            screen.blit(kk_imgs[3], [300, 200])

        pg.display.update()
        tmr += 1
        #x += 5        
        clock.tick(60)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()