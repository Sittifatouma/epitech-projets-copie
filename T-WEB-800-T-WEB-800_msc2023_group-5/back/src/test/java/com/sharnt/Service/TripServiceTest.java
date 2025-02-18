package com.sharnt.Service;

import com.sharnt.model.Trip;
import com.sharnt.repository.TripRepository;
import com.sharnt.service.TripService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.ArgumentMatchers;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;

import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertThat;
import static org.mockito.AdditionalAnswers.returnsFirstArg;
import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
public class TripServiceTest {

    @Mock
    private TripRepository tripRepository;

    @Autowired
    private TripService tripService;

    @BeforeEach
    void setup() {
        tripService = new TripService(tripRepository);
    }

    Trip genrateTrip() {
        Trip trip = new Trip();
        trip.setTitle("title");
        trip.setPicture("picture");
        trip.setType("type");
        trip.setStar("start");
        trip.setLatitude("15.151");
        trip.setLongitude("42.151");
        trip.setPrice("price");
        trip.setDescription("description");
        trip.setLink("link");
        return trip;
    }


    // Test add product
    @Test
    void whenCreatedTrip_ok() {
        Trip trip = genrateTrip();

        when(tripRepository.save(ArgumentMatchers.any(Trip.class))).then(returnsFirstArg());

        HttpStatus httpStatus = tripService.addTrip(trip).getStatusCode();

        assertThat(httpStatus, is(HttpStatus.CREATED));
    }

    /* Test add product
    @Test
    void whenSelectTrip_ok() {
        Trip trip = genrateTrip();

        when(tripRepository.findAll()).then(returnsFirstArg());

        HttpStatus httpStatus = tripService.getAllExample().getStatusCode();

        assertThat(httpStatus, is(HttpStatus.CREATED));
    }*/




}
