from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

poly_line = [(33.8938, 35.50148), (33.89321, 35.50144), (33.89286, 35.50134), (33.89218, 35.50107), (33.89192, 35.50098), (33.89124, 35.50068), (33.8904, 35.5003), (33.89015, 35.50017), (33.89, 35.50011), (33.88942, 35.49982), (33.88921, 35.49971), (33.88879, 35.49954), (33.88839, 35.49933), (33.88784, 35.49907), (33.88793, 35.49858), (33.88802, 35.49812), (33.88842, 35.4984), (33.88853, 35.49844), (33.8886, 35.49887), (33.88862, 35.49895), (33.88865, 35.49908), (33.88874, 35.4995), (33.88886, 35.50018), (33.88887, 35.50032), (33.8888, 35.50097), (33.88871, 35.50181), (33.88865, 35.50206), (33.88841, 35.50305), (33.88832, 35.50347), (33.88827, 35.50371), (33.88814, 35.50412), (33.88807, 35.50433), (33.8878, 35.50496), (33.88755, 35.50549), (33.88717, 35.50627), (33.88706, 35.50644), (33.88694, 35.50678), (33.88676, 35.50758), (33.88668, 35.50819), (33.88668, 35.50832), (33.88651, 35.50845), (33.88636, 35.50856), (33.88605, 35.50879), (33.88514, 35.50953), (33.8843, 35.5102), (33.88417, 35.51031), (33.88404, 35.51043), (33.88397, 35.5106), (33.88385, 35.51086), (33.88361, 35.51134), (33.88338, 35.51181), (33.88302, 35.51232), (33.88259, 35.51292), (33.88223, 35.51348), (33.88207, 35.51376), (33.88203, 35.51386), (33.88196, 35.51396), (33.88188, 35.5141), (33.88174, 35.5144), (33.88124, 35.51563), (33.88105, 35.51623), (33.88067, 35.5175), (33.8804, 35.51852), (33.88023, 35.51913), (33.88016, 35.51932), (33.88002, 35.51949), (33.87978, 35.51981), (33.87975, 35.51988), (33.87975, 35.51993), (33.87965, 35.52003), (33.87911, 35.52056), (33.87847, 35.52118), (33.87665, 35.52281), (33.87614, 35.52324), (33.87582, 35.52347), (33.87549, 35.52367), (33.87514, 35.52385), (33.87479, 35.52399), (33.87425, 35.52423), (33.87238, 35.52498), (33.87134, 35.5254), (33.86989, 35.526), (33.86929, 35.52629), (33.8688, 35.52657), (33.86854, 35.52677), (33.86792, 35.52728), (33.86698, 35.5282), (33.86618, 35.52898), (33.86566, 35.52944), (33.86524, 35.5298), (33.86508, 35.52982), (33.86472, 35.52995), (33.86434, 35.52997), (33.86413, 35.52995), (33.86403, 35.52995), (33.86395, 35.5299), (33.86387, 35.52977), (33.86367, 35.52996), (33.86338, 35.53022), (33.86313, 35.53043), (33.86289, 35.53061), (33.86202, 35.5314), (33.86143, 35.53192), (33.86138, 35.532), (33.8611, 35.53225), (33.86077, 35.53255), (33.85969, 35.53346), (33.85889, 35.53413), (33.85827, 35.53454), (33.85783, 35.5348), (33.857, 35.53518), (33.8567, 35.53526), (33.85589, 35.53541), (33.85571, 35.53547), (33.85557, 35.53555), (33.85544, 35.53566), (33.85537, 35.53576), (33.8553, 35.53586)]
lon = 33.893913
lat = 35.501458
p = Point(lon,lat)
polygon = Polygon( poly_line )

print(polygon.contains(p))

import matplotlib.pyplot as plt

xs, ys = zip(*poly_line)

plt.figure()
plt.axes().set_facecolor( '#d9d9d9' )
#ax.set_facecolor('black')
plt.plot(xs,ys)
plt.plot(lon,lat,'o',)
plt.show()