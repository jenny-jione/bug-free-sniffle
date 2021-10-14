// seoul_emd와 seoul_sig json 파일에서 CD와 KOR_NM만 읽어서 출력하는 코드
// 21-10-14

const fs = require('fs');
fs.readFile('./Data Processing/json/src/seoul_sig.json', (err, data) => { // 파일 읽기
  if (err) throw err;
  const seoul = JSON.parse(data); // json.parse로 파싱
  var gu = seoul.features;

  gu.forEach(function(item, idx, arr) {
    var sig = item.properties;
    console.log(sig.SIG_CD, sig.SIG_KOR_NM);
  });
});


fs.readFile('./Data Processing/json/src/seoul_emd.json', (err, data) => { // 파일 읽기
  if (err) throw err;
  const seoul = JSON.parse(data); // json.parse로 파싱

  var dong = seoul.features;
  dong.forEach(function(item, idx, arr) {
    var emd = item.properties;
    console.log(emd.EMD_CD, emd.EMD_KOR_NM);
  });
});
