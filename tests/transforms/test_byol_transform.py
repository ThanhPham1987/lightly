from PIL import Image

from lightly.transforms.byol_transform import (
    BYOLTransform,
    BYOLView1Transform,
    BYOLView2Transform,
)


def test_view_on_pil_image():
    single_view_transform = BYOLView1Transform(input_size=32)
    sample = Image.new("RGB", (100, 100))
    output = single_view_transform(sample)
    assert output.shape == (3, 32, 32)


def test_multi_view_on_pil_image():
    multi_view_transform = BYOLTransform(
        view_1_transform=BYOLView1Transform(input_size=32),
        view_2_transform=BYOLView2Transform(input_size=32),
    )
    sample = Image.new("RGB", (100, 100))
    output = multi_view_transform(sample)
    assert len(output) == 2
    assert output[0].shape == (3, 32, 32)
    assert output[1].shape == (3, 32, 32)
