package com.sharnt.reponse;

import java.util.ArrayList;
import java.util.List;

public class ErrorResponse {

    private String error;

    private List<String> messages;

    public ErrorResponse(String error, List<String> messages) {
        this.error = error;
        setMessages(messages);
    }

    public ErrorResponse(String error) {
        this.error = error;
        this.messages = new ArrayList<>();
    }

    public String getError() {
        return error;
    }

    public void setError(String error) {
        this.error = error;
    }

    public List<String> getMessages() {
        return messages;
    }

    public void setMessages(List<String> messages) {
        if (messages == null) {
            this.messages = new ArrayList<>();
        } else {
            this.messages = new ArrayList<>(messages);
        }
    }

}
