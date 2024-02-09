from datetime import datetime
from typing import Any, Dict, List

import pytest


@pytest.fixture
def sample_info() -> Dict[str, Any]:
    """COCOFormatのinfoに関するサンプルデータを作成

    Returns:
        Dict: infoのサンプルデータ
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
def sample_images() -> List[Dict[str, Any]]:
    """COOCFormatのimagesに関するサンプルデータを作成

    Returns:
        List[Dict]: imagesのサンプルデータ
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
def sample_annotations() -> List[Dict[str, Any]]:
    """COOCFormatのannotationsに関するサンプルデータを作成

    Returns:
        List[Dict]: annotationsのサンプルデータ
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
def sample_licenses() -> List[Dict[str, Any]]:
    """COOCFormatのlicensesに関するサンプルデータを作成

    Returns:
        List[Dict]: licensesのサンプルデータ
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
def sample_categories() -> List[Dict[str, Any]]:
    """COOCFormatのcategoriesに関するサンプルデータを作成

    Returns:
        List[Dict]: categoriesのサンプルデータ
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
    sample_info: Dict[str, Any],
    sample_images: List[Dict[str, Any]],
    sample_annotations: List[Dict[str, Any]],
    sample_licenses: List[Dict[str, Any]],
    sample_categories: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """COCOFormatのサンプルデータを作成

    Args:
        sample_info (Dict[str, Any]): infoのサンプルデータ
        sample_images (List[Dict[str, Any]]): imagesのサンプルデータ
        sample_annotations (List[Dict[str, Any]]): annotationsのサンプルデータ
        sample_licenses (List[Dict[str, Any]]): licensesのサンプルデータ
        sample_categories (List[Dict[str, Any]]): categoriesのサンプルデータ

    Returns:
        Dict: COCOのサンプルデータ
    """
    return {
        "info": sample_info,
        "images": sample_images,
        "annotations": sample_annotations,
        "licenses": sample_licenses,
        "categories": sample_categories,
    }
