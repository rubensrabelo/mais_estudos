export function buildPayload(formData) {
  const movie = Object.fromEntries(formData.entries());
  return {
    Series_Title: movie.Series_Title,
    Released_Year: movie.Released_Year,
    Certificate: movie.Certificate || "A",
    Runtime: movie.Runtime,
    Genre: movie.Genre,
    Overview: movie.Overview || "Descrição não informada.",
    Meta_score: parseFloat(movie.Meta_score) || 0,
    Director: movie.Director || "Desconhecido",
    Star1: movie.Star1 || "Ator 1",
    Star2: movie.Star2 || "Ator 2",
    Star3: movie.Star3 || "Ator 3",
    Star4: movie.Star4 || "Ator 4",
    No_of_Votes: parseInt(movie.No_of_Votes) || 0,
    Gross: movie.Gross || "0"
  };
}
