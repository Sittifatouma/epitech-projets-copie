package com.sharnt.service;

import com.sharnt.exception.ResourceNotFoundException;
import com.sharnt.model.Example;
import com.sharnt.repository.ExampleRepository;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.logging.Logger;

@Service
public class ExampleService {
    private static final Logger logger = Logger.getLogger(ExampleService.class.getName());

    private final ExampleRepository exampleRepository;


    public ExampleService(ExampleRepository exampleRepository) {
        this.exampleRepository = exampleRepository;
    }

    /**
     * Example of POST method
     *
     * @param example
     * @return
     */
    public ResponseEntity<Example> addExample(Example example) {
        logger.info(String.format("Create example #{%s} with col1 '%s' and col2 '%s'", example.getId(), example.getCol1(), example.getCol2()));

        example = exampleRepository.save(example);

        return new ResponseEntity<>(example, HttpStatus.CREATED);
    }


    /**
     * Example of Get method
     *
     * @param id
     * @return
     */
    public ResponseEntity<Example> getExample(Integer id) {
        logger.info(String.format("Get Event #{%s}", id));

        Example event = exampleRepository.findById(id).orElseThrow(() -> new ResourceNotFoundException("event.uid", id.toString()));
        return new ResponseEntity<>(event, HttpStatus.OK);
    }

    public ResponseEntity<List<Example>> getAllExample() {
        logger.info(String.format("Get all Events"));
        List<Example> event = (List<Example>) exampleRepository.findAll();
        return new ResponseEntity<>(event, HttpStatus.OK);
    }


    /**
     * Example of PUT method
     *
     * @param id
     * @param example
     * @return
     */
    public ResponseEntity<Example> editExample(Integer id, Example example) {
        logger.info(String.format("Edit Event #%d", id));

        exampleRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("event.id", id.toString()));

        example.setId(id);
        example = exampleRepository.save(example);

        return new ResponseEntity<>(example, HttpStatus.OK);
    }

    /**
     * Example of DELETE method
     *
     * @return
     */
    public ResponseEntity<Void> deleteExample(Integer id) {
        logger.info(String.format("Delete Event #%d", id));

        exampleRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Event.id", id.toString()));

        exampleRepository.deleteById(id);
        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }


}
