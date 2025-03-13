import React from "react";
import { render, screen } from "@testing-library/react";
import Card from "../components/Card";

describe("Card Component", () => {
  test("renders car details correctly", () => {
    const car = {
      brand: "Tesla",
      make: "Model S",
      year: 2020,
      km: 50000,
    };

    render(<Card car={car} />);
    expect(screen.getByText(/Tesla - Model S/i)).toBeInTheDocument();
    expect(screen.getByText(/50000 Km \/ Year: 2020/i)).toBeInTheDocument();
  });
});
