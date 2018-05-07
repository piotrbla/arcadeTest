import math
import random
import arcade
# import pygame
# from pygame.locals import *


def do_quit():
    arcade.quit()
    exit(0)


# pygame.init()
# pygame.mixer.init()
width, height = 640, 480
# screen = pygame.display.set_mode((width, height))
window = arcade.open_window(width, height, "Drawing Example")

keys = [False, False, False, False]
player_position = [100, 100]
acc = [0, 0]
arrows = []
bad_timer = 100
bad_timer_big = 0
bad_guys = [[640, 100]]
health_value = 194

player = arcade.Sprite("resources/images/dude.png")
grass = arcade.load_texture("resources/images/grass.png")
castle_1 = arcade.Sprite("resources/images/castle.png", center_y=50, center_x=50)
castle_2 = arcade.Sprite("resources/images/castle.png", center_y=155, center_x=50)
castle_3 = arcade.Sprite("resources/images/castle.png", center_y=260, center_x=50)
castle_4 = arcade.Sprite("resources/images/castle.png", center_y=365, center_x=50)
arrow = arcade.Sprite("resources/images/bullet.png")
bad_guy_image_1 = arcade.Sprite("resources/images/badguy.png")
bad_guy_image = bad_guy_image_1
health_bar = arcade.Sprite("resources/images/healthbar.png")
health = arcade.Sprite("resources/images/health.png")
game_over = arcade.Sprite("resources/images/gameover.png")
you_win = arcade.Sprite("resources/images/youwin.png")

hit = arcade.load_sound("resources/audio/explode.wav")
enemy = arcade.load_sound("resources/audio/enemy.wav")
shoot = arcade.load_sound("resources/audio/shoot.wav")
music = arcade.load_sound('resources/audio/moonlight.wav')
arcade.play_sound(music)

running = 1
exitcode = 0
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()
scale = 1.
for x in range(width // grass.width + 1):
    for y in range(height // grass.height + 1):
        arcade.draw_texture_rectangle(x*grass.width, y*grass.height, scale * grass.width, scale * grass.height, grass, 0)
castle_1.draw()
castle_2.draw()
castle_3.draw()
castle_4.draw()
arcade.finish_render()
arcade.run()
position = arcade.mouse.get_pos()
angle = math.atan2(position[1]-(player_position[1]+32),position[0]-(player_position[0]+26))
playerrot = arcade.transform.rotate(player, 360-angle*57.29)
#     playerpos1 = (player_position[0]-playerrot.get_rect().width/2, player_position[1]-playerrot.get_rect().height/2)
#     screen.blit(playerrot, playerpos1)
#     for bullet in arrows:
#         index = 0
#         velx = math.cos(bullet[0]) * 10
#         vely = math.sin(bullet[0]) * 10
#         bullet[1] += velx
#         bullet[2] += vely
#         if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
#             arrows.pop(index)
#         index += 1
#         for projectile in arrows:
#             arrow1 = arcade.transform.rotate(arrow, 360 - projectile[0] * 57.29)
#             screen.blit(arrow1, (projectile[1], projectile[2]))
#     if bad_timer == 0:
#         bad_guys.append([640, random.randint(50, 430)])
#         bad_timer = 100 - (bad_timer_big * 2)
#         if bad_timer_big >= 35:
#             bad_timer_big = 35
#         else:
#             bad_timer_big += 5
#     index = 0
#     for bad_guy in bad_guys:
#         if bad_guy[0] < -64:
#             bad_guys.pop(index)
#         bad_guy[0] -= 7
#         bad_rectangle = arcade.Rect(bad_guy_image.get_rect())
#         bad_rectangle.top = bad_guy[1]
#         bad_rectangle.left = bad_guy[0]
#         if bad_rectangle.left < 64:
#             hit.play()
#             health_value -= random.randint(5, 20)
#             bad_guys.pop(index)
#         # 6.3.2 - Check for collisions
#         index1 = 0
#         for bullet in arrows:
#             bullrect = arcade.Rect(arrow.get_rect())
#             bullrect.left = bullet[1]
#             bullrect.top = bullet[2]
#             if bad_rectangle.colliderect(bullrect):
#                 enemy.play()
#                 acc[0] += 1
#                 bad_guys.pop(index)
#                 arrows.pop(index1)
#             index1 += 1
#         index += 1
#     for bad_guy in bad_guys:
#         screen.blit(bad_guy_image, bad_guy)
#     font = arcade.font.Font(None, 24)
#     survived_text = font.render(str((90000 - arcade.time.get_ticks()) // 60000) + ":" + str(
#         (90000 - arcade.time.get_ticks()) // 1000 % 60).zfill(2), True, (0, 0, 0))
#     text_rectangle = survived_text.get_rect()
#     text_rectangle.topright = [635, 5]
#     screen.blit(survived_text, text_rectangle)
#     screen.blit(health_bar, (5, 5))
#     for health1 in range(health_value):
#         screen.blit(health, (health1 + 8, 8))
#     arcade.display.flip()
#     for key, v in window.key_downs.items:
#         if key == key.ESCAPE:
#             do_quit()
    #
        # if event.type == arcade.:
        #     if event.key == K_w:
        #         keys[0] = True
        #     elif event.key == K_a:
        #         keys[1] = True
        #     elif event.key == K_s:
        #         keys[2] = True
        #     elif event.key == K_d:
        #         keys[3] = True
        # if event.type == KEYUP:
        #     if event.key == K_w:
        #         keys[0] = False
        #     elif event.key == K_a:
        #         keys[1] = False
        #     elif event.key == K_s:
        #         keys[2] = False
        #     elif event.key == K_d:
        #         keys[3] = False
        #     elif event.key == K_ESCAPE:
        #         do_quit()
        #   if event.type == MOUSEBUTTONDOWN:
#             shoot.play()
#             position = arcade.mouse.get_pos()
#             acc[1] += 1
#             arrows.append(
#                 [math.atan2(position[1] - (playerpos1[1] + 32), position[0] - (playerpos1[0] + 26)), playerpos1[0] + 32,
#                  playerpos1[1] + 32])
#     if keys[0]:
#         player_position[1] -= 5
#     elif keys[2]:
#         player_position[1] += 5
#     if keys[1]:
#         player_position[0] -= 5
#     elif keys[3]:
#         player_position[0] += 5
#     bad_timer -= 1
#     if arcade.time.get_ticks() >= 90000:
#         running = 0
#         exitcode = 1
#     if health_value <= 0:
#         running = 0
#         exitcode = 0
#     if acc[1] != 0:
#         accuracy = acc[0] * 1.0 / acc[1] * 100
#     else:
#         accuracy = 0
#
# if exitcode == 0:
#     arcade.font.init()
#     font = arcade.font.Font(None, 24)
#     text = font.render("Accuracy: " + str(accuracy) + "%", True, (255, 0, 0))
#     text_rectangle = text.get_rect()
#     text_rectangle.centerx = screen.get_rect().centerx
#     text_rectangle.centery = screen.get_rect().centery + 24
#     screen.blit(game_over, (0, 0))
#     screen.blit(text, text_rectangle)
# else:
#     arcade.font.init()
#     font = arcade.font.Font(None, 24)
#     text = font.render("Accuracy: " + str(accuracy) + "%", True, (0, 255, 0))
#     text_rectangle = text.get_rect()
#     text_rectangle.centerx = screen.get_rect().centerx
#     text_rectangle.centery = screen.get_rect().centery + 24
#     screen.blit(you_win, (0, 0))
#     screen.blit(text, text_rectangle)
#
# while 1:
#     for event in arcade.event.get():
#         if event.type == QUIT:
#             do_quit()
#     arcade.display.flip()