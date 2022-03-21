import math
import numpy as np
from cv2 import cv2
import random
'''
Channel class represents channel object
'''
class Channel(object):

    def __init__(self, image, origin = (0,0), central_line_angle = 0, angle_dev = 30, segment_lo = 5, segment_hi = 10, amp_lo = 1, amp_hi = 2, thickness = 1):
        '''
        Create channel object
        :param image: Canvas for drawing channels
        :param origin: Source of channel body
        :param central_line_angle: Angle [0, 360] that defines direction of facies properties proliferation
        :param angle_dev: Standard angle deviation specifies in which extent channel body is prone to change original direction
        :param segment_lo: The lowest length of channel segment
        :param segment_hi: The highest length of channel segment
        :param amp_lo: The lowest amlpitude of meanders
        :param amp_hi: The highest amplitude of meanders
        :param thickness: Thickness of channel
        '''
        # random x,y shift of phase for sin function
        shift0 = random.randint(0, (segment_hi + segment_lo) // 4)
        shift1 = random.randint(0, (segment_hi + segment_lo) // 4)
        self.points = [(origin[0] - shift0 if origin[0] == 0 else origin[0], origin[1] - shift1 if origin[1] == 0 else origin[1])]
        # init params
        self.image = image
        self.central_line_angle = central_line_angle
        self.angle_dev = angle_dev
        self.segment_lo = segment_lo
        self.segment_hi = segment_hi
        self.amp_lo = amp_lo
        self.amp_hi = amp_hi
        self.thickness = thickness
        self.step = random.choice([0, 180])

    def add_segment(self):
        '''
        Add segment to channel
        Each segment of channel goes through full period of sine function: 180 degrees or pi radians
        '''

        # use Gaussian normal distribution set delta in channel direction (deltas fluctuate around zero)
        angle_dev = np.random.normal(0, self.angle_dev)
        # randomly choose segment lenths based on parameters
        segment_len = max(int(np.random.randint(self.segment_lo, self.segment_hi)), 1)
        rate = 180 // segment_len
        segment_len = 180 // rate
        # randomly choose sin function amplitude multiplier
        segment_amp = max(int(np.random.uniform(self.amp_lo, self.amp_hi)), 0.1)
        # use last point of channel as segment start point
        segment_start = self.points[-1]
        lps = [segment_start]
        # construct curve
        for i in range(segment_len+1):
            # adjust change angle rate in accordance to segment length for sine full period
            step = (self.step + i * rate) % 360
            # segment goes along y axis
            y = i
            # x component computed as sine function with custom amplitude and arg speed
            x = segment_amp * math.sin(math.radians(step))
            # perform rotation and translation of local segment coordinate system to coordinate system of an image
            xn = int(math.cos(math.radians(self.central_line_angle + angle_dev)) * x + math.sin(math.radians(self.central_line_angle + angle_dev)) * y + segment_start[0])
            yn = int(-math.sin(math.radians(self.central_line_angle + angle_dev)) * x + math.cos(math.radians(self.central_line_angle + angle_dev)) * y + segment_start[1])
            # add point to curve
            lps.append((xn, yn))
        # ensure that after building a curve current step goes through full function period
        self.step = (self.step + 180) % 360
        # draw line
        cv2.polylines(self.image, [np.array(lps)], False, (255, 255, 255), thickness=self.thickness)
        # adjust center line angle delta
        self.central_line_angle =+ angle_dev
        # add frame point to channel
        segment_end = (lps[-1][0], lps[-1][1])
        self.points.append(segment_end)






