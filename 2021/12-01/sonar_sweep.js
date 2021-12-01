const fs = require('fs')

try {
  const data = fs.readFileSync('./test-input-part-1.txt', 'utf8')
  console.log(data)
} catch (err) {
  console.error(err)
}

