import { render, screen } from "../test-utils/test-utils";
import Layout from "../components/Layout";

describe("Layout", () => {
  test("renders without crashing", () => {
    render(<Layout />);
    expect(document.body).toBeInTheDocument();
  });
});
