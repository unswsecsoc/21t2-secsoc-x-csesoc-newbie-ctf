const express = require('express');
const path = require('path');

const app = express();

const port = process.env.PORT;
const flag = process.env.FLAG;

app.use(express.static(path.join(__dirname, 'public')))

app.get('/', (_, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.get('/flag', (req, res) => {
    if (parseInt(req.query.u) >= 85) {
        res.send(flag);
    }
});

app.listen(port, () => {
    console.log(`Server listening on ${port}`);
});