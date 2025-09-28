import numpy as np
from PIL import Image
# Converting Image to NumPy Array
image = Image.open("25.jpg")
array: np.ndarray = np.array(image)

array_with_transparent_channel: np.ndarray = np.zeros((array.shape[0], array.shape[1], 4), dtype=np.uint8)

array_with_transparent_channel[:, :, :3] = array
array_with_transparent_channel[:, :, 3] = 255  # Set alpha channel to fully opaque

red, green, blue = array_with_transparent_channel[:,:,0], array_with_transparent_channel[:,:,1], array_with_transparent_channel[:,:,2]
mask_1 = (red > 42) & (red < 82) & (green > 34) & (green < 74) & (blue > 71) & (blue < 111)
array_with_transparent_channel[mask_1] = [0, 0, 0, 0]

mask_3 = (red > 200) & (red < 256) & (green > 200) & (green < 256) & (blue > 200) & (blue < 256)
array_with_transparent_channel[mask_3] = [0, 0, 0, 0]

mask_2 = (red > 0) & (red < 257) & (green > 0) & (green < 240) & (blue > 0) & (blue < 240)
# array_with_transparent_channel[mask_2] = [136, 136, 204, 195]
array_with_transparent_channel[mask_2] = [0, 0, 0, 60]

# mask = np.all(array_with_transparent_channel == [62, 54, 91, 255], axis=-1)

# array_with_transparent_channel[mask] = [0, 0, 0, 0]

# mask = np.all(array_with_transparent_channel == [191, 101, 136, 255], axis=-1)

# array_with_transparent_channel[mask] = [0, 0, 0, 195]

print(array_with_transparent_channel)

# Converting NumPy Array back to Image
new_image = Image.fromarray(array_with_transparent_channel, 'RGBA')
new_image.save("output_image.png")