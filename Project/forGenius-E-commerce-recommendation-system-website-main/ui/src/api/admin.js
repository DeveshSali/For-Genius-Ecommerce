import request from '../utils/request'

  export const admin_view = data => {
    return request({
      method: 'POST',
      url: '/product/all/',
      data
    })
  }

  export const admin_ord = parameter => {
    return request({
      method: 'GET',
      url: '/order/admin_view/all/',
      params: parameter
    })
  }

  export const admin_sort = parameter => {
    return request({
      method: 'GET',
      url: '/product/all/sort/',
      params: parameter
    })
  }

  export const product_add = data => {
    return request({
      method: 'POST',
      url: '/product/add/',
      data
    })
  }

  export const product_edit = data => {
    return request({
      method: 'POST',
      url: '/product/edit/',
      data
    })
  }

  export const product_delete = data => {
    return request({
      method: 'DELETE',
      url: '/product/delete/',
      data
    })
  }