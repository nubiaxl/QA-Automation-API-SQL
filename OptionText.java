import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;

public class OptionText {

	private static String wordlabel;
	private static String alertString;
	private static boolean isInAlertMessage;

	public static void main(String[] args) throws InterruptedException {
		// TODO Auto-generated method stub

		
		
		ChromeOptions ops = new ChromeOptions();
        ops.addArguments("--disable-notifications");
       
        System.setProperty("webdriver.chrome.driver", "chromedriver");
        WebDriver driver = new ChromeDriver(ops);
		driver.get("http://www.qaclickacademy.com/practice.php");
		
		WebDriverWait w=new WebDriverWait(driver,20);
		w.until(ExpectedConditions.elementToBeClickable(By.xpath("//h1[contains(text(),'Practice Page')]")));
		
		driver.findElement(By.cssSelector("#checkBoxOption3")).click();
		wordlabel = driver.findElement(By.xpath("//label[@for='honda']")).getText();
		System.out.println("|"+ wordlabel + "|");
		
		//Dropdown
		Select s = new Select(driver.findElement(By.id("dropdown-class-example")));
		s.selectByVisibleText(wordlabel);
		
		//Switch to Alert
		driver.findElement(By.id("name")).click();
		driver.findElement(By.id("name")).sendKeys(wordlabel);
		driver.findElement(By.id("alertbtn")).click();
		
		Thread.sleep(5000L);
		alertString = driver.switchTo().alert().getText();
		isInAlertMessage = alertString.contains(wordlabel);
		System.out.println(isInAlertMessage);
		if(isInAlertMessage)
			System.out.println("The alert message: " + alertString + "---- contains the word " + wordlabel);
		
		Thread.sleep(5000L);
		driver.switchTo().alert().accept();
		driver.quit();
	}
	
}
