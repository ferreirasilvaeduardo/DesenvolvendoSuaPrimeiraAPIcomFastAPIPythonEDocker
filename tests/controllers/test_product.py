from datetime import datetime
from typing import List
from unittest.mock import AsyncMock

import pytest
from fastapi import status

from src.usecases.product import ProductUsecase
from src.utils.exceptions import InsertionException, NotFoundException
from tests.factories import product_data


async def test_patch_should_update_product(mocker):
    product_id = "123"
    updates = {"price": 20.0}
    updated_at = datetime(2025, 3, 21)

    # Mock da coleção
    mock_collection = mocker.Mock()
    mock_collection.find_one = AsyncMock(
        side_effect=[
            {"id": product_id, "price": 10.0},
            {"id": product_id, "price": 20.0, "updated_at": updated_at},
        ]
    )
    mock_collection.update_one = AsyncMock(return_value=mocker.Mock(modified_count=1))

    # Mock da classe ProductUsecase
    usecase = ProductUsecase(mock_collection)
    updated_product = await usecase.patch(product_id, updates)

    assert updated_product["price"] == 20.0
    assert "updated_at" in updated_product
    assert updated_product["updated_at"] == updated_at


async def test_patch_should_return_not_found(client, mocker):
    mocker.patch(
        "src.usecases.product.ProductUsecase.patch",
        side_effect=NotFoundException("Product with ID 123 not found"),
    )

    response = await client.patch("/products/123", json={"price": 20.0})
    assert response.status_code == 404
    assert response.json() == {"detail": "Product with ID 123 not found"}


async def test_post_should_return_error_on_insertion_failure(client, mocker):
    # Simula um erro na inserção
    mocker.patch(
        "src.usecases.product.ProductUsecase.create",
        side_effect=InsertionException("Simulated insertion error"),
    )

    response = await client.post(
        "/products/",
        json={"name": "Produto A", "quantity": 10, "price": "10.0", "status": True},
    )
    assert response.status_code == 500
    assert response.json() == {"detail": "Simulated insertion error"}


async def test_controller_create_should_return_success(client, products_url):
    response = await client.post(products_url, json=product_data())

    content = response.json()

    del content["created_at"]
    del content["updated_at"]
    del content["id"]

    assert response.status_code == status.HTTP_201_CREATED
    assert content == {
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }


async def test_controller_get_should_return_success(
    client, products_url, product_inserted
):
    response = await client.get(f"{products_url}{product_inserted.id}")

    content = response.json()

    del content["created_at"]
    del content["updated_at"]

    assert response.status_code == status.HTTP_200_OK
    assert content == {
        "id": str(product_inserted.id),
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }


async def test_controller_get_should_return_not_found(client, products_url):
    response = await client.get(f"{products_url}4fd7cd35-a3a0-4c1f-a78d-d24aa81e7dca")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Product not found with filter: 4fd7cd35-a3a0-4c1f-a78d-d24aa81e7dca"
    }


@pytest.mark.usefixtures("products_inserted")
async def test_controller_query_should_return_success(client, products_url):
    response = await client.get(products_url)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), List)
    assert len(response.json()) > 1


async def test_controller_patch_should_return_success(
    client, products_url, product_inserted
):
    response = await client.patch(
        f"{products_url}{product_inserted.id}", json={"price": "7.500"}
    )

    content = response.json()

    del content["created_at"]
    del content["updated_at"]

    assert response.status_code == status.HTTP_200_OK
    assert content == {
        "id": str(product_inserted.id),
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "7.500",
        "status": True,
    }


async def test_controller_delete_should_return_no_content(
    client, products_url, product_inserted
):
    response = await client.delete(f"{products_url}{product_inserted.id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT


async def test_controller_delete_should_return_not_found(client, products_url):
    response = await client.delete(
        f"{products_url}4fd7cd35-a3a0-4c1f-a78d-d24aa81e7dca"
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Product not found with filter: 4fd7cd35-a3a0-4c1f-a78d-d24aa81e7dca"
    }
