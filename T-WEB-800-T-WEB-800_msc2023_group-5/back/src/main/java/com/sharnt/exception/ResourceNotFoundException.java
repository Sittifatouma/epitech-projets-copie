package com.sharnt.exception;

import com.sharnt.reponse.ErrorResponse;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

public class ResourceNotFoundException extends RuntimeException {

    private String resourceName;

    private String resourceValue;

    public ResourceNotFoundException(String resourceName, String resourceValue) {
        super(formatError(resourceName, resourceValue));

        this.resourceName = resourceName;
        this.resourceValue = resourceValue;
    }

    public ResponseEntity<ErrorResponse> asResponse() {
        return new ResponseEntity<>(new ErrorResponse(formatError(resourceName, resourceValue)), HttpStatus.NOT_FOUND);
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
        return String.format("Resource '%s' with value '%s' not found", resourceName, resourceValue);
    }

}
