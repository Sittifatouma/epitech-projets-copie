import { render, screen, cleanup } from "@testing-library/react";
import ItineraireCalcul from "./ItineraireCalcul";

test('Render Itineraire', () => {
    render(<ItineraireCalcul />);

    const itineraireElement = screen.getByTestId('iti_1')

    expect(itineraireElement).toHaveTextContent('Attend je charge la page 🏋🏾🏆');
})