function StatsCard({ title, value }) {

  return (
    <div className="bg-white rounded-2xl shadow-md p-6 hover:scale-105 hover:shadow-xl transition duration-300">

      <h2 className="text-gray-500 text-sm">
        {title}
      </h2>

      <p className="text-3xl font-bold mt-2">
        {value}
      </p>

    </div>
  );
}

export default StatsCard;