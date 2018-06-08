from controller import crop


class BusDetection:

    variables_set = False
    def crop_with_line(self, line_coords, width, height, calculated_crop):
        if not calculated_crop:
            print(line_coords[0][0], height - line_coords[0][1], line_coords[0][2],
                  height - line_coords[0][3], line_coords[1][0], height - line_coords[1][1],
                  line_coords[1][2], height - line_coords[1][3])

            img_width = width
            img_height = height
            print(img_width)
            print(img_height)

            self.x1_ratio = line_coords[0][0] / img_width
            self.y1_ratio = (height - line_coords[0][1]) / img_height
            self.x2_ratio = line_coords[0][2] / img_width
            self.y2_ratio = (height - line_coords[0][3]) / img_height
            self.x3_ratio = line_coords[1][0] / img_width
            self.y3_ratio = (height - line_coords[1][1]) / img_height
            self.x4_ratio = line_coords[1][2] / img_width
            self.y4_ratio = (height - line_coords[1][3]) / img_height
            self.variables_set = True

    def crop(self, frame):
        if self.variables_set:
            crop.crop_image(self.x1_ratio, self.y1_ratio, self.x2_ratio,
                            self.y2_ratio, self.x3_ratio,
                            self.y3_ratio, self.x4_ratio,
                            self.y4_ratio, frame)