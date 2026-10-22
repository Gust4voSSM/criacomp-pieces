import hashlib
from pathlib import Path

class VNLoadCachedRGBA:
    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'path': ('STRING', {}), 'sha256': ('STRING', {})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'run'
    CATEGORY = 'VN Sprites/Test'
    def run(self, path, sha256):
        import io
        import numpy as np
        import torch
        from PIL import Image
        data = Path(path).read_bytes()
        if hashlib.sha256(data).hexdigest() != sha256:
            raise ValueError('Reference hash mismatch')
        with Image.open(io.BytesIO(data)) as im:
            if im.mode != 'RGBA':
                raise ValueError('Reference must already be RGBA')
            pixels = np.array(im, dtype=np.float32) / 255.0
        return (torch.from_numpy(pixels).unsqueeze(0),)
    @classmethod
    def VALIDATE_INPUTS(cls, path, sha256):
        return True if Path(path).is_file() else 'Reference not found'

NODE_CLASS_MAPPINGS = {'VNLoadCachedRGBA': VNLoadCachedRGBA}
