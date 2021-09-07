package org.tektutor;

import org.junit.Test;
import static org.junit.Assert.*;

public class HelloTest {

	@Test
	public void testSayHello() {
		Hello hello = new Hello();

		String expectedResponse = "Hello DevOps!";
		String actualResponse   = hello.sayHello();

		assertEquals ( expectedResponse, actualResponse );
	}

}
