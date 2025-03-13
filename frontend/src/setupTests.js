import "@testing-library/jest-dom";
import { jest } from "@jest/globals";

// Environnement
process.env.REACT_APP_API_URL = "http://localhost:5005";

// Mock global fetch
global.fetch = jest.fn();

// Mock Chart.js
jest.mock("chart.js", () => ({
  Chart: { register: jest.fn() },
  ArcElement: jest.fn(),
  Tooltip: jest.fn(),
  Legend: jest.fn(),
}));

// Mock react-chartjs-2
jest.mock("react-chartjs-2", () => ({
  Pie: () => null,
}));

// Mock d3-scale-chromatic
jest.mock(
  "d3-scale-chromatic",
  () => ({
    schemePastel1: ["#color1", "#color2", "#color3"],
  }),
  { virtual: true }
);
