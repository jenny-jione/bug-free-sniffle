const fs = require('fs');

// let obj = {
//     SIG_CD: '11110',
//     SIG_KOR_NM: '종로구'
// };

// convert JSON object to a string
const data = JSON.stringify(obj, null, 4);
  // write file to disk
  fs.writeFile('./Data Processing/json/outcome/seoul_gu.json', data, 'utf8', (err) => {

    if (err) {
      console.log(`Error writing file: ${err}`);
    } else {
      console.log(`File is written successfully!`);
    }

  });

//
