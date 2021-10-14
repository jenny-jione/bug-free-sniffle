// 원래 있던 seoul_sig.json 파일에서 SIG_CD, SIG_KOR_NM 만 새로운 json 파일에 저장하는 코드
// 21-10-14

const fs = require('fs');

var obj = [];

fs.readFile('./Data Processing/json/src/seoul_sig.json', (err, data) => { // 파일 읽기
  if (err) throw err;
  const seoul = JSON.parse(data); // json.parse로 파싱
  var gu = seoul.features;

  gu.forEach(function(item, idx, arr) {
    var sig = item.properties;
    // console.log(sig.SIG_CD, sig.SIG_KOR_NM);
    var sigcd = sig.SIG_CD;
    var sigkr = sig.SIG_KOR_NM;
    var gu = {
      SIG_CD: sigcd,
      SIG_KOR_NM: sigkr
    }

    obj.push(gu);
  });

  // convert JSON object to a string
  const data2 = JSON.stringify(obj, null, 4);
    // write file to disk
    fs.writeFile('./Data Processing/json/outcome/seoul_gu.json', data2, 'utf8', (err) => {

      if (err) {
        console.log(`Error writing file: ${err}`);
      } else {
        console.log(`File is written successfully!`);
      }

    });
});



//
