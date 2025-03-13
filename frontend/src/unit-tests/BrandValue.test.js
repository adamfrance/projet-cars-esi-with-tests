import React from "react";
import { render, screen } from "@testing-library/react";
import BrandValue from "../components/BrandValue";

describe("BrandValue", () => {
  test("renders without crashing", () => {
    render(<BrandValue />);
    expect(document.body).toBeInTheDocument();
  });
});
