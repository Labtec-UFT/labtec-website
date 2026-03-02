export default function Button({text}: {text: string}) {
    return(
        <>
            <button type="submit" className="w-85 p-2 rounded-md bg-black text-white hover:cursor-pointer">
                {text}
            </button>
        </>
    );
}