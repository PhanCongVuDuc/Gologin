const puppeteer = require('puppeteer-core');
const GoLogin = require('./gologin');

(async () => {
  const GL = new GoLogin({
    token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MTc4ZDEyMDM0MWY2OGY1YzlmYjQzYTkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWE3N2FjZWU4MjhjOTRmNTA0NzhhMGUifQ.jvQPpHdtwXptJQN5NKySEVpB0JTp8vRmkWR7Z9uUkBs",
    profile_id: "61a7b48cb8e08cb7ea96e9b6",
  });

  const { status, wsUrl } = await GL.start().catch((e) => {
    console.trace(e);
    return { status: 'failure' };
  });

  if (status !== 'success') {
    console.log('Invalid status');
    return;
  }

  const browser = await puppeteer.connect({
    browserWSEndpoint: wsUrl.toString(),
    ignoreHTTPSErrors: true,
  });

  const page = await browser.newPage();
  await page.goto('https://myip.link/mini');
  console.log(await page.content());
  await browser.close();
  await GL.stop();
})();
