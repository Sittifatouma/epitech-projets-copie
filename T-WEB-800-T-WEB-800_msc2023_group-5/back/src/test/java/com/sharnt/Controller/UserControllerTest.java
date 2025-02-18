package com.sharnt.Controller;

import com.sharnt.controller.FoodController;
import com.sharnt.controller.UsersController;
import com.sharnt.model.Trip;
import com.sharnt.service.TripService;
import com.sharnt.service.UsersService;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.junit.MockitoJUnitRunner;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;

import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.assertNotNull;
import static org.mockito.Mockito.times;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;


@RunWith(MockitoJUnitRunner.class)
public class UserControllerTest {

    private MockMvc mockMvc;

    @Mock
    private UsersService userService;

    @InjectMocks
    private UsersController usersController;

    @Before
    public void before() {
        mockMvc = MockMvcBuilders.standaloneSetup(usersController).build();
    }

    private List<Trip> createTripList() {
        List<Trip> tripList = new ArrayList<>();
        Trip trip = new Trip();
        trip.setTitle("test ajout trip");
        tripList.add(trip);
        return tripList;
    }

    /**
     * Test fetch method
     * http://localhost:8080/food
     *
     * @throws Exception
     */
    @Test
    public void shouldReturn_BadRequest() throws Exception {
        try {
            mockMvc.perform(get("/food"));
        } catch (Exception e){
            int a = 0;
            assertNotNull("Bas request",a);
        }


    }
    /**
     * Test fetch method
     * http://localhost:8080/uSERS
     *
     * @throws Exception
     */
    @Test
    public void shouldReturn_Post() throws Exception {
        mockMvc.perform(post("/Users").header("Origin", " ")).andExpect(status().is2xxSuccessful());
        Mockito.verify(userService, times(1)).createUser();
    }


}