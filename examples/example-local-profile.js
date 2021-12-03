const puppeteer = require('puppeteer-core');
const GoLogin = require('../gologin');

(async () =>{
    const GL = new GoLogin({
        token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MTc4ZDEyMDM0MWY2OGY1YzlmYjQzYTkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWE3N2FjZWU4MjhjOTRmNTA0NzhhMGUifQ.jvQPpHdtwXptJQN5NKySEVpB0JTp8vRmkWR7Z9uUkBs",
        profile_id: "61a79952a8084fead8495f8a",
        executablePath: '/usr/bin/orbita-browser/chrome',
        tmpdir: '/my/tmp/dir',
    });
    const wsUrl = await GL.startLocal(); 
    const browser = await puppeteer.connect({
        browserWSEndpoint: wsUrl.toString(), 
        ignoreHTTPSErrors: true,
    });

    const page = await browser.newPage();
    await page.goto('https://myip.link');   
    console.log(await page.content());
    await browser.close();
    await GL.stopLocal({posting: false});
})();
