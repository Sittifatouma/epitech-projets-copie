package com.sharnt.controller;

import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;
import com.mashape.unirest.http.exceptions.UnirestException;
import com.sharnt.model.Trip;
import com.sharnt.service.TripService;
import org.json.JSONArray;
import org.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;


@CrossOrigin(origins = "http://localhost:3000")
@RestController
@RequestMapping("/hotel")
public class HotelController {


    @Autowired
    TripService tripService;

    @GetMapping()
    @ResponseBody
    List<Trip> fetch(@Valid String bl_latitude,@Valid String tr_latitude,@Valid String bl_longitude,@Valid String tr_longitude) throws IOException, UnirestException {


        /**
         * Build the Api Url
         */
        StringBuilder sb = new StringBuilder();
        sb.append("https://travel-advisor.p.rapidapi.com/hotels/list-in-boundary?bl_latitude=");
        sb.append(bl_latitude);
        sb.append("&bl_longitude=");
        sb.append(bl_longitude);
        sb.append("&tr_longitude=");
        sb.append(tr_longitude);
        sb.append("&tr_latitude=");
        sb.append(tr_latitude);
        sb.append("&limit=10&currency=USD&subcategory=hotel%2Cbb%2Cspecialty&adults=1");
        String urlApi = sb.toString();
        System.out.println(urlApi);

        /**
         * Call the Url
         */
        HttpResponse<String> response2 = Unirest.get(urlApi)       .header("X-RapidAPI-Key", "6d491c9c48msh30e5abb72a551f4p13e118jsn6e1074011151")
                .header("X-RapidAPI-Host", "travel-advisor.p.rapidapi.com").asString();

        System.out.println(response2);
        System.out.println(response2.getBody());
        System.out.println(response2.getRawBody());


        List<Trip> listTrip = new ArrayList<Trip>();

        /**
         * Parse JSON
         */


        String jsonString = response2.getBody(); ; //assign your JSON String here
        System.out.println(jsonString);
        JSONObject obj = new JSONObject(jsonString);


        JSONArray arr = obj.getJSONArray("data"); // notice that `"data": [...]`
        System.out.println(arr);
        for (int i = 0; i < arr.length(); i++)
        {
            Trip trip = new Trip();
            trip.setType("hotel");

            try {
                trip.setLink(arr.getJSONObject(i).getString("web_url"));
            }  catch (Exception e) {
                trip.setLink(null);
            }

            try {
                trip.setLatitude(arr.getJSONObject(i).getString("latitude"));
            }  catch (Exception e) {
                trip.setLatitude(null);
            }
            try {
                trip.setLongitude(arr.getJSONObject(i).getString("longitude"));
            }  catch (Exception e) {
                trip.setLongitude(null);
            }

            try {
                trip.setDescription(arr.getJSONObject(i).getString("location_string"));
            }  catch (Exception e) {
                trip.setDescription(null);
            }

            try {
                trip.setStar(arr.getJSONObject(i).getString("rating"));
            }  catch (Exception e) {
                trip.setStar(null);
            }

            try {
                trip.setPrice(arr.getJSONObject(i).getString("price"));
            }  catch (Exception e) {
                trip.setPrice(null);
            }

            try {
                trip.setTitle(arr.getJSONObject(i).getString("name"));
            }  catch (Exception e) {
                trip.setTitle(null);
            }

            try {
                JSONObject photo  = arr.getJSONObject(i).getJSONObject("photo");
                JSONObject photo2  = photo.getJSONObject("images");
                JSONObject photo3  = photo2.getJSONObject("medium");
                trip.setPicture(photo3.getString("url"));
            }  catch (Exception e) {
                trip.setPicture(null);
            }

            if (trip.getTitle() != null){
                listTrip.add(trip);
            }

            System.out.println(i);
            System.out.println(trip);
        }

        System.out.println("test ok");
        return listTrip;
    }

    @PostMapping()
    @ResponseBody
    String saveTrip(@RequestBody @Valid Trip trip) {
        tripService.addTrip(trip);
        return "ok";
    }
}
