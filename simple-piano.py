import pygame
from pygame.locals import *
from mingus.containers import *
from mingus.midi import fluidsynth
from os import sys

SF2 = "Sonatina_Symphonic_Orchestra.sf2"
FADEOUT = 25  # coloration fadeout time (1 tick = 0.001)
WHITE_KEYS = ["C", "D", "E", "F", "G", "A", "B"]
BLACK_KEYS = ["C#", "D#", "F#", "G#", "A#"]

if not fluidsynth.init(SF2):
    print("Couldn't load soundfont", SF2)
    sys.exit(1)

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

octave = 4
channel = 8

playing_w = []  # white keys being played right now
playing_b = []  # black keys being played right now
quit = False
tick = 0.0


def handle_events():
    global quit
    global channel
    octave = 4
    for event in pygame.event.get():
        if event.type == QUIT:
            quit = True
        if event.type == KEYDOWN:
            if event.key == K_z:
                play_note(Note("C", octave))
            elif event.key == K_s:
                play_note(Note("C#", octave))
            elif event.key == K_x:
                play_note(Note("D", octave))
            elif event.key == K_d:
                play_note(Note("D#", octave))
            elif event.key == K_c:
                play_note(Note("E", octave))
            elif event.key == K_v:
                play_note(Note("F", octave))
            elif event.key == K_g:
                play_note(Note("F#", octave))
            elif event.key == K_b:
                play_note(Note("G", octave))
            elif event.key == K_h:
                play_note(Note("G#", octave))
            elif event.key == K_n:
                play_note(Note("A", octave))
            elif event.key == K_j:
                play_note(Note("A#", octave))
            elif event.key == K_m:
                play_note(Note("B", octave))
            elif event.key == K_COMMA:
                play_note(Note("C", octave + 1))
            elif event.key == K_l:
                play_note(Note("C#", octave + 1))
            elif event.key == K_PERIOD:
                play_note(Note("D", octave + 1))
            elif event.key == K_SEMICOLON:
                play_note(Note("D#", octave + 1))
            elif event.key == K_SLASH:
                play_note(Note("E", octave + 1))
            elif event.key == K_q:
                play_note(Note("B", octave))
            elif event.key == K_w:
                play_note(Note("C", octave + 1))
            elif event.key == K_3:
                play_note(Note("C#", octave + 1))
            elif event.key == K_e:
                play_note(Note("D", octave + 1))
            elif event.key == K_4:
                play_note(Note("D#", octave + 1))
            elif event.key == K_r:
                play_note(Note("E", octave + 1))
            elif event.key == K_t:
                play_note(Note("F", octave + 1))
            elif event.key == K_6:
                play_note(Note("F#", octave + 1))
            elif event.key == K_y:
                play_note(Note("G", octave + 1))
            elif event.key == K_7:
                play_note(Note("G#", octave + 1))
            elif event.key == K_u:
                play_note(Note("A", octave + 1))
            elif event.key == K_8:
                play_note(Note("A#", octave + 1))
            elif event.key == K_i:
                play_note(Note("B", octave + 1))
            elif event.key == K_o:
                play_note(Note("C", octave + 2))
            elif event.key == K_0:
                play_note(Note("C#", octave + 2))
            elif event.key == K_p:
                play_note(Note("D", octave + 2))
            elif event.key == K_MINUS:
                octave -= 1
            elif event.key == K_EQUALS:
                octave += 1
            elif event.key == K_BACKSPACE:
                channel -= 1
            elif event.key == K_BACKSLASH:
                channel += 1
            elif event.key == K_ESCAPE:
                quit = True


def play_note(note):
    playing_w.append([tick, note])
    playing_b.append([tick, note])
    print(f"play note: {note=}, {channel=}, {octave=}")
    fluidsynth.play_Note(note, channel, 100)

while not quit:
    clock.tick(25)
    for note in playing_w:
        diff = tick - note[0]

        if diff > FADEOUT:
            fluidsynth.stop_Note(note[1], channel)
            playing_w.remove(note)

    for note in playing_b:
        diff = tick - note[0]

        if diff > FADEOUT:
            fluidsynth.stop_Note(note[1], channel)
            playing_b.remove(note)

    handle_events()


    pygame.display.update()
    tick += 0.5
pygame.quit()
