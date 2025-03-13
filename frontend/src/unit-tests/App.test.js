import React from "react";
import { render, screen } from "@testing-library/react";
import App from "../App"; 

describe("App Component", () => {
  test("renders the correct text", () => {
    render(<App />);
    expect(screen.getByText(/Some test text/i)).toBeInTheDocument();
  });

  test("applies the correct CSS classes", () => {
    render(<App />);
    const divElement = screen.getByText(/Some test text/i);
    expect(divElement).toHaveClass("bg-orange-500", "text-white");
  });
});
