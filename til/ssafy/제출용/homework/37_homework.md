# Web API를 활용한 JS 응용

### 학습해야 할 내용

- Web API에 Axios 라이브러리를 활용해 요청 보내기

**1.**  Axios를 사용하는 아래 코드를 완성하시오.

- Browser는 axios CDN을 통해
- Node는 npm install 과 require 를 통해 axios를 가져와야 한다.

```javascript
const URL = "https://dog.ceo/api/breeds/image/random"
axios.get(URL)
    .then(res => {
    // imgSrc 상수에 res 에서 개 image 의 URL 을 뽑아서 저장한다.
    // console.log(res.data.message)
    const imgSrc = res.data.message
    // imgSrc 를 return 한다.
    return imgSrc
})
    .then(imageSource => {
    // imageSource 를 콘솔에 출력한다.
    console.log(imageSource)
});

```

