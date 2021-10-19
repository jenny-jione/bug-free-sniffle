// seoul_gu.json과 seoul_dong.json 파일의 정보를 combine 해서 새로운 json 파일에 write 하는 코드
// 21-10-15

const fs = require('fs');

var seoul = [];

fs.readFile('./Data Processing/json/src/seoul_gu.json', (err, data) => { // 파일 읽기
  if (err) throw err;
  const districts = JSON.parse(data); // json.parse로 파싱

  var gu_arr = []; // 서울 구 배열 생성

  districts.forEach(function(item, idx, arr) {
    gu_arr.push({
      SIG_CD: item.SIG_CD,
      SIG_KOR_NM: item.SIG_KOR_NM
    });
  });

  fs.readFile('./Data Processing/json/src/seoul_dong.json', (err, data2) => { // 파일 읽기
    if (err) throw err;
    const dongs = JSON.parse(data2); // json.parse로 파싱

    var dong_arr = []; // 서울 구 배열 생성

    dongs.forEach(function(item, idx, arr) {
      dong_arr.push({
        EMD_CD: item.EMD_CD,
        EMD_KOR_NM: item.EMD_KOR_NM
      });
    });

    console.log(gu_arr.length);
    console.log(dong_arr.length);

    combineObject(gu_arr, dong_arr);

  });
});

function combineObject(gu, dong){
  var i = 0;  // 구 배열 도는 인덱스

  dong.forEach(function(item, idx, arr){
    var emdcd = item.EMD_CD;
    var emdkr = item.EMD_KOR_NM;

    // EMD_CD 앞의 다섯자리와 SIG_CD가 같으면
    if(emdcd.substr(0,5)==gu[i].SIG_CD){
      // console.log("Same!", emdcd, sigcd, sigkr, emdkr);
      // seoul obj에 프로퍼티를 추가한다.
      seoul.push({
        SIG_CD: gu[i].SIG_CD,
        EMD_CD: emdcd,
        SIG_KOR_NM: gu[i].SIG_KOR_NM,
        EMD_KOR_NM: emdkr
      });
    }

    // EMD_CD 앞의 다섯자리와 SIG_CD가 다른 경우, 다음 구로 넘어간 것이므로
    else{
      i++;  // 구 인덱스를 증가시키고
      seoul.push({  // 새로 추가한다.
        SIG_CD: gu[i].SIG_CD,
        EMD_CD: emdcd,
        SIG_KOR_NM: gu[i].SIG_KOR_NM,
        EMD_KOR_NM: emdkr
      })
    }
  });

  // convert JSON object to a string
  const data3 = JSON.stringify(seoul, null, 4);
    // write file to disk
    fs.writeFile('./Data Processing/json/outcome/seoul.json', data3, 'utf8', (err) => {

      if (err) {
        console.log(`Error writing file: ${err}`);
      } else {
        console.log(`File is written successfully!`);
      }
    });


}
