# Reinforcement Learning file
POLICY = dict()
FPS = 60
TIME_PASSED = 1 / FPS
BIRD_WIDTH = 34
BIRD_HEIGHT = 24
PIPE_WIDTH = 52
PIPE_GAP = 100
PIPE_GAP_HARD = 40


# check if bird and pipes will collide
def will_collide(distance, height, speed):
    available_gap = (PIPE_GAP_HARD - BIRD_HEIGHT) // 2
    if distance <= BIRD_WIDTH + PIPE_WIDTH and (height <= -available_gap or available_gap <= height):
        return True
    else:
        # if flap will lead to collision
        while speed > 0:
            if distance <= 86 and (height <= -38 or 38 <= height):
                return True
            height += speed
            distance -= 4
            speed -= 77 * TIME_PASSED

        # if still too high and may lead to collision
        while height > 0:
            if distance <= 86 and (height <= -38 or 38 <= height):
                return True
            height += speed
            distance -= 4
            speed -= 77 * TIME_PASSED

        return False


# given current status (distance, height, speed), then decide next best action (flap or idle)
def next_best_action(distance, height, speed):
    flap_speed = max(9, speed + 2)
    # update
    flap_speed -= 77 * TIME_PASSED
    flap_height = height + flap_speed

    idle_speed = speed - 77 * TIME_PASSED
    idle_height = height + idle_speed

    distance -= 4
    # decide best action
    is_flap_collide = will_collide(distance, flap_height, flap_speed)
    is_idle_collide = will_collide(distance, idle_height, idle_speed)
    flap_value = -1000 * is_flap_collide - abs(flap_height)
    idle_value = -1000 * is_idle_collide - abs(idle_height)
    if flap_value > idle_value:
        # in case of distance is too close (between pipes) and still flap to collide
        if distance <= 52 and not is_idle_collide:
            return False
        return True
    else:
        return False


# given current status (bird, pipes), and turn it into (distance, height, speed), check POLICY if flap or idle
def if_flap(bird, pipe_sprites):
    # distance
    pipe_top = pipe_sprites.sprites()[0]

    distance = pipe_top.rect.right - bird.rect.left
    if distance < 0:
        pipe_top = pipe_sprites.sprites()[2]
        distance = pipe_top.rect.right - bird.rect.left
    if distance > 179:
        distance = 179

    # height
    if distance >= 179:
        height = 256 - bird.rect.centery
    else:
        height = pipe_top.rect.bottom + 75 - bird.rect.centery
    if height < -100:
        height = -100
    elif height > 100:
        height = 100

    # speed
    speed = round(bird.speed, 1)
    if speed > 15:
        speed = 15.0
    elif speed < -15:
        speed = -15.0

    # get action
    action = POLICY[(distance, height, speed)]
    if action:
        print(str((distance, height, speed)) + " true")
    return action


# generate the policy (could use Neural Networks instead)
for x in range(0, 180):
    for y in range(-100, 101):
        for z in range(-150, 151):
            POLICY[(x, y, z / 10)] = next_best_action(x, y, z / 10)
