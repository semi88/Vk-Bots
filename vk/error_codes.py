"""
// @apply https://raw.githubusercontent.com/VKCOM/vk-api-schema/master/methods.data

const data = JSON.parse(document.body.innerText)
let s = ''
for (let error of data.errors) {
  s += `${error.name} = ${error.code}\n`
}
consol.log(s)
"""
API_ERROR_UNKNOWN = 1
API_ERROR_DISABLED = 2
API_ERROR_METHOD = 3
API_ERROR_SIGNATURE = 4
API_ERROR_AUTH = 5
API_ERROR_TOO_MANY = 6
API_ERROR_PERMISSION = 7
API_ERROR_REQUEST = 8
API_ERROR_FLOOD = 9
API_ERROR_SERVER = 10
API_ERROR_ENABLED_IN_TEST = 11
API_ERROR_CAPTCHA = 14
API_ERROR_ACCESS = 15
API_ERROR_AUTH_HTTPS = 16
API_ERROR_AUTH_VALIDATION = 17
API_ERROR_METHOD_PERMISSION = 20
API_ERROR_METHOD_ADS = 21
API_ERROR_METHOD_DISABLED = 23
API_ERROR_NEED_CONFIRMATION = 24
API_ERROR_VOTES_PERMISSION = 500
API_ERROR_ACCESS_AUDIO = 201
API_ERROR_ACCESS_GROUP = 203
API_ERROR_PARAM_USER_ID = 113
API_ERROR_PARAM = 100
API_ERROR_ALBUM_FULL = 300
API_ERROR_ACCESS_ALBUM = 200
API_ERROR_ADS_SPECIFIC = 603
API_ERROR_ADS_PERMISSION = 600
API_ERROR_PARAM_TIMESTAMP = 150
API_ERROR_PARAM_API_ID = 101
API_ERROR_USER_DELETED = 18
