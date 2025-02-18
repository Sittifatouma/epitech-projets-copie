package com.sharnt;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class WebApplication implements CommandLineRunner {

		public static void main (String[]args){
		SpringApplication.run(WebApplication.class, args);
	}

		@Override
		public void run (String...args) throws Exception {
		// TODO Auto-generated method stub
			System.out.println("test run start");
			System.out.println("test run end");
	}
}