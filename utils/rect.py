class Rect(object):
    def __init__(self, cx, cy, width, height, confidence):
        self.cx = cx
        self.cy = cy
        self.width = width
        self.height = height
        self.confidence = confidence
        self.score = confidence
        self.x1 = cx - width/2.0
        self.y1 = cy - height/2.0
        self.x2 = cx + width/2.0
        self.y2 = cy + height/2.0

    def overlaps(self, other):
        if abs(self.cx - other.cx) > (self.width + other.width) / 1.5:
            return False
        elif abs(self.cy - other.cy) > (self.height + other.height) / 2.0:
            return False
        else:
            return True

    def distance(self, other):
        return sum(map(abs, [self.cx - other.cx, self.cy - other.cy,
                       self.width - other.width, self.height - other.height]))

    def intersection(self, other):
        left = max(self.cx - self.width/2., other.cx - other.width/2.)
        right = min(self.cx + self.width/2., other.cx + other.width/2.)
        width = max(right - left, 0)
        top = max(self.cy - self.height/2., other.cy - other.height/2.)
        bottom = min(self.cy + self.height/2., other.cy + other.height/2.)
        height = max(bottom - top, 0)
        return width * height

    def area(self):
        return self.height * self.width

    def union(self, other):
        return self.area() + other.area() - self.intersection(other)

    def iou(self, other):
        return self.intersection(other) / self.union(other)

    def rescale(self, factor_x, factor_y=None):
        if factor_y is None:
            factor_y = factor_x
        self.x1 = (self.cx - (self.width/2.0)*factor_x)
        self.y1 = (self.cy - (self.height/2.0)*factor_y)
        self.x2 = (self.cx + (self.width/2.0)*factor_x)
        self.y2 = (self.cy + (self.height/2.0)*factor_y)

    def transform(self, resize_factor, x_corr, y_corr):
        self.x1 = self.x1 * resize_factor[0] + x_corr
        self.x2 = self.x2 * resize_factor[0] + x_corr
        self.y1 = self.y1 * resize_factor[1] + y_corr
        self.y2 = self.y2 * resize_factor[1] + y_corr
        self.cx = (self.x1 + self.x2)/2.
        self.cy = (self.y1 + self.y2)/2.
        self.width = self.x2 - self.x1
        self.height = self.y2 - self.y1

    def cov(self, other):
        return self.intersection(other) / float(self.width * self.height)

    def __eq__(self, other):
        return (self.cx == other.cx and
                self.cy == other.cy and
                self.width == other.width and
                self.height == other.height and
                self.confidence == other.confidence)

    def to_dict(self):
        return {"x1": self.x1, "y1": self.y1, "x2": self.x2, "y2": self.y2,
                # "score": self.score, "cx": self.cx, "cy": self.cy,
                # "width": self.width, "height": self.height,
                # "confidence": self.confidence
                }

    def __repr__(self):
        return str(self.to_dict())


class RectXY(Rect):
    def __init__(self, bbox, class_label=-1, score=1.0):
        self.x1 = bbox[0]
        self.y1 = bbox[1]
        self.x2 = bbox[2]
        self.y2 = bbox[3]
        self.width = self.x2 - self.x1
        self.height = self.y2 - self.y1
        self.class_label = class_label
        self.truncated = 0
        self.score = score
        self.confidence = score
        self.cx = (self.x1 + self.x2) / 2
        self.cy = (self.y1 + self.y2) / 2
