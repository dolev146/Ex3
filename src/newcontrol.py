import sys
import tkinter
import tkinter.filedialog
from threading import Timer
import pygame
from src.gui.Button import Button
import src.gui.constants
from src.gui.algo_func import tsp_ga, center_ga, reset_center, reset_tsp, shortest_ga, reset_shortest, \
    reset_shortest_string, reset_tsp_string
from src.gui.graph_func import add_node_g, reset_add_node_string, remove_node_g, reset_remove_node_string, \
    remove_edge_g, reset_remove_edge_string, add_edge_g, reset_add_edge_string


def prompt_file():
    """Create a Tk file dialog and cleanup when finished"""
    top = tkinter.Tk()
    top.withdraw()  # hide window
    file_name = tkinter.filedialog.askopenfilename(parent=top, initialdir="./data")
    top.destroy()
    return file_name

def GUI(file_name):
    src.gui.constants.ga.load_from_json(file_name=file_name)
    pygame.init()
    black = [0, 0, 0]
    white = [255, 255, 255]
    size = [src.gui.constants.width, src.gui.constants.height]
    window = pygame.display.set_mode(size)
    center_button = Button((150, 20, 30), 2, 2, 70, 20, 'center')
    load_button = Button((32, 150, 51), 400, 2, 70, 20, 'load')
    pygame.display.set_caption("EX3 Dolev Daniel Yakov")
    src.gui.constants.getminmax()
    src.gui.constants.calculate_values()
    clock = pygame.time.Clock()
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 10)
    base_font_tsp = pygame.font.Font(None, 20)
    input_rect_tsp = pygame.Rect(0, 25, 140, 20)
    color_active_tsp = (102, 51, 153)
    color_passive_tsp = (216, 191, 216)
    active_tsp = False

    base_font_shortest = pygame.font.Font(None, 20)
    input_rect_shortest = pygame.Rect(0, 50, 140, 20)
    color_active_shortest = (102, 51, 153)
    color_passive_shortest = (216, 191, 216)
    active_shortest = False

    base_font_add_node = pygame.font.Font(None, 20)
    input_rect_add_node = pygame.Rect(80, 1, 140, 20)
    color_active_add_node = (102, 51, 153)
    color_passive_add_node = (216, 191, 216)
    active_add_node = False

    base_font_remove_node = pygame.font.Font(None, 20)
    input_rect_remove_node = pygame.Rect(80, 22, 140, 20)
    color_active_remove_node = (102, 51, 153)
    color_passive_remove_node = (216, 191, 216)
    active_remove_node = False

    base_font_remove_edge = pygame.font.Font(None, 20)
    input_rect_remove_edge = pygame.Rect(180, 22, 140, 20)
    color_active_remove_edge = (102, 51, 153)
    color_passive_remove_edge = (216, 191, 216)
    active_remove_edge = False

    base_font_add_edge = pygame.font.Font(None, 20)
    input_rect_add_edge = pygame.Rect(180, 1, 140, 20)
    color_active_add_edge = (102, 51, 153)
    color_passive_add_edge = (216, 191, 216)
    active_add_edge = False

    base_font_node_loc = pygame.font.Font(None, 20)
    input_rect_node_loc = pygame.Rect(280, 1, 140, 20)
    color_active_node_loc = (102, 51, 153)
    color_passive_node_loc = (216, 191, 216)
    active_node_loc = False
    node_loc_font = pygame.font.Font(None, 20)

    base_font_edge_weight = pygame.font.Font(None, 20)
    input_rect_edge_weight = pygame.Rect(280, 22, 140, 20)
    color_active_edge_weight = (102, 51, 153)
    color_passive_edge_weight = (216, 191, 216)
    active_edge_weight = False
    edge_weight_font = pygame.font.Font(None, 20)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if active_tsp == True:
                    if event.key == pygame.K_BACKSPACE:
                        src.gui.constants.user_text_tsp = src.gui.constants.user_text_tsp[:-1]
                    elif event.key == pygame.K_RETURN:
                        cost = tsp_ga(src.gui.constants.user_text_tsp)
                        src.gui.constants.user_text_tsp = "{:.4f}".format(cost)
                        timeout = Timer(5.0, reset_tsp_string)
                        timeout.start()
                        active_tsp = False
                    else:
                        src.gui.constants.user_text_tsp += event.unicode

                if active_shortest == True:
                    if event.key == pygame.K_BACKSPACE:
                        src.gui.constants.user_text_shortest = src.gui.constants.user_text_shortest[:-1]
                    elif event.key == pygame.K_RETURN:
                        cost = shortest_ga(src.gui.constants.user_text_shortest)
                        src.gui.constants.user_text_shortest = "{:.4f}".format(cost)
                        timeout = Timer(5.0, reset_shortest_string)
                        timeout.start()
                        active_shortest = False
                    else:
                        src.gui.constants.user_text_shortest += event.unicode

                if active_add_node == True:
                    if event.key == pygame.K_BACKSPACE:
                        src.gui.constants.user_text_add_node = src.gui.constants.user_text_add_node[:-1]
                    elif event.key == pygame.K_RETURN:
                        cost = add_node_g(src.gui.constants.user_text_add_node)
                        src.gui.constants.user_text_add_node = str(cost)
                        timeout = Timer(2.0, reset_add_node_string)
                        timeout.start()
                        active_add_node = False
                        pygame.display.flip()
                    else:
                        src.gui.constants.user_text_add_node += event.unicode

                if active_remove_node == True:
                    if event.key == pygame.K_BACKSPACE:
                        src.gui.constants.user_text_remove_node = src.gui.constants.user_text_remove_node[:-1]
                    elif event.key == pygame.K_RETURN:
                        cost = remove_node_g(src.gui.constants.user_text_remove_node)
                        src.gui.constants.user_text_remove_node = str(cost)
                        timeout = Timer(2.0, reset_remove_node_string)
                        timeout.start()
                        active_remove_node = False
                        pygame.display.flip()
                    else:
                        src.gui.constants.user_text_remove_node += event.unicode

                if active_remove_edge == True:
                    if event.key == pygame.K_BACKSPACE:
                        src.gui.constants.user_text_remove_edge = src.gui.constants.user_text_remove_edge[:-1]
                    elif event.key == pygame.K_RETURN:
                        cost = remove_edge_g(src.gui.constants.user_text_remove_edge)
                        src.gui.constants.user_text_remove_edge = str(cost)
                        timeout = Timer(2.0, reset_remove_edge_string)
                        timeout.start()
                        active_remove_edge = False
                        pygame.display.flip()
                    else:
                        src.gui.constants.user_text_remove_edge += event.unicode

                if active_add_edge == True:
                    if event.key == pygame.K_BACKSPACE:
                        src.gui.constants.user_text_add_edge = src.gui.constants.user_text_add_edge[:-1]
                    elif event.key == pygame.K_RETURN:
                        cost = add_edge_g(src.gui.constants.user_text_add_edge)
                        src.gui.constants.user_text_add_edge = str(cost)
                        timeout = Timer(2.0, reset_add_edge_string)
                        timeout.start()
                        active_add_edge = False
                        pygame.display.flip()
                    else:
                        src.gui.constants.user_text_add_edge += event.unicode

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if center_button.isOver(pygame.mouse.get_pos()):
                    center_ga()
                if load_button.isOver(pygame.mouse.get_pos()):
                    path_str = prompt_file()
                    src.gui.constants.ga.load_from_json(path_str)
                    src.gui.constants.getminmax()
                    src.gui.constants.calculate_values()


                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect_tsp.collidepoint(event.pos):
                        active_tsp = True
                        src.gui.constants.user_text_tsp = ''
                    else:
                        active_tsp = False
                        src.gui.constants.user_text_tsp = 'tsp'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect_shortest.collidepoint(event.pos):
                        active_shortest = True
                        src.gui.constants.user_text_shortest = ''
                    else:
                        active_shortest = False
                        src.gui.constants.user_text_shortest = 'shortest'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect_add_node.collidepoint(event.pos):
                        active_add_node = True
                        src.gui.constants.user_text_add_node = ''
                    else:
                        active_add_node = False
                        src.gui.constants.user_text_add_node = 'add node'

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect_remove_node.collidepoint(event.pos):
                        active_remove_node = True
                        src.gui.constants.user_text_remove_node = ''
                    else:
                        active_remove_node = False
                        src.gui.constants.user_text_remove_node = 'remove node'

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect_remove_edge.collidepoint(event.pos):
                        active_remove_edge = True
                        src.gui.constants.user_text_remove_edge = ''
                    else:
                        active_remove_edge = False
                        src.gui.constants.user_text_remove_edge = 'remove edge'

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect_add_edge.collidepoint(event.pos):
                        active_add_edge = True
                        src.gui.constants.user_text_add_edge = ''
                    else:
                        active_add_edge = False
                        src.gui.constants.user_text_add_edge = 'add edge'

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect_node_loc.collidepoint(event.pos):
                        active_node_loc = not active_node_loc
                        if active_node_loc is False:
                            src.gui.constants.user_text_node_loc = 'hide location'
                        else:
                            src.gui.constants.user_text_node_loc = 'show location'

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect_edge_weight.collidepoint(event.pos):
                        active_edge_weight = not active_edge_weight
                        if active_edge_weight is False:
                            src.gui.constants.user_text_edge_weight = 'hide weight'
                        else:
                            src.gui.constants.user_text_edge_weight = 'show weight'

        window.fill(white)

        for ind in range(len(src.gui.constants.src_edge_list)):
            src_list = src.gui.constants.src_edge_list[ind]
            dest_list = src.gui.constants.dest_edge_list[ind]
            pygame.draw.line(window, black, [src_list[0], src_list[1]],
                             [dest_list[0], dest_list[1]])
            pygame.draw.polygon(window, [46, 139, 87], src.gui.constants.arrow_head_list[ind])
            if active_edge_weight is True:
                weight_str = "{:.2f}".format(src_list[2])
                x_pos = (src_list[0] + dest_list[0]) / 2
                y_pos = (src_list[1] + dest_list[1]) / 2
                edge_weight_surface = edge_weight_font.render(f"{weight_str}", True, black)
                window.blit(edge_weight_surface, (x_pos - 25, y_pos - 25))

        for nodeV in src.gui.constants.node_list:
            pygame.draw.circle(window, black, [nodeV[0], nodeV[1]], 10)
            textsurface = myfont.render(f"{nodeV[2]}", True, white)
            window.blit(textsurface, (nodeV[0] - 7, nodeV[1] - 5))

            if src.gui.constants.center_node == nodeV[2]:
                pygame.draw.circle(window, (26, 10, 166), [nodeV[0], nodeV[1]], 15)
                textsurface = myfont.render(f"{nodeV[2]}", True, white)
                window.blit(textsurface, (nodeV[0] - 7, nodeV[1] - 5))
                timeout = Timer(5.0, reset_center)
                timeout.start()

            if src.gui.constants.tsp_list is not None:
                if nodeV[2] in src.gui.constants.tsp_list:
                    pygame.draw.circle(window, (140, 64, 6), [nodeV[0], nodeV[1]], 10)
                    textsurface = myfont.render(f"{nodeV[2]}", True, white)
                    window.blit(textsurface, (nodeV[0] - 7, nodeV[1] - 5))
                    timeout2 = Timer(5.0, reset_tsp)
                    timeout2.start()

            if src.gui.constants.shortest_list is not None:
                if nodeV[2] in src.gui.constants.shortest_list:
                    pygame.draw.circle(window, (140, 64, 6), [nodeV[0], nodeV[1]], 10)
                    textsurface = myfont.render(f"{nodeV[2]}", True, white)
                    window.blit(textsurface, (nodeV[0] - 7, nodeV[1] - 5))
                    timeout2 = Timer(5.0, reset_shortest)
                    timeout2.start()

            if active_node_loc is False:
                pygame.draw.circle(window, black, [nodeV[0], nodeV[1]], 10)
                textsurface = myfont.render(f"{nodeV[2]}", True, white)
                window.blit(textsurface, (nodeV[0] - 7, nodeV[1] - 5))
                x_loc = "{:.2f}".format(nodeV[3])
                y_loc = "{:.2f}".format(nodeV[4])
                location_surface = node_loc_font.render(f"({x_loc}, {y_loc})", True, black)
                window.blit(location_surface, (nodeV[0] - 25, nodeV[1] - 25))

        if active_tsp:
            color_tsp = color_active_tsp
        else:
            color_tsp = color_passive_tsp
        pygame.draw.rect(window, color_tsp, input_rect_tsp, 2)
        text_surface = base_font_tsp.render(src.gui.constants.user_text_tsp, True, (0, 0, 128))
        window.blit(text_surface, (input_rect_tsp.x + 5, input_rect_tsp.y + 5))
        input_rect_tsp.w = max(text_surface.get_width() + 10, 73)

        if active_shortest:
            color_shortest = color_active_shortest
        else:
            color_shortest = color_passive_shortest
        pygame.draw.rect(window, color_shortest, input_rect_shortest, 2)
        text_surface = base_font_shortest.render(src.gui.constants.user_text_shortest, True, (0, 0, 128))
        window.blit(text_surface, (input_rect_shortest.x + 5, input_rect_shortest.y + 5))
        input_rect_shortest.w = max(text_surface.get_width() + 10, 73)

        if active_add_node:
            color_add_node = color_active_add_node
        else:
            color_add_node = color_passive_add_node
        pygame.draw.rect(window, color_add_node, input_rect_add_node, 2)
        text_surface = base_font_add_node.render(src.gui.constants.user_text_add_node, True, (0, 0, 128))
        window.blit(text_surface, (input_rect_add_node.x + 5, input_rect_add_node.y + 5))
        input_rect_add_node.w = max(text_surface.get_width() + 10, 73)

        if active_remove_node:
            color_remove_node = color_active_remove_node
        else:
            color_remove_node = color_passive_remove_node
        pygame.draw.rect(window, color_remove_node, input_rect_remove_node, 2)
        text_surface = base_font_remove_node.render(src.gui.constants.user_text_remove_node, True, (0, 0, 128))
        window.blit(text_surface, (input_rect_remove_node.x + 5, input_rect_remove_node.y + 5))
        input_rect_remove_node.w = max(text_surface.get_width() + 10, 73)

        if active_remove_edge:
            color_remove_edge = color_active_remove_edge
        else:
            color_remove_edge = color_passive_remove_edge
        pygame.draw.rect(window, color_remove_edge, input_rect_remove_edge, 2)
        text_surface = base_font_remove_edge.render(src.gui.constants.user_text_remove_edge, True, (0, 0, 128))
        window.blit(text_surface, (input_rect_remove_edge.x + 5, input_rect_remove_edge.y + 5))
        input_rect_remove_edge.w = max(text_surface.get_width() + 10, 73)

        if active_add_edge:
            color_add_edge = color_active_add_edge
        else:
            color_add_edge = color_passive_add_edge
        pygame.draw.rect(window, color_add_edge, input_rect_add_edge, 2)
        text_surface = base_font_add_edge.render(src.gui.constants.user_text_add_edge, True, (0, 0, 128))
        window.blit(text_surface, (input_rect_add_edge.x + 5, input_rect_add_edge.y + 5))
        input_rect_add_edge.w = max(text_surface.get_width() + 10, 73)

        if active_node_loc:
            color_node_loc = color_passive_node_loc
        else:
            color_node_loc = color_active_node_loc
        pygame.draw.rect(window, color_node_loc, input_rect_node_loc, 2)
        text_surface = base_font_node_loc.render(src.gui.constants.user_text_node_loc, True, (0, 0, 128))
        window.blit(text_surface, (input_rect_node_loc.x + 5, input_rect_node_loc.y + 5))
        input_rect_node_loc.w = max(text_surface.get_width() + 10, 73)

        if active_edge_weight:
            color_edge_weight = color_passive_edge_weight
        else:
            color_edge_weight = color_active_edge_weight
        pygame.draw.rect(window, color_edge_weight, input_rect_edge_weight, 2)
        text_surface = base_font_edge_weight.render(src.gui.constants.user_text_edge_weight, True, (0, 0, 128))
        window.blit(text_surface, (input_rect_edge_weight.x + 5, input_rect_edge_weight.y + 5))
        input_rect_edge_weight.w = max(text_surface.get_width() + 10, 73)

        center_button.draw(window)
        load_button.draw(window)
        pygame.display.flip()
        clock.tick(20)
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    GUI("./data/A2.json")
