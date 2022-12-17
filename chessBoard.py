import pygame
import time
import sys
pygame.init()


start_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
# start_fen = start_fen[::-1]

size = width, height = 800, 800
screen = pygame.display.set_mode(size)
# convert alpha does something about pixel collision but I think it also helps retain the transparent pixels of the image


white_colour = (250, 250, 250)
black_colour = (182, 137, 98)
# screen.fill(white_colour)

color = [black_colour, white_colour]

# for i in range(0,900,100):
# 	pygame.draw.line(screen, black_colour, (i,0), (i,800), 10)
# 	pygame.draw.line(screen, black_colour, (0,i), (800,i), 10)

rook_white = pygame.transform.scale(
    pygame.image.load("resources/rook_white.png"), (50, 50))
rook = pygame.transform.scale(
    pygame.image.load("resources/rook.png"), (50, 50))
knight_white = pygame.transform.scale(
    pygame.image.load("resources/knight_white.png"), (50, 50))
knight = pygame.transform.scale(
    pygame.image.load("resources/knight.png"), (50, 50))
bishop_white = pygame.transform.scale(
    pygame.image.load("resources/bishop_white.png"), (50, 50))
bishop = pygame.transform.scale(
    pygame.image.load("resources/bishop.png"), (50, 50))
king_white = pygame.transform.scale(
    pygame.image.load("resources/king_white.png"), (50, 50))
king = pygame.transform.scale(
    pygame.image.load("resources/king.png"), (50, 50))
queen_white = pygame.transform.scale(
    pygame.image.load("resources/queen_white.png"), (50, 50))
pawn_white = pygame.transform.scale(
    pygame.image.load("resources/pawn_white.png"), (50, 50))
queen = pygame.transform.scale(
    pygame.image.load("resources/queen.png"), (50, 50))
pawn = pygame.transform.scale(
    pygame.image.load("resources/pawn.png"), (50, 50))
# ima = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)


# creating piece index array for translating FEN string to board pieces

piece_index = dict(n=2, N=8, b=1, B=7, r=0, R=6,
                   q=3, Q=9, k=4, K=10, p=5, P=11)
pieces = [rook_white, knight_white, bishop_white, queen_white,
          king_white, pawn_white, rook, knight, bishop, queen, king, pawn]

pygame.display.flip()
# pygame.time.wait(10000)


class chess_board:

    # DRAWING THE BOARD-Took me hours wtf

    def draw_board():
        for y in range(0, 9):
            for x in range(0, 9):
                pygame.draw.rect(
                    screen, color[(y + x) % 2], pygame.Rect(x * 100, y * 100, 100, 100))
        pygame.display.flip()
                # print(color[y%2])
                # pygame.draw.rect(screen, color[y%2],pygame.Rect(y*100,x,100,100))

    # def draw_pieces(piece, coordinate):
    #     screen.blit(piece, coordinate)

    def read_fen(fen_string):
        coordinate = 0
        for i in fen_string:
            if(i > '0' and i < '9'):
                coordinate += int(i)
                print(i, " ", coordinate, end="\n")
                # print("  ")
            elif i == '/':
                coordinate += 1
            else:
                current_piece = pieces[piece_index[i]]

                # calculating x,y positions for pieces based on box number(coordinate)
                x = (coordinate % 9) * 100 + 20
                y = (800 - (int(coordinate / 9)) * 100) - 74
                coordinate += 1
                coordinate_pair = x, y
                screen.blit(current_piece, coordinate_pair)
                # pygame.display.flip()
                # pygame.event.wait(10000)

                # draw_pieces(current_piece, coordinate_pair)

    if __name__ == '__main__':
        draw_board()
        read_fen(start_fen)
        pygame.display.flip()
        for i in range(100000000): a=1

 #    def main():
	#     # screen = pygame.display.set_mode((640, 480))
	#     clock = pygame.time.Clock()
	#     while True:
	#         events = pygame.event.get()
	#         for e in events:
	#             if e.type == pygame.QUIT:
	#                 return

	#         clock.tick(60)
 #        draw_board()
 #        read_fen(start_fen)
 #        pygame.display.flip()

	# if __name__ == '__main__':
	#     main()



# Move the pieces according to user action
