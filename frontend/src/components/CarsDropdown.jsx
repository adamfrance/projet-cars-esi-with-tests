import React from "react";
import PropTypes from "prop-types";

const CarsDropdown = ({
  selectHandler = () => {},
  allCars = false,
  elValue = "",
}) => {
  const carBrands = [
    "Fiat",
    "Opel",
    "Renault",
    "Peugeot",
    "VW",
    "Ford",
    "Honda",
    "Toyota",
  ];

  return (
    <select
      onChange={selectHandler}
      className="px-2 py-1 my-2 mx-2 rounded-lg form-select md:w-1/6"
      value={elValue}
    >
      {allCars && <option value="">All brands</option>}
      {carBrands.map((brand) => (
        <option value={brand} key={brand}>
          {brand}
        </option>
      ))}
    </select>
  );
};

CarsDropdown.propTypes = {
  selectHandler: PropTypes.func,
  allCars: PropTypes.bool,
  elValue: PropTypes.string,
};

export default CarsDropdown;
