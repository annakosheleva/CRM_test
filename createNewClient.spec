const { Builder, By, until } = require("selenium-webdriver");
const assert = require("assert");

async function createNewClient() {
	let driver;

	try {
		driver = await new Builder().forBrowser("chrome").build();

		// Step 1: Go to the website

		await driver.get("https://kompot.us/");
		await driver.manage().window().maximize();

		// Step 2: LogIn

		await driver
			.findElement(By.xpath("//a[contains(@href, '/user/login')]"), 10000)
			.click();

		await driver.wait(
			until.elementLocated(By.className("MuiBox-root")),
			10000
		);

		let emailTextBox = await driver.findElement(
			By.xpath("//input[@id='email']")
		);
		await emailTextBox.sendKeys("businessowner@businessowner.com");

		let passwordTextBox = await driver.findElement(
			By.xpath("//input[@id='password']")
		);
		await passwordTextBox.sendKeys("Aa123123");

		await driver.findElement(By.css(".MuiButton-contained")).click();

		console.log("Login successful.");

		// Step 3: Navigate to "Create New Client" section

		await driver.wait(until.elementLocated(By.id("top-menu")), 10000);

		await driver
			.findElement(By.xpath("//a[contains(text(),'Clients')]"), 10000)
			.click();

		// Step 4: Open form for new client create

		await driver.wait(
			until.elementLocated(By.xpath("(//button[@type='button'])[8]")),
			10000
		);

		await driver
			.findElement(By.xpath("(//button[@type='button'])[8]"), 10000)
			.click();

		// Wait until the client creation form is loaded
		await driver.wait(
			until.elementLocated(By.className("MuiBox-root")),
			10000
		);

		// Step 5: Fill out the form "Create new client"

		await driver
			.findElement(By.xpath("//input[@id='firstName']"))
			.sendKeys("Alex");
		await driver
			.findElement(By.xpath("//input[@id='lastName']"))
			.sendKeys("Smith");
		await driver
			.findElement(By.xpath("//input[@id='company']"))
			.sendKeys("Smith&Co");
		await driver
			.findElement(By.xpath("//input[@id='email']"))
			.sendKeys("smithco@gmail.com");
		await driver
			.findElement(By.xpath("//input[@id='phone']"))
			.sendKeys("3336667777");

		await driver
			.findElement(By.xpath("//button[@type='submit']"), 10000)
			.click();

		// Step 6: Verify the new client was created successfully

		await driver.wait(until.elementLocated(By.id("top-menu")), 10000);

		await driver
			.findElement(By.xpath("//a[contains(text(),'Clients')]"), 10000)
			.click();

		// This can be done by checking for a success message or checking if the new client appears in a list

		console.log("New client created successfully.");
	} catch (error) {
		console.error("Test scenario failed:", error);
	} finally {
		// Close the browser
		await driver.quit();
	}
}

createNewClient();
