package com.sharnt.service;

import com.sharnt.exception.ResourceNotFoundException;
import com.sharnt.model.Example;
import com.sharnt.model.Trip;
import com.sharnt.repository.ExampleRepository;
import com.sharnt.repository.TripRepository;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.logging.Logger;

@Service
public class TripService {
    private static final Logger logger = Logger.getLogger(TripService.class.getName());

    private final TripRepository tripRepository;


    public TripService(TripRepository tripRepository) {
        this.tripRepository = tripRepository;
    }

    /**
     * Example of POST method
     *
     * @param trip
     * @return
     */
    public ResponseEntity<Trip> addTrip(Trip trip) {
        logger.info(String.format("Create example #{%s} ", trip.getId()));

        trip = tripRepository.save(trip);

        return new ResponseEntity<>(trip, HttpStatus.CREATED);
    }


    /**
     * Example of Get method
     *
     * @param
     * @return
     */


    public ResponseEntity<List<Trip>> getAllExample() {
        logger.info(String.format("Get all Trip"));
        List<Trip> listTrip = (List<Trip>) tripRepository.findAll();
        return new ResponseEntity<>(listTrip, HttpStatus.OK);
    }



    /**
     * Example of DELETE method
     *
     * @return
     */
    public ResponseEntity<Void> deleteExample(Integer id) {
        logger.info(String.format("Delete Event #%d", id));

        tripRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Event.id", id.toString()));

        tripRepository.deleteById(id);
        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }


}
