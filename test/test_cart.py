from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_cart(login_in_driver):
    driver = login_in_driver

    # Agregar producto al carrito
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()

    # Verificar contador del carrito
    contador_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert contador_cart .text ==   "1", "El producto no se agrego correctamente"

    # Obtener Nombre del primer producto - como todos tienen el mismo nombre de la clase agrego el indice para identificarlo
    product_name = driver.find_elements(By.CLASS_NAME,"inventory_item_name")[0].text
    
    # Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Obtener nombre del producto en el carrito
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    
    #comparar los nombres
    assert cart_item == product_name , "El producto agregado no coinciede "

