import request from '../utils/request'

export const login = data => {
    return request({
      method: 'POST',
      url: 'user/login/',
      data
    })
}
export const signup = data => {
    return request({
      method: 'POST',
      url: 'user/register/',
      data
    })
}

export const signup_code = data => {
  return request({
    method: 'POST',
    url: 'user/register/send_code',
    data
  })
}

export const change_password = data => {
  return request({
    method: 'POST',
    url: 'user/change_password/',
    data
  })
} 

export const change_username = data => {
  return request({
    method: 'POST',
    url: 'user/change_username/',
    data
  })
} 

export const address_view = data => {
  return request({
    method: 'POST',
    url: 'user/address/view/',
    data
  })
}

export const logout = data => {
  return request({
    method: 'POST',
    url: 'user/logout/',
    data
  })
}

export const address_delete = data => {
  return request({
    method: 'DELETE',
    url: '/user/address/delete/',
    data
  })
}

export const interest_add = data => {
  return request({
    method: 'POST',
    url: '/user/interests/add/',
    data
  })
}

export const address_edit = data => {
  return request({
    method: 'POST',
    url: '/user/address/edit/',
    data
  })
}

export const address_add = data => {
  return request({
    method: 'POST',
    url: '/user/address/add/',
    data
  })
}

export const send_code = data => {
  return request({
    method: 'POST',
    url: '/user/send_reset_code/',
    data
  })
}

export const reset_password = data => {
  return request({
    method: 'POST',
    url: '/user/reset_password/',
    data
  })
}