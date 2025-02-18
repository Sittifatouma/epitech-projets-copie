package com.sharnt;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.junit.Assert.*;

@ExtendWith(MockitoExtension.class)
class WebApplicationTests {


	@Test
	void contextLoads() {
	}

	@Test
	void affichageTest(){
		System.out.println("test ok");
		String str1="test sharnt";
		assertEquals("test sharnt", str1);
	}

}
