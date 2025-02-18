import React from 'react';
import App from './App'; 
import { shallow } from 'enzyme';
import Header from './components/Header/Header'
import Map from './components/Map/Map';
import List from './components/List/List';
import { exec } from 'child_process';
import ItineraireCalcul from './components/ItineraireCalcul/ItineraireCalcul';

describe('App', () => {

    let appWrapper;

    beforeAll(() => {
        appWrapper = shallow(<App />);
    });

    it('Component Header', () => {
        appWrapper.find(Header);
    })

    it('Component List', () => {
        const list = appWrapper.find(List);
        expect(list).toHaveLength(1);
    })

    it('Component Map', () => {
        appWrapper.find(Map);
    })

    it('Component Itineraire', () => {
        appWrapper.find(ItineraireCalcul);
    })
});