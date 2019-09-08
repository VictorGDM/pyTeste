import sysconfig, pygame
import crgImg, idtBto, tcrTela, crgSons

###-----------------------------------------------------------###
"""
crgImg  ===== Carrega as imagens do jogo
idtBto  ===== Identifica as posições dos botões
tcrTela ===== Troca as imagens da tela
"""
###-----------------------------------------------------------###
def updateScreen(tela):
    screen.blit(tela, (0, 0))
    pygame.display.update()

#--Variaveis de alteração--#
pygame.init()
size = width, height = 1000, 650
screen = pygame.display.set_mode(size)
executando = True
tSom = 0
som = crgSons.mdrSom(tSom)
botao = 0
tema = 0

#--Telas do jogo--#
pygame.display.set_caption('Xadrez')
camada = 0
crgImg.mdrTema(tema)
tela = crgImg.menu
updateScreen(tela)

#--Jogo em execução--#
while executando == True:
    x, y = pygame.mouse.get_pos()

    #--Controlar os eventos--#
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            executando = False

        if event.type == pygame.MOUSEBUTTONUP:
            if camada == 4:
                mudou, tela, camada, tema = tcrTela.prxTela(camada, botao, tema, tSom)
                crgImg.mdrTema(tema)
                updateScreen(tela)

            elif camada == 0 and botao == 5:
                executando = tcrTela.prxTela(camada, botao, tema, tSom)

            else:
                mudou, tela_r, camada_r = tcrTela.prxTela(camada, botao, tema, tSom)    
                if(mudou):
                    tela = tela_r
                    camada = camada_r
                    updateScreen(tela)

    print(f'x:{x} y:{y} b:{botao} t:{tema} c:{camada} tS:{tSom}')

    mudou, tela_r, botao_r, tSom_r = idtBto.btMouse(x, y, camada, tela)
    
    if(mudou):
        tela = tela_r
        botao = botao_r
        tSom = tSom_r
        updateScreen(tela)

pygame.quit()
sysconfig.exit()
