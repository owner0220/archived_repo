# REST API

### Background

- REST API 구조
- HTTP methods

### Goal

- REST API의 일반적인 설계에 대해 알아본다.

### Problem

- 아래의 두 코드에 적절한 데코레이터를 작성해 허용되지 않은 HTTP Method의 경우 405 Method Not Allowed 상태코드를 반환하도록 하시오.

```python
#방법 1
@require_GET
@require_POST

#방법 2
@require_http_methods(["GET","POST"])
```

