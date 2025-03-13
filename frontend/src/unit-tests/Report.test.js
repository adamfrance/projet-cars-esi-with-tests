import React from "react";
import { render, screen } from "@testing-library/react";
import Report from "../components/Report";

describe("Report", () => {
  test("renders without crashing", () => {
    render(<Report />);
    expect(document.body).toBeInTheDocument();
  });
});
