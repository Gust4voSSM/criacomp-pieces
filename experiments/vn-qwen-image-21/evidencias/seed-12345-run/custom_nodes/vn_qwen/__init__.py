"""Shared text and prompt assembly for native Qwen RGBA generation."""

class VNQwenText:
    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': ('STRING', {'multiline': True})}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'run'
    CATEGORY = 'VN Sprites/Qwen'

    def run(self, text):
        return (text,)


class VNQwenPrompt:
    @classmethod
    def INPUT_TYPES(cls):
        shared = {key: ('STRING', {'forceInput': True}) for key in ('prefix', 'character', 'framing', 'style', 'constraints', 'suffix')}
        return {'required': {**shared, 'action': ('STRING', {'multiline': True})}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'run'
    CATEGORY = 'VN Sprites/Qwen'

    def run(self, prefix, character, framing, style, constraints, suffix, action):
        parts = (prefix, character, action, framing, style, constraints, suffix)
        return (' '.join(part.strip().rstrip('. ,') + '.' for part in parts if part.strip()),)


class VNQwenEmptyLatent:
    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {
            'width': ('INT', {'default': 768, 'min': 32, 'max': 4096, 'step': 32}),
            'height': ('INT', {'default': 1152, 'min': 32, 'max': 4096, 'step': 32}),
            'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 1}),
        }}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'run'
    CATEGORY = 'VN Sprites/Qwen'

    def run(self, width, height, batch_size=1):
        import torch
        import comfy.model_management as mm
        if width % 32 or height % 32:
            raise ValueError('Qwen canvas dimensions must be multiples of 32')
        return ({'samples': torch.zeros([batch_size, 64, height // 16, width // 16], device=mm.intermediate_device())},)


NODE_CLASS_MAPPINGS = {'VNQwenEmptyLatent': VNQwenEmptyLatent, 'VNQwenText': VNQwenText, 'VNQwenPrompt': VNQwenPrompt}
