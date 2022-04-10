import numpy as np
import math
import cv2
import sys
import copy


def make_pattern(shape):
    return np.random.uniform(0, 1, shape)


depth_map = cv2.imread(sys.argv[1])
depth_map = cv2.cvtColor(depth_map, cv2.COLOR_BGR2GRAY)

size_x, size_y = depth_map.shape
pattern = make_pattern((size_y, size_x // 6, 1))
# Make a copy of the initial pattern to avoid moving pixels mulitple times

cv2.imshow("pattern", pattern)

def normalize(depthmap):
    "Normalizes values of depthmap to [0, 1] range."
    if depthmap.max() > depthmap.min():
        return (depthmap - depthmap.min()) / (depthmap.max() - depthmap.min())
    else:
        return depthmap

def make_autostereogram(depthmap, pattern, shift_amplitude=0.1, invert=False):
    "Creates an autostereogram from depthmap and pattern."
    depthmap = normalize(depthmap)
    if invert:
        depthmap = 1 - depthmap
    autostereogram = np.zeros_like(depthmap, dtype=pattern.dtype)
    for r in np.arange(autostereogram.shape[0]):
        for c in np.arange(autostereogram.shape[1]):
            if c < pattern.shape[1]:
                autostereogram[r, c] = pattern[r % pattern.shape[0], c]
            else:
                shift = int(depthmap[r, c] * shift_amplitude * pattern.shape[1])
                autostereogram[r, c] = autostereogram[r, c - pattern.shape[1] + shift]
    return autostereogram

def autostereogram(depth_map, pattern):
    E = 0.06
    b = 1  # Distance between the near and far plane
    a = 0.5 # Distance between the autostereogram plane and the near plane
    final_image = np.zeros_like(depth_map, dtype=pattern.dtype)

    for y in range(depth_map.shape[0]):
        for x in range(depth_map.shape[1]):
            grey_value = depth_map[y, x]
            s_on_two = math.floor((((a - (b * grey_value / 255)) * E) / 2 * (1 + a - (b * grey_value))) + 0.5)
            if x + s_on_two < size_x:
                final_image[y, x + s_on_two] = pattern[y, x % pattern.shape[1]]
            if x - s_on_two > 0:
                final_image[y, x - s_on_two] = pattern[y, x % pattern.shape[1]]
    return final_image

# final_image = make_autostereogram(depth_map, pattern, shift_amplitude=0.1, invert=False)
final_image = autostereogram(depth_map, pattern)
cv2.imshow("final", final_image)

# cv2.imshow("final", final_image)

cv2.imwrite("result.jpg", 255 * final_image)

cv2.waitKey(0)

cv2.destroyAllWindows()
