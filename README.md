# DRF Template

Django 4.2.3 h5game 后端项目模板



## Installation

使用3.10.4创建虚拟环境后

```shell
pip install pipenv
pipenv install
```



## Script

运行配置

- 添加Django Server, Server name 固定为 `project`
- host=127.0.0.1 prot=82xx  # xx为管理端站点id
- Environment variables: `PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=project.settings;APP_ENV=dev`
- settings 中需要修改环境变量的有
  - Django Console
  - Django (中的Settings也需要指定对应settings文件)
  - Python Console
  - Terminal
- project 和 apps 文件夹需要 Mark Directory  >  Sources Root



## Precautions

新项目复制时需要修改的地方

- `.env.prod`文件信息

- 添加`.env.dev`文件,从`.env.prod`中复制,并修改其配置
- `uwsgi.ini`文件信息
- `settings` 中的 `SECRET_KEY`

  ```python
  # pip install django-extensions
  from django.core.management.utils import get_random_secret_key
  
  secret_key = get_random_secret_key()
  print(secret_key)
  ```

  



## Other

app 命名规则

- app命名应与网站类型一致，game类型网站应该命名为game...
- 与管理端交互的app命名为 `system`

