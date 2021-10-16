// 원래 있던 seoul_emd.json 파일에서 EMD_CD, EMD_KOR_NM 만 새로운 json 파일에 저장하는 코드
// 21-10-15

const fs = require('fs');

var obj = [];

fs.readFile('./Data Processing/json/src/seoul_emd.json', (err, data) => { // 파일 읽기
  if (err) throw err;
  const seoul = JSON.parse(data); // json.parse로 파싱
  var dong = seoul.features;

  dong.forEach(function(item, idx, arr) {
    var emd = item.properties;
    // console.log(emd.EMD_CD, emd.EMD_KOR_NM);
    var emdcd = emd.EMD_CD;
    var emdkr = emd.EMD_KOR_NM;
    var dong = {
      EMD_CD: emdcd,
      EMD_KOR_NM: emdkr
    }
    console.log(dong);
    obj.push(dong);
  });

  // convert JSON object to a string
  const data2 = JSON.stringify(obj, null, 4);
    // write file to disk
    fs.writeFile('./Data Processing/json/outcome/seoul_dong.json', data2, 'utf8', (err) => {

      if (err) {
        console.log(`Error writing file: ${err}`);
      } else {
        console.log(`File is written successfully!`);
      }
    });
});



//
