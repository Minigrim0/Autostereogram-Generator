import numpy as np
import math
import cv2


def autostereogram(depth_map, pattern, grayscale):
    """This function implements the autostereogram algorithm"""
    E = 0.1
    b = 1.0  # Distance between the near and far plane
    a = 2  # Distance between the autostereogram plane and the near plane
    if grayscale:
        autostereogram = np.zeros(
            shape=[depth_map.shape[0], depth_map.shape[1], 1],
            dtype=pattern.dtype)
    else:
        autostereogram = np.zeros(
            shape=[depth_map.shape[0], depth_map.shape[1], 3],
            dtype=pattern.dtype)

    for row in range(depth_map.shape[0]):
        for column in range(depth_map.shape[1]):
            # If the current column is smaller than the amount of columns
            # in the pattern
            if column < pattern.shape[1]:
                # Copy in the current row/col the pattern
                autostereogram[row][column] = pattern[
                    row % pattern.shape[0]][column]
                continue

            # otherwise, apply the autostereogram algorithm
            grey_value = depth_map[row, column]
            s_on_two = math.floor(
                (
                    ((a - (b * grey_value / 255)) * E) / 2 *
                    (1 + a - (b * grey_value))
                ) + 0.5
            )
            autostereogram[row][column] = autostereogram[
                row][column - pattern.shape[1] + s_on_two]
            if column - pattern.shape[1] - s_on_two > 0:
                autostereogram[row][column] = autostereogram[
                    row][column - pattern.shape[1] - s_on_two]
    return autostereogram


def create_autoStereogram(filename, grayscale=False):
    """
    This function preprocesses the initial image and creates the autostereogram
    """
    # Load the image
    depth_map = cv2.imread(filename)
    # Convert to grayscale
    depth_map = cv2.cvtColor(depth_map, cv2.COLOR_BGR2GRAY)

    # Create the random pattern
    size_x, size_y = depth_map.shape
    if grayscale:
        pattern = np.random.uniform(0, 1, (size_y, 64, 1))
    else:
        pattern = np.random.uniform(0, 1, (size_y, 64, 3))

    final_image = autostereogram(depth_map, pattern, grayscale)
    cv2.imwrite('autostereogram.png', 255 * final_image)
    return final_image


if __name__ == "__main__":
    import sys

    # Example run of the algorithm
    if len(sys.argv) < 2:
        print("Please provide a filename")
        sys.exit(1)

    final_image = create_autoStereogram(sys.argv[1])
    cv2.imshow('Autostereogram', final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
