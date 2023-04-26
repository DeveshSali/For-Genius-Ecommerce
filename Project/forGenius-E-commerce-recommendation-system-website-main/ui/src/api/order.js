import request from '../utils/request'

export const cart_add = data => {
    return request({
      method: 'POST',
      url: '/order/cart/add/',
      data
    })
}

export const cart_view = parameter => {
  return request({
    method: 'GET',
    url: '/order/cart/view/',
    params: parameter
  })
}

export const ord_view = parameter => {
  return request({
    method: 'GET',
    url: '/order/view/all/',
    params: parameter
  })
}

export const ord_sin_view = parameter => {
  return request({
    method: 'GET',
    url: '/order/view/',
    params: parameter
  })
}

export const cart_qua = data => {
  return request({
    method: 'POST',
    url: '/order/cart/product_quantity/edit/',
    data
  })
}

export const cart_del = data => {
  return request({
    method: 'DELETE',
    url: '/order/cart/remove/',
    data
  })
}

export const cart_create = data => {
  return request({
    method: 'POST',
    url: '/order/create/',
    data
  })
}

export const ord_pay = data => {
  return request({
    method: 'POST',
    url: '/order/pay/',
    data
  })
}

export const ord_share = data => {
  return request({
    method: 'POST',
    url: '/order/share/',
    data
  })
}
