import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import CarsDropdown from "../components/CarsDropdown";

describe("CarsDropdown", () => {
  test("renders without crashing", () => {
    render(<CarsDropdown />);
    expect(screen.getByRole("combobox")).toBeInTheDocument();
  });

  test("renders all brands option when allCars is true", () => {
    render(<CarsDropdown allCars={true} />);
    expect(screen.getByText("All brands")).toBeInTheDocument();
  });

  test("does not render all brands option when allCars is false", () => {
    render(<CarsDropdown allCars={false} />);
    expect(screen.queryByText("All brands")).not.toBeInTheDocument();
  });

  test("calls selectHandler when option is selected", () => {
    const mockSelectHandler = jest.fn();
    render(<CarsDropdown selectHandler={mockSelectHandler} />);

    fireEvent.change(screen.getByRole("combobox"), {
      target: { value: "Fiat" },
    });
    expect(mockSelectHandler).toHaveBeenCalled();
  });

  test("displays correct selected value", () => {
    render(<CarsDropdown elValue="Fiat" />);
    expect(screen.getByRole("combobox")).toHaveValue("Fiat");
  });
});
