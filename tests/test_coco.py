from datetime import datetime
from typing import Any, Dict, List

from annococo.coco import COCO, Annotations, Categories, Images, Info, Licenses


def test_info(sample_info: Dict[str, Any]):
    """Infoクラスのテスト"""

    info = Info(**sample_info)
    assert info.year == 2021
    assert info.version == "1.0"
    assert info.description == "Sample COCO dataset"
    assert info.contributor == "User"
    assert info.url == "https://example.com"
    assert info.date_created == datetime(2021, 10, 1).isoformat()


def test_images(sample_images: List[Dict[str, Any]]):
    """Imagesクラスのテスト"""

    for image_data in sample_images:
        image = Images(**image_data)
        assert image.id == image_data["id"]
        assert image.width == image_data["width"]
        assert image.height == image_data["height"]
        assert image.file_name == image_data["file_name"]
        assert image.license == image_data["license"]
        assert image.flickr_url == image_data["flickr_url"]
        assert image.coco_url == image_data["coco_url"]
        assert image.date_captured == image_data["date_captured"]


def test_annotations(sample_annotations: List[Dict[str, Any]]):
    """Annotationsクラスのテスト"""

    for annotation_data in sample_annotations:
        annotation = Annotations(**annotation_data)
        assert annotation.id == annotation_data["id"]
        assert annotation.image_id == annotation_data["image_id"]
        assert annotation.category_id == annotation_data["category_id"]
        assert annotation.segmentation == annotation_data["segmentation"]
        assert annotation.area == annotation_data["area"]
        assert annotation.bbox == annotation_data["bbox"]
        assert annotation.iscrowd == annotation_data["iscrowd"]


def test_licenses(sample_licenses: List[Dict[str, Any]]):
    """Licensesクラスのテスト"""

    for license_data in sample_licenses:
        license = Licenses(**license_data)
        assert license.id == license_data["id"]
        assert license.name == license_data["name"]
        assert license.url == license_data["url"]


def test_categories(sample_categories: List[Dict[str, Any]]):
    """Categoriesクラスのテスト"""

    for category_data in sample_categories:
        category = Categories(**category_data)
        assert category.id == category_data["id"]
        assert category.name == category_data["name"]
        assert category.supercategory == category_data["supercategory"]


def test_coco(sample_coco: Dict[str, Any]):
    """COCOクラスのテスト"""
    coco = COCO(sample_coco)

    assert coco.info == sample_coco["info"]
    assert coco.images == sample_coco["images"]
    assert coco.annotations == sample_coco["annotations"]
    assert coco.licenses == sample_coco["licenses"]
    assert coco.categories == sample_coco["categories"]
