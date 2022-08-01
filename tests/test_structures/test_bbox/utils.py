from mmdet.structures.bbox import BaseInstanceBoxes


class ToyBaseInstanceBoxes(BaseInstanceBoxes):

    _bbox_dim = 4

    @property
    def centers(self):
        pass

    @property
    def areas(self):
        pass

    @property
    def widths(self):
        pass

    @property
    def heights(self):
        pass

    def flip(self, img_shape, direction='horizontal'):
        pass

    def translate(self, distances):
        pass

    def clip(self, img_shape):
        pass

    def rotate(self, center, angle, img_shape):
        pass

    def project(self, homography_matrix, img_shape=None):
        pass

    def rescale(self, rescale_factor):
        pass

    def rescale_size(self, rescale_factor):
        pass

    def is_bboxes_inside(self, img_shape):
        pass

    def find_inside_points(self, points):
        pass