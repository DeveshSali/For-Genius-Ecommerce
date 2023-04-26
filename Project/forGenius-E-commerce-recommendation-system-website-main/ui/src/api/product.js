import request from '../utils/request'

export const product_view = parameter => {
    return request({
      method: 'GET',
      url: '/product/user/view/',
      params: parameter
    })
}

export const rec_guest = parameter => {
  return request({
    method: 'GET',
    url: '/product/recommendation/public/',
    params: parameter
  })
}

export const rec_user = parameter => {
  return request({
    method: 'GET',
    url: '/product/recommendation/private/',
    params: parameter
  })
}

export const ser_res = parameter => {
  return request({
    method: 'GET',
    url: '/product/search/result/',
    params: parameter
  })
}