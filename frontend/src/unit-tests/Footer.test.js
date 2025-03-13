import React from "react";
import { render, screen } from "@testing-library/react";
import Footer from "../components/Footer";

describe("Footer", () => {
  test("renders without crashing", () => {
    render(<Footer />);
    expect(document.body).toBeInTheDocument();
  });
});
