package com.sharnt.exception;

import java.util.ArrayList;
import java.util.List;

import com.sharnt.reponse.ErrorResponse;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;


public class BadRequestException extends RuntimeException {

    private String parameterName;
    private String message;

    public BadRequestException(String parameterName, String message) {
        super(formatError(parameterName, message));
        this.parameterName = parameterName;
        this.message = message;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public String getParameterName() {
        return parameterName;
    }

    public void setParameterName(String parameterName) {
        this.parameterName = parameterName;
    }

    public ResponseEntity<ErrorResponse> asResponse() {
        List<String> messages = new ArrayList<>();
        messages.add(message);

        return new ResponseEntity<>(
                new ErrorResponse(String.format("Parameter '%s' is malformed", parameterName), messages), HttpStatus.CONFLICT);
    }

    private static String formatError(String parameterName, String message) {
        return String.format("Parameter '%s' is malformed: %s", parameterName, message);
    }

}
