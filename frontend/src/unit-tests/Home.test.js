import React from "react";
import { render, screen } from "@testing-library/react";
import Home from "../components/Home";

describe("Home", () => {
  test("renders without crashing", () => {
    render(<Home />);
    expect(document.body).toBeInTheDocument();
  });
});
