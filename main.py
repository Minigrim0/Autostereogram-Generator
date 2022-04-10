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
pattern = make_pattern((size_y, 64, 1))
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
    for row in np.arange(autostereogram.shape[0]):
        for column in np.arange(autostereogram.shape[1]):
            if column < pattern.shape[1]:  # If the current column is smaller than the amount of columns in the pattern
                # Copy in the current row/col the pattern
                autostereogram[row, column] = pattern[row % pattern.shape[0], column]
            else:
                shift = int(depthmap[row, column] * shift_amplitude * pattern.shape[1])
                autostereogram[row, column] = autostereogram[row, column - pattern.shape[1] + shift]
    return autostereogram

def autostereogram(depth_map, pattern):
    E = 0.1
    b = 1.0  # Distance between the near and far plane
    a = 2  # Distance between the autostereogram plane and the near plane
    autostereogram = np.zeros_like(depth_map, dtype=pattern.dtype)

    for row in range(depth_map.shape[0]):
        for column in range(depth_map.shape[1]):
            if column < pattern.shape[1]:  # If the current column is smaller than the amount of columns in the pattern
                # Copy in the current row/col the pattern
                autostereogram[row, column] = pattern[row % pattern.shape[0], column]
            else:
                grey_value = depth_map[row, column]
                s_on_two = math.floor((((a - (b * grey_value / 255)) * E) / 2 * (1 + a - (b * grey_value))) + 0.5)
                autostereogram[row, column] = autostereogram[row, column - pattern.shape[1] + s_on_two]
                if column - pattern.shape[1] - s_on_two > 0:
                    autostereogram[row, column] = autostereogram[row, column - pattern.shape[1] - s_on_two]
    return autostereogram

# final_image = make_autostereogram(depth_map, pattern, shift_amplitude=0.1, invert=False)
final_image = autostereogram(depth_map, pattern)
cv2.imshow("final", final_image)

cv2.imwrite("result.jpg", 255 * final_image)

cv2.waitKey(0)

cv2.destroyAllWindows()
