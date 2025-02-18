package com.sharnt.exception;

import com.sharnt.reponse.ErrorResponse;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import java.util.Optional;

public class ResourceAlreadyExistingException extends RuntimeException {

    private String resourceName;

    private String resourceValue;

    public ResourceAlreadyExistingException(String resourceName, String resourceValue) {
        super(formatError(resourceName, resourceValue));

        this.resourceName = resourceName;
        this.resourceValue = resourceValue;
    }

    public ResponseEntity<ErrorResponse> asResponse() {
        return new ResponseEntity<>(new ErrorResponse(formatError(resourceName, resourceValue)), HttpStatus.CONFLICT);
    }

    public <T> void throwIfNotEmpty(Optional<T> value) throws ResourceAlreadyExistingException {
        if (value.isPresent()) {
            throw this;
        }
    }

    public String getResourceValue() {
        return resourceValue;
    }

    public void setResourceValue(String resourceValue) {
        this.resourceValue = resourceValue;
    }

    public String getResourceName() {
        return resourceName;
    }

    public void setResourceName(String resourceName) {
        this.resourceName = resourceName;
    }

    private static String formatError(String resourceName, String resourceValue) {
        return String.format("Resource '%s' with value '%s' already exists", resourceName, resourceValue);
    }
}
