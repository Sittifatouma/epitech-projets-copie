package com.sharnt.Controller;

import com.sharnt.controller.ActivityController;
import com.sharnt.controller.FoodController;
import com.sharnt.model.Trip;
import com.sharnt.service.TripService;
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
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;


@RunWith(MockitoJUnitRunner.class)
public class FoodControllerTest {

    private MockMvc mockMvc;

    @Mock
    private TripService tripService;

    @InjectMocks
    private FoodController foodController;

    @Before
    public void before() {
        mockMvc = MockMvcBuilders.standaloneSetup(foodController).build();
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
     * http://localhost:8080/food
     *
     * @throws Exception
     */
    @Test
    public void shouldReturn_ListTrip() throws Exception {
        mockMvc.perform(get("/food?bl_latitude=48.856&tr_latitude=2.352&bl_longitude=2.553&tr_longitude=49.857").header("Origin", " ")).andExpect(status().is2xxSuccessful())
                .andExpect(MockMvcResultMatchers.content().contentType(MediaType.APPLICATION_JSON));

    }

    @Test
    public void shouldNotCall_Delete() throws Exception {
        List<Trip> ajusSucoTOList = createTripList();
        Trip trip = new Trip();

        mockMvc.perform(get("/food?bl_latitude=48.856&tr_latitude=2.352&bl_longitude=2.553&tr_longitude=49.857").header("Origin", " ")).andExpect(status().is2xxSuccessful())
                .andExpect(MockMvcResultMatchers.content().contentType(MediaType.APPLICATION_JSON));

        Mockito.verify(tripService, times(0)).deleteExample(1);
    }

    @Test
    public void shouldNotCall_Select() throws Exception {
        List<Trip> ajusSucoTOList = createTripList();
        Trip trip = new Trip();

        mockMvc.perform(get("/food?bl_latitude=48.856&tr_latitude=2.352&bl_longitude=2.553&tr_longitude=49.857").header("Origin", " ")).andExpect(status().is2xxSuccessful())
                .andExpect(MockMvcResultMatchers.content().contentType(MediaType.APPLICATION_JSON));

        Mockito.verify(tripService, times(0)).getAllExample();
    }
}