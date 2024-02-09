from datetime import datetime
from typing import Any

import pytest


@pytest.fixture
def sample_info() -> dict[str, Any]:
    """COCOFormatのinfoに関するサンプルデータを作成

    Returns:
        dict: infoのサンプルデータ
    """
    return {
        "year": 2021,
        "version": "1.0",
        "description": "Sample COCO dataset",
        "contributor": "User",
        "url": "https://example.com",
        "date_created": datetime(2021, 10, 1).isoformat(),
    }


@pytest.fixture
def sample_images() -> list[dict]:
    """COOCFormatのimagesに関するサンプルデータを作成

    Returns:
        list[dict]: imagesのサンプルデータ
    """
    return [
        {
            "id": 1,
            "width": 640,
            "height": 480,
            "file_name": "image1.jpg",
            "license": 1,
            "flickr_url": "https://flickr.com",
            "coco_url": "https://example.com",
            "date_captured": datetime(2021, 10, 1).isoformat(),
        },
        {
            "id": 2,
            "width": 800,
            "height": 600,
            "file_name": "image2.jpg",
            "license": 2,
            "flickr_url": "https://flickr.com",
            "coco_url": "https://example.com",
            "date_captured": datetime(2021, 10, 2).isoformat(),
        },
    ]


@pytest.fixture
def sample_annotations() -> list[dict]:
    """COOCFormatのannotationsに関するサンプルデータを作成

    Returns:
        list[dict]: annotationsのサンプルデータ
    """
    return [
        {
            "id": 1,
            "image_id": 1,
            "category_id": 1,
            "segmentation": [[10, 10, 100, 10, 100, 100, 10, 100]],
            "area": 1000,
            "bbox": [10, 10, 90, 90],
            "iscrowd": 0,
        },
        {
            "id": 2,
            "image_id": 2,
            "category_id": 1,
            "segmentation": [[10, 10, 100, 10, 100, 100, 10, 100]],
            "area": 1000,
            "bbox": [10, 10, 90, 90],
            "iscrowd": 0,
        },
    ]


@pytest.fixture
def sample_licenses() -> list[dict]:
    """COOCFormatのlicensesに関するサンプルデータを作成

    Returns:
        list[dict]: licensesのサンプルデータ
    """
    return [
        {
            "id": 1,
            "name": "license1",
            "url": "https://example.com",
        },
        {
            "id": 2,
            "name": "license2",
            "url": "https://example.com",
        },
    ]


@pytest.fixture
def sample_categories() -> list[dict]:
    """COOCFormatのcategoriesに関するサンプルデータを作成

    Returns:
        list[dict]: categoriesのサンプルデータ
    """
    return [
        {
            "id": 1,
            "name": "category1",
            "supercategory": "object",
        },
        {
            "id": 2,
            "name": "category2",
            "supercategory": "object",
        },
    ]


@pytest.fixture
def sample_coco(
    sample_info: dict[str, Any],
    sample_images: list[dict],
    sample_annotations: list[dict],
    sample_licenses: list[dict],
    sample_categories: list[dict],
) -> dict[str, Any]:
    """COCOFormatのサンプルデータを作成

    Args:
        sample_info (dict[str, Any]): infoのサンプルデータ
        sample_images (list[dict]): imagesのサンプルデータ
        sample_annotations (list[dict]): annotationsのサンプルデータ
        sample_licenses (list[dict]): licensesのサンプルデータ
        sample_categories (list[dict]): categoriesのサンプルデータ

    Returns:
        dict: COCOのサンプルデータ
    """
    return {
        "info": sample_info,
        "images": sample_images,
        "annotations": sample_annotations,
        "licenses": sample_licenses,
        "categories": sample_categories,
    }
