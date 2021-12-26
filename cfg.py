# configure file
import os

FPS = 60

SCREENWIDTH = 289
SCREENHEIGHT = 512

PIPE_GAP_SIZE = 100

# images
NUMBER_IMAGE_PATHS = {
    '0': os.path.join(os.getcwd(), 'resources/images/0.png'),
    '1': os.path.join(os.getcwd(), 'resources/images/1.png'),
    '2': os.path.join(os.getcwd(), 'resources/images/2.png'),
    '3': os.path.join(os.getcwd(), 'resources/images/3.png'),
    '4': os.path.join(os.getcwd(), 'resources/images/4.png'),
    '5': os.path.join(os.getcwd(), 'resources/images/5.png'),
    '6': os.path.join(os.getcwd(), 'resources/images/6.png'),
    '7': os.path.join(os.getcwd(), 'resources/images/7.png'),
    '8': os.path.join(os.getcwd(), 'resources/images/8.png'),
    '9': os.path.join(os.getcwd(), 'resources/images/9.png')
}

BIRD_IMAGE_PATHS = {
    'red': {
        'up': os.path.join(os.getcwd(), 'resources/images/red-bird-up-flap.png'),
        'mid': os.path.join(os.getcwd(), 'resources/images/red-bird-mid-flap.png'),
        'down': os.path.join(os.getcwd(), 'resources/images/red-bird-down-flap.png')
    },
    'blue': {
        'up': os.path.join(os.getcwd(), 'resources/images/blue-bird-up-flap.png'),
        'mid': os.path.join(os.getcwd(), 'resources/images/blue-bird-mid-flap.png'),
        'down': os.path.join(os.getcwd(), 'resources/images/blue-bird-down-flap.png')
    },
    'yellow': {
        'up': os.path.join(os.getcwd(), 'resources/images/yellow-bird-up-flap.png'),
        'mid': os.path.join(os.getcwd(), 'resources/images/yellow-bird-mid-flap.png'),
        'down': os.path.join(os.getcwd(), 'resources/images/yellow-bird-down-flap.png')
    }
}

BACKGROUND_IMAGE_PATHS = {
    'day': os.path.join(os.getcwd(), 'resources/images/background-day.png'),
    'night': os.path.join(os.getcwd(), 'resources/images/background-night.png')
}

PIPE_IMAGE_PATHS = {
    'green': os.path.join(os.getcwd(), 'resources/images/pipe-green.png'),
    'red': os.path.join(os.getcwd(), 'resources/images/pipe-red.png')
}

OTHER_IMAGE_PATHS = {
    'game-over': os.path.join(os.getcwd(), 'resources/images/game-over.png'),
    'message': os.path.join(os.getcwd(), 'resources/images/message.png'),
    'base': os.path.join(os.getcwd(), 'resources/images/base.png')
}

# audio
AUDIO_PATHS = {
    'die': os.path.join(os.getcwd(), 'resources/audios/die.wav'),
    'hit': os.path.join(os.getcwd(), 'resources/audios/hit.wav'),
    'point': os.path.join(os.getcwd(), 'resources/audios/point.wav'),
    'swoosh': os.path.join(os.getcwd(), 'resources/audios/swoosh.wav'),
    'wing': os.path.join(os.getcwd(), 'resources/audios/wing.wav')
}
