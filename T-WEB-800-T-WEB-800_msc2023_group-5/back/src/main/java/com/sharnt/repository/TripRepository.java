package com.sharnt.repository;

import com.sharnt.model.Trip;
import org.springframework.data.domain.Pageable;
import org.springframework.data.repository.CrudRepository;

public interface TripRepository  extends CrudRepository<Trip, Integer> {
    Object findAll(Pageable any);
}

