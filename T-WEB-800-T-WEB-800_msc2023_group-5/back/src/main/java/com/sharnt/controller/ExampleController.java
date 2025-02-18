package com.sharnt.controller;


import com.sharnt.model.Example;
import com.sharnt.service.ExampleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;


@RestController
public class ExampleController {

    @Autowired
    private ExampleService exampleService;

    @GetMapping("/example/{id}")
    @ResponseBody
    ResponseEntity<Example> getDeviceByUID(@PathVariable Integer id) {
        return exampleService.getExample(id);
    }

    @GetMapping("/examples")
    @ResponseBody
    ResponseEntity<List<Example>> getAll() {
        return exampleService.getAllExample();
    }

    @PostMapping("/example")
    @ResponseBody
    ResponseEntity<Example> createDevice(@RequestBody @Valid Example example) {
        return exampleService.addExample(example);
    }

    @PutMapping("/example/{id}")
    @ResponseBody
    ResponseEntity<Example> edit(@PathVariable Integer id, @RequestBody @Valid Example example) {
        return exampleService.editExample(id, example);
    }


    @DeleteMapping("/example/{id}")
    @ResponseBody
    ResponseEntity<Void> delete(@PathVariable Integer id) {
        return exampleService.deleteExample(id);
    }

}