from pilmoji.core import Pilmoji
from PIL import Image, ImageFont
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

my_string = '''
Hello, world! 👋 Here are some emojis: 🎨 🌊 😎
I also support Discord emoji: <:rooThink:596576798351949847>
'''

# with Image.new('RGB', (550, 80), (255, 255, 255)) as image:
#     font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 24)

#     with Pilmoji(image) as pilmoji:
#         pilmoji.text((10, 10), my_string.strip(), (0, 0, 0), font)

#     image.show()

# generate emoji as image
size = 500
font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', size)
image = Image.new('RGBA', (size, size), (255, 255, 255, 0))

# get image from Pilmoji
pilmoji = Pilmoji(image)
pilmoji.text((0, 0), "🎨", None, font)
im = np.array(image)

def get_emoji(emoji, font_path, font_size=500):
    font = ImageFont.truetype(font_path, font_size)
    image = Image.new('RGBA', (font_size, font_size), (255, 255, 255, 0))

    pilmoji = Pilmoji(image)
    pilmoji.text((0, 0), emoji, None, font)
    emoji_im = np.array(image)

    return emoji_im

def plot_emoji(x, y, emoji_im, axs, marker_size = 1, label=""):

    for i in range(len(x)):
        im_range = marker_size/2
        extent = (x[i]-im_range, x[i]+im_range, y[i]-im_range, y[i]+im_range)
        axs.imshow(emoji_im[::-1,:,:], origin="lower", extent = extent)
    
    line = axs.plot(x, y, markersize=0, linestyle="", label=label)
    return line

def plot_legend(emoji_im, ax, legend, loc, zoom=0.05):
    legend_marker = AnnotationBbox(OffsetImage(emoji_im, zoom=zoom), loc, frameon=False, xycoords="data")

    legend_marker.set_zorder(legend.get_zorder()+1)
    ax.add_artist(legend_marker)


x = np.linspace(0, 2*np.pi, 20)
y = np.sin(x)
emoji = "🎨"

font_path = '/System/Library/Fonts/Supplemental/Arial.ttf'
size= 0.25
emoji_im = get_emoji(emoji, font_path)
line = plot_emoji(x, y, emoji_im, plt.gca(), size, "palette")
legend = plt.legend()
plot_legend(emoji_im, plt.gca(), legend, (5.25, 0.87), 0.03)


# ax = plt.gca()

# bbox = legend.get_bbox_to_anchor()

# axis_to_data = ax.transData.inverted()
# data_to_axis = axis_to_data.inverted()
# x0, y0 = axis_to_data.transform((bbox.x0, bbox.y0))
# x1, y1 = axis_to_data.transform((bbox.x1, bbox.y1))


# plt.plot([0,1000], [0, 2000])
# plt.imshow(im[::-1,:,:], origin="lower")

# xs = np.linspace(0, 2*np.pi, 20)
# ys = np.sin(xs)
# emoji = "🎨"

# font_path = '/System/Library/Fonts/Supplemental/Arial.ttf'
# image = Image.new('RGBA', (font_size, font_size), (255, 255, 255, 0))

# pilmoji = Pilmoji(image)
# pilmoji.text((0, 0), emoji, None, font)
# im = np.array(image)

# size = 0.25
# for i in range(len(xs)):
#     x, y = xs[i], ys[i]
#     plt.imshow(im[::-1,:,:], origin="lower", extent = (x-size/2, x+size/2, y-size/2, y+size/2))
