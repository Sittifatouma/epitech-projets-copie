package com.sharnt.service;

import com.sharnt.model.Users;
import com.sharnt.repository.UsersRepository;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.logging.Logger;


@Service
public class UsersService {
    private static final Logger logger = Logger.getLogger(TripService.class.getName());

    private final UsersRepository usersRepository;


    public UsersService(UsersRepository usersRepository) {
        this.usersRepository = usersRepository;
    }

    /**
     * Example of POST method
     *
     * @param
     * @return
     */
    public ResponseEntity<Users> createUser() {
        logger.info(String.format("Create Users "));
        Users users = new Users();
        LocalDate date = LocalDate.now();
        users.setCreatedDate(date);

        users = usersRepository.save(users);


        return new ResponseEntity<>(users, HttpStatus.CREATED);
    }


}
