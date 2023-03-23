const webdriver = require('selenium-webdriver');
const chrome = require('selenium-webdriver/firefox');
const fs = require('fs');

const options = new chrome.Options();
options.addArguments('--headless'); // Run Chrome in headless mode

const driver = new webdriver.Builder()
  .forBrowser('chrome')
  .setChromeOptions(options)
  .build();

(async () => {
  await driver.get('https://google.com');
  const screenshot = await driver.takeScreenshot();
  fs.writeFileSync('screenshot.png', screenshot, 'base64');
  await driver.quit();
})();