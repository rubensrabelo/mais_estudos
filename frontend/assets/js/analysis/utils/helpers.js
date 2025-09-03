// helpers.js
export function formatCurrency(value) {
  return `$${value.toLocaleString()}`;
}

export function formatNumber(value) {
  return value.toLocaleString();
}
