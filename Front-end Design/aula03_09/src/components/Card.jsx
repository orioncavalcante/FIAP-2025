

const Card = () => {
    return (
        <div className="w-full max-w-md bg-white shadow-xl rounded-2xl overflow-hidden">
            <img src="https://picsum.photos/seed/picsum/200/300" alt="Imagem Ilustrativa" className="w-full h-60 object-cover" />
            <div className="p-6 text-center">
                <h2 className="text-2xl font-bold text-gray-900">Título do Card</h2>
                <p className="text-gray-600 mt-3">Esta é uma descrição de exemplo para mostrar como o Tailwin facilita a estilização</p>
                <button className="mt-5 w-full bg-blue-500 text-white py-3 rounded-lg font-semibold hover:bg-blue-700 transition duration-300">Saiba mais</button>
            </div>
        </div>
    );
}

export default Card;