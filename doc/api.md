
## 2.3 AUTO接收sn获取结果反馈

### 2.3.1 功能描述

Agent尝试ssh设备并获取设备sn后，通过该接口反馈AUTO获取结果

### 2.3.2 请求说明

> 请求方式： POST
>
> 请求URL： /api/v1/resources/net_devices/get_sn_result

### 2.3.3 HTTP 头定义

|     字段     |       参数       |
| :----------: | :--------------: |
| Content-Type | application/json |
| accept       | application/json |

### 2.3.4 请求参数

|         字段         | 类型 | 是否必填 | 说明           |
| :------------------: | :--: | :------: | -------------- |
| result             | string |    是    | 任务ID         |
| net_port_info      | list  |    是    | 测试需要的信息   |
| dev_info           | list  |    是    |测试需要的信息    |
| template_info      | list  |    是    | 测试需要的信息   |



### 2.3.6 返回结果

| 字段      | 类型   | 说明                               |
| --------- | ------ | ---------------------------------- |
| id        | int    | 任务ID                             |
| uuid      | string | 任务UUID                           |
| done      | bool   | 是否完成测试                       |
| name      | str    | 测试名称                           |
| user_uuid | str    | 用户uuid                           |
| running   | bool   | 测试是否正在执行，false为 未在执行 |

### 2.3.7 状态码

- 正确返回状态码

  | 状态码 |   说明   |
  | :----: | :------: |
  |  200   | 正常返回 |

  

- 错误状态码

  | 状态码 |             说明              |
  | :----: | :---------------------------: |
  |  401   | 表示用户没有权限（token错误） |
  |  404   |    Task instance not found    |
  |  400   |   Task instance is running    |
  |  400   |    Task instance has done     |


### 2.3.5 请求/返回示例
#### agent成功获取SN且auto在库中匹配到sn
- request
```
请求url: http://x.x.x.x:xxxx/api/v1/resources/net_devices/get_sn_result
方法:post
请求内容（json）：
{
  "result": "success",
  "failure_info": "N/A",
  "dev_info": {
    "sn": "123",
    "dhcp_ip": "192.168.33.10",
    "vendor": "H3C",
    "device_type": "FW"
  }
}

```

- response
```json
{
  "sn_match_result": "success",
  "dev_config_data": {
    "hostname": "NFV-SRV-1",
    "mng_ip": "10.10.10.1",
    "netmask": "24",
    "gw": "10.10.10.254"
  }
}
```















## 2.3 AUTO接收sn获取结果反馈

### 2.3.1 功能描述

Agent尝试ssh设备并获取设备sn后，通过该接口反馈AUTO获取结果

### 2.3.2 请求说明

> 请求方式： POST
>
> 请求URL： /api/v1/resources/net_devices/get_sn_result

### 2.3.3 HTTP 头定义

|     字段     |       参数       |
| :----------: | :--------------: |
| Content-Type | application/json |
| accept       | application/json |

### 2.3.4 请求参数

|         字段         | 类型 | 是否必填 | 说明           |
| :------------------: | :--: | :------: | -------------- |
| 请求头中的<task-id>  | int   |    是    | 任务ID         |
| net_port_info      | list  |    是    | 测试需要的信息   |
| dev_info           | list  |    是    |测试需要的信息    |
| template_info      | list  |    是    | 测试需要的信息   |

### 2.3.5 请求示例
```
请求url: http://x.x.x.x:xxxx/api/v1/resources/net_devices/get_sn_result
方法:post
请求内容（json）：
{
  "result": "success",
  "failure_info": "N/A",
  "dev_info": {
    "sn": "123",
    "dhcp_ip": "192.168.33.10",
    "vendor": "H3C",
    "device_type": "FW"
  }
}

```



### 2.3.6 返回结果

| 字段      | 类型   | 说明                               |
| --------- | ------ | ---------------------------------- |
| id        | int    | 任务ID                             |
| uuid      | string | 任务UUID                           |
| done      | bool   | 是否完成测试                       |
| name      | str    | 测试名称                           |
| user_uuid | str    | 用户uuid                           |
| running   | bool   | 测试是否正在执行，false为 未在执行 |

### 2.3.7 状态码

- 正确返回状态码

  | 状态码 |   说明   |
  | :----: | :------: |
  |  200   | 正常返回 |

  

- 错误状态码

  | 状态码 |             说明              |
  | :----: | :---------------------------: |
  |  401   | 表示用户没有权限（token错误） |
  |  404   |    Task instance not found    |
  |  400   |   Task instance is running    |
  |  400   |    Task instance has done     |

### 2.3.8 返回示例

```json
{
  "sn_match_result": "success",
  "dev_config_data": {
    "hostname": "NFV-SRV-1",
    "mng_ip": "10.10.10.1",
    "netmask": "24",
    "gw": "10.10.10.254"
  }
}
```


