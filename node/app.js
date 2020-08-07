const wkhtmltopdf = require('wkhtmltopdf');
const express = require('express');

const app = express();

app.get('/render', (req, res) => {
    const { url } = req.query;
    const options = {
        pageSize: 'A4',
        noStopSlowScripts: true,
        debugJavascript: true,
        debug: true,
    };
    wkhtmltopdf(url, options)
        .pipe(res);
});

const port = process.env.PORT || 8080;

app.listen(port, () => console.log(`Magic happening on ${port}`))