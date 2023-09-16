__copyright__ = """

    Copyright 2023 John Pratt

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

"""
__license__ = "Apache 2.0"

import cv2

class Tracker:
    IMAGE_THRESHOLD = 225
    HISTORY_DEPTH = 10

    def __init__(self) -> None:
        self._center_list = [0 for i in range(self.HISTORY_DEPTH)]
        self._center_idx = 0

    def add_frame(self, frame):
        single = frame[:,:,1]
        # convert the grayscale image to binary image
        _,thresh = cv2.threshold(single,self.IMAGE_THRESHOLD,255,0)

        # calculate moments of binary image
        M = cv2.moments(thresh)
        
        # calculate x,y coordinate of center
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        self._center_list[self._center_idx] = (cX, cY)
        self._center_idx = (self._center_idx + 1) % self.HISTORY_DEPTH
        return (cX, cY)
