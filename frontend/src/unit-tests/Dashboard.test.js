import React from "react";
import { render, screen } from "@testing-library/react";
import Dashboard from "../components/Dashboard";

describe("Dashboard", () => {
  test("renders without crashing", () => {
    render(<Dashboard />);
    expect(document.body).toBeInTheDocument();
  });
});
