import { useParams } from "react-router-dom";

export default function MovieDetail() {
  const { id } = useParams<{ id: string }>();

  return <h1>Movie ID: {id}</h1>;
}