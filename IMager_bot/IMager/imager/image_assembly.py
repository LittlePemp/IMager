from typing import Optional, Tuple

from PIL import Image
from settings.config import (RES_VOLUME, TEMP_VOLUME, TOPICS_VOLUME,
                             content_abs, results_abs, temp_abs, topics_abs)


class ImageEngine:
    def get_avg_colors(self, image_path: str) -> Optional[Tuple[int]]:
        try:
            rgb = self._get_rgb_attrs(image_path)
            attrs = (rgb[0, 0][0], rgb[0, 0][1], rgb[0, 0][2])
            return attrs
        except Exception as e:
            print(e)

    def _get_rgb_attrs(self, image_path: str):
        image = Image.open(image_path)
        return image.resize((1, 1)).load()
