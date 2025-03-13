import { render, screen, waitFor } from "@testing-library/react";
import { SWRConfig } from "swr";
import BrandCount from "../components/BrandCount";

describe("BrandCount Component", () => {
  beforeEach(() => {
    // Réinitialiser les mocks avant chaque test
    global.fetch = jest.fn();
  });

  test("shows loading state", async () => {
    // Simuler une requête qui prend du temps à répondre
    global.fetch.mockImplementation(
      () => new Promise((resolve) => setTimeout(resolve, 100))
    );

    render(
      <SWRConfig value={{ provider: () => new Map(), dedupingInterval: 0 }}>
        <BrandCount />
      </SWRConfig>
    );

    // Vérifier l'état de chargement initial
    expect(screen.getByText(/loading.../i)).toBeInTheDocument();
  });

  test("shows error state", async () => {
    // Simuler une erreur
    global.fetch.mockRejectedValue(new Error("Failed to fetch"));

    render(
      <SWRConfig value={{ provider: () => new Map(), dedupingInterval: 0 }}>
        <BrandCount />
      </SWRConfig>
    );

    // Attendre que le message d'erreur apparaisse
    await waitFor(() => {
      expect(screen.getByText(/failed to load/i)).toBeInTheDocument();
    });
  });

  test("displays data when loaded", async () => {
    // Simuler une réponse réussie
    const mockData = [
      { _id: "Brand1", count: 10 },
      { _id: "Brand2", count: 20 },
    ];

    global.fetch.mockResolvedValue({
      ok: true,
      json: async () => mockData,
    });

    render(
      <SWRConfig value={{ provider: () => new Map(), dedupingInterval: 0 }}>
        <BrandCount />
      </SWRConfig>
    );

    // Vérifier que le contenu est affiché une fois chargé
    await waitFor(() => {
      expect(screen.getByText(/Vehicle Count by Brand/i)).toBeInTheDocument();
    });
  });

  afterEach(() => {
    jest.clearAllMocks();
  });
});
