import React from "react";
import { render, screen } from "@testing-library/react";
import ModelCount from "../components/ModelCount";

describe("ModelCount", () => {
  test("renders without crashing", () => {
    render(<ModelCount />);
    expect(document.body).toBeInTheDocument();
  });
});
