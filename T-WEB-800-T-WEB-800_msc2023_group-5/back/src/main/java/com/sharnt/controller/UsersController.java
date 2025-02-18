package com.sharnt.controller;

import com.sharnt.model.Users;
import com.sharnt.service.UsersService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;


@RestController
@CrossOrigin(origins = "http://localhost:3000")
public class UsersController {

    @Autowired
    private UsersService usersService;


    @PostMapping("/Users")
    @ResponseBody
    ResponseEntity<Users> createDevice() {
        return usersService.createUser();
    }

}