import os
import cv2
import numpy as np
from matplotlib import pyplot
from channel import Channel

# Colors (B, G, R)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def create_blank(width, height, color=(0, 0, 0)):
    """Create new image(numpy array) filled with certain color in BGR"""
    image = np.zeros((height, width, 3), np.uint8)
    # Fill image with color
    image[:] = color
    return image

def key(params):
    pairs = sorted(params.items())
    plist = []
    for param, val in pairs:
        plist.append(f"{param}{str(val)}")
    return "_".join(plist)

# Create new blank 300x150 white image
width, height = 300, 300
image = create_blank(width, height, color=BLACK)

params1 = {
    "angdev": 15,
    "seg_hi": 30,
    "seg_lo": 25,
    "amp_hi": 10,
    "amp_lo": 2,
    "num_channels": 3,
}

params2 = {
    "angdev": 30,
    "seg_hi": 10,
    "seg_lo": 5,
    "amp_hi": 2.5,
    "amp_lo": 1,
    "num_channels": 4,
}

params3 = {
    "angdev": 15,
    "seg_hi": 30,
    "seg_lo": 10,
    "amp_hi": 40,
    "amp_lo": 3,
    "num_channels": 2,
}

params4 = {
    "angdev": 15,
    "seg_hi": 30,
    "seg_lo": 25,
    "amp_hi": 10,
    "amp_lo": 2,
    "num_channels": 2,
}

params5 = {
    "angdev": 15,
    "seg_hi": 30,
    "seg_lo": 25,
    "amp_hi": 10,
    "amp_lo": 2,
    "num_channels": 1,
}

params6 = {
    "angdev": 30,
    "seg_hi": 10,
    "seg_lo": 5,
    "amp_hi": 2.5,
    "amp_lo": 1,
    "num_channels": 3,
}

params7 = {
    "angdev": 30,
    "seg_hi": 10,
    "seg_lo": 5,
    "amp_hi": 2.5,
    "amp_lo": 1,
    "num_channels": 2,
}

params8 = {
    "angdev": 30,
    "seg_hi": 10,
    "seg_lo": 5,
    "amp_hi": 2.5,
    "amp_lo": 1,
    "num_channels": 1,
}

params9 = {
    "angdev": 15,
    "seg_hi": 30,
    "seg_lo": 10,
    "amp_hi": 40,
    "amp_lo": 3,
    "num_channels": 1,
}

params10 = {
    "angdev": 15,
    "seg_hi": 8,
    "seg_lo": 2,
    "amp_hi": 0.1,
    "amp_lo": 0.05,
    "num_channels": 5,
}

params11 = {
    "angdev": 20,
    "seg_hi": 8,
    "seg_lo": 2,
    "amp_hi": 0.1,
    "amp_lo": 0.05,
    "num_channels": 4,
}

params12 = {
    "angdev": 22,
    "seg_hi": 8,
    "seg_lo": 2,
    "amp_hi": 0.1,
    "amp_lo": 0.05,
    "num_channels": 3,
}

params13 = {
    "angdev": 30,
    "seg_hi": 8,
    "seg_lo": 2,
    "amp_hi": 0.1,
    "amp_lo": 0.05,
    "num_channels": 2,
}

params14 = {
    "angdev": 30,
    "seg_hi": 10,
    "seg_lo": 6,
    "amp_hi": 0.1,
    "amp_lo": 0.05,
    "num_channels": 2,
}

params15 = {
    "angdev": 15,
    "seg_hi": 20,
    "seg_lo": 10,
    "amp_hi": 0.1,
    "amp_lo": 0.05,
    "num_channels": 1,
}


param_opts = [params1, params2, params3, params4, params5, params6, params7, params8, params9, params10, params11, params12, params13, params14, params15]
params = params15
num_channels = params["num_channels"]
padding = width // (num_channels + 1)

# for i in range(padding, width, padding):
#     chObj = Channel(image, (i, 0), 0, angle_dev=params["angdev"], segment_hi=params["seg_hi"], segment_lo=params["seg_lo"], amp_hi=params["amp_hi"], amp_lo=params["amp_lo"], thickness=2)
#     for i in range(height // (params["seg_lo"] // 2)):
#         chObj.add_segment()
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# pyplot.figure(figsize=image.shape)
# im = pyplot.imshow(image)
# pyplot.gca().invert_yaxis()
# pyplot.colorbar(im)
# pyplot.show()
# cv2.imwrite('half_circle_rounded.jpg', image)

for params in param_opts:
    num_channels = params["num_channels"]
    padding = width // (num_channels + 1)
    niterations = 300
    pack_name = key(params)
    dirname = os.path.join(os.getcwd(), "obm_channels_ds", pack_name)
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    for it in range(niterations):
        image = create_blank(width, height, color=BLACK)
        for i in range(padding, width, padding):
            chObj = Channel(image, (i, 0), 0, angle_dev=params["angdev"], segment_hi=params["seg_hi"], segment_lo=params["seg_lo"], amp_hi=params["amp_hi"], amp_lo=params["amp_lo"], thickness=2)
            for l in range(height // (params["seg_lo"] // 2)):
                chObj.add_segment()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fname = f"{pack_name}_{str(it)}.jpg"
        fullname = os.path.join(dirname, fname)
        cv2.imwrite(fullname, image)




