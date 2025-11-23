export default function TextBox({ rows = 3,...props }) {
  return (
    <textarea
      rows={rows}
      className="textbox"
      {...props}
    />
  );
}
