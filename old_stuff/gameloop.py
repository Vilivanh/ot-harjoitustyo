import pygame


class GameLoop:
    def __init__(self, level, cell_size, display):
        self._level = level
        self._clock = pygame.time.Clock()
        self._cell_size = cell_size
        self._display = display

    def start(self):
        while True:
            if self._handle_events() == False:
                break

            self._render()

            # jokaista sekunttia kohden piirretään maksimissaan 60 näkymää
            self._clock.tick(60)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #x,y = event.pos
                
            elif event.type == pygame.QUIT:
                return False

    